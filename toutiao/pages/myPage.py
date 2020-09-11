# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.page import Page
from pages.jobPage import JobPage


class MyPage(Page):
    # 小说图片
    book_img_loc = ("id", "com.bytedance.common.plugin.edgeplugin:id/mine_novel_history_imgv")
    # 返回按钮
    back_btn_loc = ("id", "com.bytedance.novelplugin:id/back_button")
    # 查看视频
    book_video_loc = ("id", "com.bytedance.novelplugin:id/novel_coin_exciting_ad_btn")
    # 小说分页标题
    book_labels_loc = ("id", "com.ss.android.article.lite:id/br")
    # 弹窗提示获取金币
    msg_img_loc = ("id", "com.ss.android.article.lite:id/a0a")
    # 立即查看按钮.
    check_btn_loc = ('id', "com.ss.android.article.lite:id/i6")

    def book_itm(self):
        self.driver.find_element(*self.book_img_loc).click()

    def back_itm(self):
        self.driver.find_elements(*self.back_btn_loc)

    def book_video_itm(self):
        book_video = self.driver.find_elements(*self.book_video_loc)
        return book_video

    def book_labels_itm(self):
        label_items = self.driver.find_elements(*self.book_labels_loc)
        return label_items

    def read_book_func(self):
        self.book_itm()
        sleep(5)
        count = 1
        while count < 30:
            book_video = self.book_video_itm()
            if len(book_video) == 0:
                print("没有广告")
                self.left_swipe()
                continue
            else:
                print("有广告")
                book_video[0].click()
                sleep(20)
                count += 1
                print("count:%s" % count)
                continue
