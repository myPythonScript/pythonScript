import os
import pytest_check as ck
import pytest
from jsonschema import validate



def test_register_sys_user_by_phone(case_data):
    data = case_data
    print(data)

# file_name = "test_register_sys_user_by_phone"
# data = {'methods': [{'method': 'get', 'headers': None}, {'method': 'get', 'headers': {'uId': '88731867704197357'}}], 'paramss': [{'corpusId': 78552860459270153}], 'test_register_sys_user_by_phone': 123}
# print(data.get(file_name))