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
    # replay_btn_loc = ("id", "com.ss.android.article.lite:id/ie")
    replay_btn_loc = ("xpath", "//*[@text='重播']")
    # 广告标记
    advert_tab_loc = ("id", "com.ss.android.article.lite:id/pw")
    # 广告视频
    advert_video_loc = ("id", "com.ss.android.article.lite:id/pw")

    # def count_video1(self):
    #     count_video = self.driver.find_elements(*self.open_video_loc)
    #     return count_video

    def video_time_itm(self):
        self.driver.find_element(*self.video_time_loc)

    def close_advert_itm(self):
        close_ad = self.driver.find_elements(*self.close_advert_loc)
        return close_ad

    def play_btn(self):
        play_buttons = self.driver.find_elements(*self.play_btn_loc)
        return play_buttons

    def replay_itm(self):
        replay_loc = "com.ss.android.article.lite:id/ie"
        result = self.wait_element_by(6, "id", replay_loc)
        return result

    def is_advert_label(self):
        advert = self.driver.find_elements(*self.advert_tab_loc)
        print("advert:%s" % advert)
        if len(advert) == 0:
            return False
        else:
            return True

    def is_advert(self):
        self.driver.find_element(*self.advert_video_loc)

    def play_video(self):
        play_buttons = self.play_btn()
        for i in play_buttons:
            advert_tab = self.is_advert_label()
            if advert_tab is True:
                print("广告视频，跳过")
                self.up_swipe()
                continue
            i.click()
            rest = self.replay_itm()
            if rest is True:
                break
