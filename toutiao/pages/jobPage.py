# -*- coding:utf-8 -*-


class JobPage(object):
    def __init__(self, driver):
        self.driver = driver

    # 任务按钮
    job_btn_loc = ("id", "com.ss.android.article.lite:id/ex")
    # 宝箱
    box_img_loc = ("xpath",
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[13]/android.view.View/android.widget.Image")
    video_btn_loc = ("xpath",
                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
    # 倒计时完成
    time_btn_loc = ("id", "com.ss.android.article.lite:id/ey")
    # 任务右上角的开宝箱按钮
    now_open_btn_loc = ("id", "com.ss.android.article.lite:id/a_4")
    # 小说阅读次数
    book_read_loc = ("xpath", "//*[contains(@text, '每天可赚1500金币，已完成')]")

    # 点击栏底任务按钮
    def job_itm(self):
        self.driver.find_elements(*self.job_btn_loc)[3].click()
        print("跳转至任务界面")

    def my_itm(self):
        self.driver.find_elements(*self.job_btn_loc)[4].click()
        print('跳转至"我的"界面')

    def time_itm(self):
        text = self.driver.find_elements(*self.time_btn_loc)[3].get_attribute("text")
        print("倒计时完成")
        print(text)
        return text

    def now_open_itm(self):
        now_open_itm = self.driver.find_elements(*self.now_open_btn_loc)
        return now_open_itm

    def box_itm(self):
        self.driver.find_element(*self.box_img_loc).click()

    def box_video(self):
        self.driver.find_element(*self.video_btn_loc).click()

    def read_book_count(self):
        read_book_count = self.driver.find_elements(*self.book_read_loc)
        read_text = read_book_count[0].get_attribute("text")
        print(read_text)
        if read_text == "每天可赚1500金币，已完成30/30次":
            return True
