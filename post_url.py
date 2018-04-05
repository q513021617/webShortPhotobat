import requests

def post_url_to_baidu():

    file={'file':open('urls.txt','rb')}

    response=requests.post(url="http://data.zz.baidu.com/urls?site=htmlmuban.zhiyigo.cn&token=89c899zmSyQicCmj",files=file)
    print(response.text)


if __name__ == '__main__':
    post_url_to_baidu()