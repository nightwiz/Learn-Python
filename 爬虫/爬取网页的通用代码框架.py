import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "main":
    url = "http://www.baidu.com"
    print(getHtmlText(url))
