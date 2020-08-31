# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.actions import up_swipe
from base import video_play
from pages.my_page import MyPage


def read_book(driver, job_page):
    job_page.my_itm()
    my_page = MyPage(driver)
    driver.implicitly_wait(30)
    # 等待书架中的书加载完成
    # WebDriverWait(driver, 30, 0.5).until(
    #     EC.presence_of_element_located((By.ID, "com.bytedance.common.plugin.edgeplugin:id/mine_novel_history_imgv")))
    book_img = my_page.book_itm()
    print("book_img%s" % book_img)
    # 判断书架是否为空
    if len(book_img) == 0:
        print("书架没有书，还是看视频吧")
        # 播放视频
        video_play.video_play(driver)
    else:
        print("书架中有书，看书吧")
        for j in range(1, 30):
            book_video = my_page.book_video_itm()
            print("book video：%s" % book_video)
            if len(book_video) != 0:
                print("广告")
                book_video[0].click()
                sleep(20)
                driver.back()
            # sleep_time = random.randint(2, 5)
            # sleep(sleep_time)
            up_swipe(driver)
            print("第%d页" % j)
            continue
        driver.keyevent(4)
