import pytest
import os
from utils.data import Data

@pytest.fixture
def case_data(request):
    # 获取用例名称
    test_case_name = request.function.__name__
    name = os.path.split(os.path.dirname(__file__))[-1]
    file_name = name + '.yaml'
    print("file_name:%s" % file_name)
    data = Data(file_name).yaml_data()
    # 获取用例数据
    case_data = data.get(test_case_name)
    print('用例名称为：%s,用例参数为：%s' % (test_case_name, case_data))
    return (case_data)


