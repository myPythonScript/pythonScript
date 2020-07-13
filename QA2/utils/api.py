import requests


class API(object):
    def req_func(self, meth, url, **kwargs):
        self.res = requests.request(method=meth, url=url, **kwargs)
        self.res.encoding = 'utf-8'
        return self.res.text

    def get(self, url, **kwargs):
        self.res = self.req_func('get', url=url, params=kwargs)
        return self.res

    def post(self, url, **kwargs):
        print(url)
        self.res = self.req_func('post', url=url, json=kwargs)
        return self.res


if __name__ == "__main__":
    para = {
        "mobile": "13572561700"
    }
    res = API().post(r"http://114.67.225.196/auth-service/code/sms", **para)
    print(res)
