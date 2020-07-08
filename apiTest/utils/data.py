import os
import yaml
import data

class Data(object):
    def __init__(self, fileName):
        self.filePath = os.path.dirname(os.path.abspath(fileName))
        self.dataPath = os.path.join(self.filePath, 'data', fileName)
        print(self.dataPath)

    def yamlData(self):
        with open (self.dataPath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data     

if __name__ == "__main__":
    data = Data("data.yaml").yamlData()
    print(data)