
class Actions(object):
    def __init__(self, driver):
        self.driver = driver

    def window_size(self):
        size = self.driver.get_window_size()
        return size

    def up_swipe(self):
        result = self.window_size()
        print(result)
        width = result['width']
        height = result["height"]
        print("width:%s, height:%s" % (width, height))
        self.driver.swipe(width / 2, height * 0.9, width / 2, height * 0.5)
