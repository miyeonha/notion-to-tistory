import json
import os
import re


from flask import Flask, render_template, request
import markdown
from notion.client import NotionClient
from requests.sessions import REDIRECT_STATI

app = Flask(__name__)


def _load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as rfile:
        return json.load(rfile)


def _split_title_url(text_block):
    regex = r"\[(.+)\](.+)"

    list_splited = []

    matches = re.finditer(regex, text_block, re.MULTILINE)
    for match_num, match in enumerate(matches, start=1):

        if match_num == 1:
            for num in range(0, len(match.groups())):
                num = num + 1
                list_splited.append(match.group(num))
        else:
            list_splited.append(text_block)

    return list_splited


def _convert_notion(token_v2, notion_link, md_save, html_save):

    try:

        client = NotionClient(token_v2=token_v2)
        blog_home = client.get_block(notion_link)

        page_title = blog_home.title
        content = ""
        list_images = []

        for child in blog_home.children:

            block_type = child.type

            if block_type == "header":
                content += f"# {child.title}\n\n"
            elif block_type == "sub_header":
                content += f"## {child.title}\n\n"
            elif block_type == "sub_sub_header":
                content += f"### {child.title}\n\n"
            elif block_type == "text":

                list_splited = _split_title_url(child.title)
                if len(list_splited) == 1:
                    content += f"{child.title}"
                elif len(list_splited) == 2:
                    content += f"[{list_splited[0]}]({list_splited[1]})"

            elif block_type == "bulleted_list":
                content += f"- {child.title}\n\n"
            elif block_type == "code":
                content += f"```\n{child.title}\n```\n\n"
            elif block_type == "callout":
                content += f">> {child.title}\n\n"
            elif block_type == "quote":
                content += f"> {child.title}\n\n"
            elif block_type == "divider":
                content += f"***\n\n"
            elif block_type == "image":
                list_images.append(child.source)
                content += f"![image]({child.source})\n\n"

        page_title = page_title.replace(" ", "")

        converted = ["success"]
        folder_path = os.path.dirname(os.path.realpath(__file__))

        if md_save:
            md_path = f"./contents/md/{page_title}.md"
            f_md = open(md_path, "w")
            f_md.write(content)
            f_md.close()

            md_path = folder_path + md_path[1:]
            converted.append(md_path)

        if html_save:
            html_path = f"./contents/html/{page_title}.html"
            f_html = open(html_path, "w")
            md_to_html = markdown.markdown(content, extensions=["fenced_code"])
            html = markdown.markdown(md_to_html)
            f_html.write(html)
            f_html.close()

            html_path = folder_path + html_path[1:]
            converted.append(html_path)

        return converted

    except Exception as err:
        print(err)
        return ["fail"]


@app.route("/")
def index(
    token_v2=None,
    notion_link=None,
    file_path=None,
    result=None,
    md_path=None,
    html_path=None,
    client_id=None,
    redirect_uri=None,
):
    return render_template(
        "index.html",
        token_v2=token_v2,
        notion_link=notion_link,
        md_path=md_path,
        html_path=html_path,
        client_id=client_id,
        redirect_uri=redirect_uri,
    )


@app.route("/convert-notion", methods=["POST"])
def convert_notion():

    dict_auth = _load_json("./auth.json")

    token_v2 = dict_auth["token_v2"]
    client_id = dict_auth["client_id"]
    redirect_uri = dict_auth["redirect_uri"]

    notion_link = request.form["notion_link"]
    file_save = request.form.getlist("file_save")

    print(token_v2)

    md_save = False
    html_save = False
    if len(file_save) == 1:
        if file_save[0] == "md_save":
            md_save = True
        else:
            html_save = True
    elif len(file_save) == 2:
        md_save = True
        html_save = True

    converted = _convert_notion(token_v2, notion_link, md_save, html_save)

    result = converted[0]
    md_path = None
    html_path = None

    if len(converted) >= 2:
        md_path = converted[1]

    if len(converted) == 3:
        html_path = converted[2]

    return render_template(
        "index.html",
        token_v2=token_v2,
        notion_link=notion_link,
        result=result,
        md_path=md_path,
        html_path=html_path,
        client_id=client_id,
        redirect_uri=redirect_uri,
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
