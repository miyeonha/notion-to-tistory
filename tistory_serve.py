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


def _convert_blog_name(list_blogs):

    list_blog_names = []
    for blog in list_blogs:
        if blog["default"] == "Y":
            list_blog_names.append(f"[대표 블로그] {blog['title']}")
        else:
            list_blog_names.append(blog["title"])

    return list_blog_names


def _get_categories(access_token, blog_name):

    URL = f"https://www.tistory.com/apis/category/list?access_token={access_token}&output=json&blogName={blog_name}"

    blog_category = requests.get(url=URL).json()

    try:
        if blog_category["tistory"]["status"] == "200":
            return blog_category["item"]["categories"]

    except KeyError:
        print("Error : Fail to get blog categories")
        return "fail"


@app.route("/write-post", methods=["POST"])
@cache.cached(timeout=50)
def write_post():

    selected_blog_name = request.form["select-blog-name"]

    print("selected_blog_name : ")
    print(selected_blog_name)

    return render_template("write-post.html")


@app.route("/")
@cache.cached(timeout=50)
def index():

    auth = _load_json("./tistory_auth.json")
    client_id = auth["client_id"]
    client_secret = auth["client_secret"]
    redirect_uri = auth["redirect_uri"]

    parameter_dict = request.args.to_dict()

    result_access_token = None
    list_blog_names = None

    if parameter_dict and result_access_token is None:
        result_access_token = _get_access_token(
            parameter_dict, client_id, redirect_uri, client_secret
        )

        list_blog_names = None
        if result_access_token != "fail":
            list_blogs = _get_blog_info(result_access_token)

            print("list_blogs : ")
            print(json.dumps(list_blogs, ensure_ascii=False, indent=2))

            list_blog_names = _convert_blog_name(list_blogs)

            print("list_blog_names : ")
            print(json.dumps(list_blog_names, ensure_ascii=False, indent=2))

    return render_template(
        "tistory.html",
        client_id=client_id,
        redirect_uri=redirect_uri,
        result_access_token=result_access_token,
        list_blog_names=list_blog_names,
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
