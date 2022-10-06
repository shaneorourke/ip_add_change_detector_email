import requests as rq

def ifconfig_get():
    api_link = "https://ifconfig.me"
    output = rq.get(api_link)
    return output.content

