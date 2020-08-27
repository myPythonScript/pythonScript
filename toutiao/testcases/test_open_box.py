# # -*- coding:utf-8 -*-
from time import sleep
import random
from pages.jobPage import JobPage
from testcases import open_box
from testcases import read_book
from testcases import video_play
from testcases.actions import Actions


def test_open_box(driver):
    # 等待跳过广告
    sleep(5)
    job_page = JobPage(driver)
    # 等待界面加载完成
    driver.implicitly_wait(30)
    i = 1
    while i <= 10:
        time_item = job_page.time_itm()
        print("time_item:%s" % time_item)
        if time_item != "任务":
            print("仍在倒计时中...")
            time = int(time_item[0:2])
            time_slp = (time + 1) * 60
            print("倒计时还有%d秒" % time_slp)
            # 跳转至我的界面
            time_slp = random.randint(1, 5)
            sleep(time_slp)
            read_book.read_book(driver, job_page)
            i += 1
            print("i=%d" % i)
            continue
        else:
            print("倒计时已完成，打开宝箱")
            # 打开宝箱
            open_box.open_box(driver, job_page)
            i += 1
            print("i=%d" % i)
            Actions(driver).up_swipe()
            read_count = job_page.read_book_count()
            if read_count is True:
                video_play.video_play(driver)
            continue
    print("关闭APP")
    driver.quit()
