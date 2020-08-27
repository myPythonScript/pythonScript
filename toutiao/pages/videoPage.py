# -*- coding:utf-8 -*-


class VideoPage(object):
    # 底部导航栏视频按钮
    video_btn_loc = ("id", "com.ss.android.article.lite:id/ex")
    # 视频
    open_video_loc = ("id", "com.ss.android.article.lite:id/zh")
    # 播放时长
    video_time_loc = ("id", "com.ss.android.article.lite:id/ic")
    # 播放按钮
    play_btn_loc = ("id", "com.ss.android.article.lite:id/iy")
    # 关闭广告
    close_advert_loc = ("id", "com.ss.android.article.lite:id/e6")
    # 重播
    replay_btn_loc = ("id", "com.ss.android.article.lite:id/i3")

    def __init__(self, driver):
        self.driver = driver

    # 底部导航栏视频
    def video_itm(self):
        video_ele = self.driver.find_elements(*self.video_btn_loc)[1]
        return video_ele

    def count_video(self):
        count_video = self.driver.find_elements(*self.open_video_loc)
        return count_video

    def video_time_itm(self):
        self.driver.find_element(*self.video_time_loc)

    def close_advert_itm(self):
        close_ad = self.driver.find_elements(*self.close_advert_loc)
        return close_ad

    def replay_itm(self):
        replay_itm = self.driver.find_elements(*self.replay_btn_loc)
        return replay_itm
