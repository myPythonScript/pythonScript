import os

import yaml


class Data(object):
    def __init__(self, file_name):
        #
        # name = os.path.split(os.path.dirname(case_name))[-1]
        # file_name = name + '.yaml'
        # print("file_name:%s" % file_name)

        self.basePath = os.path.dirname(os.path.abspath(file_name))
        self.filePath = os.path.join(self.basePath, 'casesData', file_name)
        print(self.filePath)

    def yaml_data(self):
        with open(self.filePath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data


if __name__ == "__main__":
    data = Data("user_service.yaml").yaml_data()
    print(data)
