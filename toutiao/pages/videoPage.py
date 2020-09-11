# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from pages.page import Page
from pages.jobPage import JobPage


class VideoPage(Page):
    # 视频
    open_video_loc = ("id", "com.ss.android.article.lite:id/zh")
    # 视频卡片
    video_loc = ("id", "com.ss.android.article.lite:id/b_")
    # 播放时长
    video_time_loc = ("id", "com.ss.android.article.lite:id/ic")
    # 播放按钮
    play_btn_loc = ("id", "com.ss.android.article.lite:id/jf")
    # 关闭广告
    close_advert_loc = ("id", "com.ss.android.article.lite:id/e6")
    # 重播
    replay_btn_loc = ("id", "com.ss.android.article.lite:id/ie")
    # 广告视频
    advert_video_loc = ("id", "com.ss.android.article.lite:id/pw")

    def count_video1(self):
        count_video = self.driver.find_elements(*self.open_video_loc)
        return count_video

    def count_video2(self):
        count_video = self.driver.find_elements(*self.video_loc)
        return count_video

    def video_time_itm(self):
        self.driver.find_element(*self.video_time_loc)

    def close_advert_itm(self):
        close_ad = self.driver.find_elements(*self.close_advert_loc)
        return close_ad

    def play_btn(self):
        play_buttons = self.driver.find_elements(*self.play_btn_loc)
        return play_buttons

    def replay_itm(self):
        # replay_itm = self.driver.find_elements(*self.replay_btn_loc)
        # print("重播：%s" % replay_itm)
        # # res = assert replay_itm in self.driver.page_source
        # # print("res:%s" % res)
        # if len(replay_itm) == 0:
        #     return False
        # else:
        #     return True
        res = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "com.ss.android.article.lite:id/ie")), message="timeout")
        if res == 'timeout':
            return False
        else:
            return True

    def is_advert(self):
        self.driver.find_element(*self.advert_video_loc)

    def play_video(self):
        play_buttons = self.play_btn()
        for i in play_buttons:
            i.click()
            res = self.replay_itm()
            if res is True:
                continue
            else:
                break
