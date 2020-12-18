"""读取数据"""
import os
import yaml


class Data(object):
    def __init__(self, file_name):
        #
        # name = os.path.split(os.path.dirname(case_name))[-1]
        # file_name = name + '.yaml'
        # print("file_name:%s" % file_name)

        # 框架中的数据读取
        # self.basePath = os.path.dirname(os.path.abspath(file_name))
        # self.filePath = os.path.join(self.basePath, 'casesData', file_name)
        # print(self.filePath)

        # 当前文件路径的数据读取
        self.basePath = os.path.dirname(os.path.dirname(os.path.abspath(file_name)))
        self.filePath = os.path.join(self.basePath, 'casesData', file_name)
        print(self.filePath)

    def yaml_data(self):
        with open(self.filePath, 'r', encoding="utf-8") as file:
            lines = []
            for line in file.readlines():
                if line != '\n':
                    lines.append(line)
            file.close()
        with open(self.filePath, 'w', encoding="utf-8") as f:
            flag = 0
            for line in lines:
                if "&collect_id" in line and '#' not in line:

                    break
                    # lefstr = line.split(":")[0]
                    # print(lefstr)
                    # newlen = "{0}:{1}".format(lefstr, "123")
                    # print("newlen:%s" % newlen)
                    # line = newlen
                    # f.write("%s\n" % line)
                    # flag = 1
                else:
                    # f.write("%s" % line)
                    pass
            print("line is:%s" % line)
            f.close()
            return flag


if __name__ == "__main__":
    data = Data("user_service.yaml").yaml_data()
    print(data)
