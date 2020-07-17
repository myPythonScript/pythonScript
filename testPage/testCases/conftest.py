# -*- coding:utf-8 -*-

import pytest
from utils.data import Data


@pytest.fixture(scope='session')
def data():
    data = Data("testData.csv").data()
    return data