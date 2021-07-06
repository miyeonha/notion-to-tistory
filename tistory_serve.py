import json

from flask import Flask, render_template, request
from flask_caching import Cache

import requests

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


def _load_json(input_path):
    with open(input_path, "r") as rfile:
        return json.load(rfile)


def _get_access_token(parameter_dict, client_id, redirect_uri, client_secret):

    try:
        code = parameter_dict["code"]

        URL = f"https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code"

        result = requests.get(url=URL).text
        access_token = result[13:]
        return access_token

    except KeyError:
        print("Error : No code in parameters")
        return "fail"

    except Exception as e:
        print("Error : _get_access_token try catch error : ")
        print(e)
        return "fail"


def _get_blog_info(access_token):

    URL = f"https://www.tistory.com/apis/blog/info?access_token={access_token}&output=json"

    blog_info = requests.get(url=URL).json()

    try:
        if blog_info["tistory"]["status"] == "200":
            list_blogs = blog_info["tistory"]["item"]["blogs"]
            return list_blogs
        else:
            return "fail"
    except KeyError:
        print("Error : Fail to get blog information")
        return "fail"


def _convert_blog_title(list_blogs):

    list_blog_titles = []

    for blog in list_blogs:
        if blog["default"] == "Y":
            list_blog_titles.append(f"[대표 블로그] {blog['title']}")
        else:
            list_blog_titles.append(blog["title"])

    return list_blog_titles


def _get_categories(access_token, blog_title):

    list_blogs = cache.get("list_blogs")

    print("_get_categories function ")
    print("list_blogs : ")
    print(list_blogs)
    print("blog_title : ")
    print(blog_title)

    try:
        blog_name = [
            blog["name"] for blog in list_blogs if blog["title"] in blog_title
        ][0]

        print("blog_name : ")
        print(blog_name)

        URL = f"https://www.tistory.com/apis/category/list?access_token={access_token}&output=json&blogName={blog_name}"
        blog_category = requests.get(url=URL).json()

        print("blog_category : ")
        print(json.dumps(blog_category, ensure_ascii=False))

        if blog_category["tistory"]["status"] == "200":
            return [
                category["name"]
                for category in blog_category["tistory"]["item"]["categories"]
            ]

    except IndexError:
        print("Error : No blog title")
        return "fail"

    except KeyError:
        print(
            "Error : No name or title field in list_blogs or Fail to get blog categories"
        )
        return "fail"


@app.route("/write-post", methods=["POST"])
def write_post():

    selected_blog_title = cache.get("selected_blog_title")
    if not selected_blog_title:
        selected_blog_title = request.form["selected-blog-title"]
        cache.set("selected_blog_title", selected_blog_title)

    access_token = cache.get("access_token")
    list_blog_categories = _get_categories(access_token, selected_blog_title)
    if type(list_blog_categories) == "str"
    
    print("list_blog_categories : ")
    print(json.dumps(list_blog_categories, ensure_ascii=False))

    result_write_post = None
    url_post = None

    return render_template(
        "write-post.html",
        list_blog_categories=list_blog_categories,
        blog_name=selected_blog_title,
        result_write_post=result_write_post,
        url_post=url_post,
    )


@app.route("/")
def index():

    auth = _load_json("./tistory_auth.json")
    client_id = auth["client_id"]
    client_secret = auth["client_secret"]
    redirect_uri = auth["redirect_uri"]

    parameter_dict = request.args.to_dict()

    result_access_token = cache.get("access_token")
    list_blog_titles = cache.get("list_blog_titles")

    if parameter_dict and not result_access_token:
        result_access_token = _get_access_token(
            parameter_dict, client_id, redirect_uri, client_secret
        )
        cache.set("access_token", result_access_token, timeout=5 * 60)

        if result_access_token != "fail" and not list_blog_titles:
            list_blogs = _get_blog_info(result_access_token)

            print("list_blogs : ")
            print(json.dumps(list_blogs, ensure_ascii=False, indent=2))

            cache.set("list_blogs", list_blogs)

            list_blog_titles = _convert_blog_title(list_blogs)
            cache.set("list_blog_titles", list_blog_titles)

    return render_template(
        "tistory.html",
        client_id=client_id,
        redirect_uri=redirect_uri,
        result_access_token=result_access_token,
        list_blog_titles=list_blog_titles,
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
