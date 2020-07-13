# -*- coding:utf-8 -*-
import os
import pytest
from utils.data import Data
from utils.api import API
from utils.db import DB





@pytest.fixture(scope='session')
def api():
    api = API()
    return api


@pytest.fixture(scope='session')
def db():
    db = DB()
    db.close()





