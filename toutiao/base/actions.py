def window_size(driver):
    size = driver.get_window_size()
    print(size)
    width = size['width']
    height = size["height"]
    return width, height


# 上滑
def up_swipe(driver):
    width, height = window_size(driver)
    print("width:%s, height:%s" % (width, height))
    driver.swipe(width / 2, height * 0.9, width / 2, height * 0.1)


# 下滑
def down_swipe(driver):
    width, height = window_size(driver)
    print("width:%s, height:%s" % (width, height))
    driver.swipe(width / 2, height * 0.2, width / 2, height * 0.8)


# 左滑
def left_swipe(driver):
    width, height = window_size(driver)
    print("width:%s, height:%s" % (width, height))
    driver.swipe(width * 0.9, height / 2, width * 0.2, height / 2)


# 右滑
def right_swipe(driver):
    width, height = window_size(driver)
    print("width:%s, height:%s" % (width, height))
    driver.swipe(width * 0.2, height / 2, width * 0.9, height / 2)



