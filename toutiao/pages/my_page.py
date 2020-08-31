# -*- coding:utf-8 -*-


class MyPage(object):
    def __init__(self, driver):
        self.driver = driver

    # 我的界面
    book_img_loc = ("id", "com.bytedance.common.plugin.edgeplugin:id/mine_novel_history_imgv")
    back_btn_loc = ("id", "com.bytedance.novelplugin:id/back_button")
    book_video_loc = ("id", "com.bytedance.novelplugin:id/novel_coin_exciting_ad_btn")

    # 即时推送界面
    # 弹窗提示获取金币
    msg_img_loc = ("id", "com.ss.android.article.lite:id/a0a")
    # 立即查看按钮.
    check_btn_loc = ('id', "com.ss.android.article.lite:id/i6")

    def book_itm(self):
        book = self.driver.find_elements(*self.book_img_loc)
        return book

    def back_itm(self):
        self.driver.find_elements(*self.back_btn_loc)

    def book_video_itm(self):
        book_video = self.driver.find_elements(*self.book_video_loc)
        return book_video
