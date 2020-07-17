# -*- coding:utf-8 -*-

import os
import csv


class Data(object):
    def __init__(self, file_name):
        # 本文件内的路径
        # self.abs_path = os.path.dirname(os.path.dirname(os.path.abspath(file_name)))

        # 框架中的路径
        self.abs_path = os.path.dirname(os.path.abspath(file_name))
        self.file_path = os.path.join(self.abs_path, 'data', file_name)
        print(self.file_path)

    def data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            case_data = list(csv.reader(f))
            return case_data[0][1]

if __name__ == '__main__':
    data = Data("testData.csv").data()
    print(data)
