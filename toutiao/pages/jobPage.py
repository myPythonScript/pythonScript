# -*- coding:utf-8 -*-
from time import sleep
from pages.page import Page


class JobPage(Page):
    # 任务按钮
    job_btn_loc = ("id", "com.ss.android.article.lite:id/ex")

    # 宝箱
    box_img_loc = ("xpath",
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[13]/android.view.View/android.widget.Image")
    # 宝箱打开后的广告
    video_btn_loc = ("xpath",
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
    # 倒计时完成
    time_btn_loc = ("id", "com.ss.android.article.lite:id/ey")

    # 任务界面的开宝箱按钮
    now_open_btn_loc = ("id", "com.ss.android.article.lite:id/a_4")

    # 小说阅读次数
    book_read_loc = ("xpath", "//*[contains(@text, '每天可赚1500金币，已完成')]")

    # 导航栏的“任务”
    def job_itm(self):
        self.driver.find_elements(*self.job_btn_loc)[3].click()
        print("跳转至任务界面")

    # 底部导航栏“视频”
    def video_itm(self):
        self.driver.find_elements(*self.job_btn_loc)[1].click()
        print('跳转至"视频"界面')

    # 导航栏的“我的”
    def my_itm(self):
        self.driver.find_elements(*self.job_btn_loc)[4].click()
        print('跳转至"我的"界面')

    # 判断倒计时是否完成
    def is_time_to_open(self):
        print("倒计时是否完成")
        self.driver.implicitly_wait(20)
        text = self.driver.find_elements(*self.time_btn_loc)[3].get_attribute("text")
        if text != "任务":
            print("仍在倒计时中...")
            return False
        else:
            print("倒计时已完成，可以打开宝箱")
            return True

    # 打开任务界面的宝箱
    def now_open_itm(self):
        now_open_itm = self.driver.find_elements(*self.now_open_btn_loc)
        return now_open_itm

    # 点击宝箱
    def box_itm(self):
        self.driver.find_element(*self.box_img_loc).click()

    # 打开宝箱后的广告
    def box_video(self):
        self.driver.find_element(*self.video_btn_loc).click()

    # 判断小说阅读次数是否完成
    def read_book_count(self):
        read_book_count = self.driver.find_elements(*self.book_read_loc)
        read_text = read_book_count[0].get_attribute("text")
        print(read_text)
        if read_text == "每天可赚1500金币，已完成30/30次":
            return True

    def open_box(self):
        # 宝箱
        self.box_itm()
        self.driver.implicitly_wait(30)
        # 点击看视频
        self.box_video()
        sleep(20)
