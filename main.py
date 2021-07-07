import justpy as jp
import helpers

def hello_world():
    wp = jp.WebPage()
    
    post = helpers.get_post_by_id(1)

    jp.P(a=wp, text=post["title"])
    jp.P(a=wp, text=post["body"])

    return wp

jp.justpy(hello_world)

print("Done")