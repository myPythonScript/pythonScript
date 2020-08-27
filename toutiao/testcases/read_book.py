# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def read_book(driver, job_page):
    job_page.my_itm()
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.ID, "com.bytedance.common.plugin.edgeplugin:id/mine_novel_history_imgv")))
    job_page.book_itm()
    for j in range(1, 30):
        book_video = job_page.book_video_itm()
        print("book video：%s" % book_video)
        if len(book_video) != 0:
            print("广告")
            book_video[0].click()
            sleep(20)
            driver.back()
        # sleep_time = random.randint(2, 5)
        # sleep(sleep_time)
        size = driver.get_window_size()
        width = size['width']
        height = size["height"]
        driver.swipe(width*0.9, height/2, width*0.2, height/2)
        print("第%d页" % j)
        continue
    driver.keyevent(4)

