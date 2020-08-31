import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.web
def test_baidu_search(BaiDu):
    BaiDu.search()
