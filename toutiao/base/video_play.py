# -*- coding:utf-8 -*-
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.videoPage import VideoPage
from base.actions import up_swipe


def video_play(driver):
    print("跳转至视频分页界面")
    sleep(3)
    vid_page = VideoPage(driver)
    video_ele = vid_page.video_itm()
    video_ele.click()
    driver.implicitly_wait(30)
    # 获取一屏视频个数
    count_video = vid_page.count_video2()
    for v in count_video:
        # 播放视频
        v.click()
        while True:
            replay_func = vid_page.replay_itm()
            if replay_func:
                replay_btn_loc = "com.ss.android.article.lite:id/i3"
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, replay_btn_loc)), message='timeout')
                break
            # sleep(60)
            # replay_btn = vid_page.replay_itm()
            # print("replay_btn:%s" % replay_btn)
            continue
        up_swipe(driver)
        driver.back()
