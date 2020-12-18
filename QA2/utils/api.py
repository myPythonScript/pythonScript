"""接口类型"""
import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class API(object):
    @staticmethod
    def request_function(method, url, **kwargs):
        result = requests.request(method=method, url=url, **kwargs)
        result.encoding = 'utf-8'
        return result.text

    def get(self, header, url, **kwargs):
        get_res = self.request_function('get', headers=header, url=url, params=kwargs)
        return get_res

    def post_params(self, header, url, **kwargs):
        print(url)
        post_res = self.request_function('post', headers=header, url=url, params=kwargs)
        return post_res

    def post_json(self, header, url, **kwargs):
        print(url)
        post_res = self.request_function('post', headers=header, url=url, json=kwargs)
        return post_res

    def put(self, header, url, **kwargs):
        print(url)
        put_res = self.request_function("put", headers=header, url=url, json=kwargs)
        return put_res

    def delete(self, header, url, **kwargs):
        print(url)
        delete_res = self.request_function("delete", headers=header, url=url, params=kwargs)
        return delete_res

    def api_function(self, header, method, url, **kwargs):
        # print("**kwargs: %s" % (kwargs))
        if method == "get":
            res = self.get(header, url, **kwargs)
        elif method == "post":
            res = self.post_params(header, url, **kwargs)
        elif method == "put":
            res = self.put(header, url, **kwargs)
        elif method == "delete":
            res = self.delete(header, url, **kwargs)
        else:
            res = "未匹配到请求方法"
        return res


if __name__ == "__main__":
    para ={
        'id': '5fdb03a5924266ba555dbc14',
        'name': '收藏夹8'
    }
    headers = {
        "X-Token": "eyJhbGciOiJIUzI1NiJ9.eyJjY0lkIjowLCJ1c2VySWQiOiI1ZmNmMzBlZDE2YjkyOTMwMThmYjQ3OWMiLCJpYXQiOjE2MDc5OTc3MjMsImV4cCI6MTYwOTIwNzMyM30.53i5J21EElG_G0tqe8aqebu_zz3tdLKWaJvj0igTbuY"
    }
    method = "put"
    res = API().api_function(method, headers, r"http://192.168.1.91:8040/collect/modify", **para)
    print(res)
