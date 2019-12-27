from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time,os,allure


class Base:

    def __init__(self, driver):
        self.driver = driver

    def search_ele(self, loc, timeout=5, poll=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,"属性值") (By.XPATH,"属性值") (By.CLASS_NAME,"属性值")
        :param timeout: 搜索超时时间
        :param poll: 搜索间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1):
        """
        定位单个元素
        :param loc: 元组 (By.ID,"属性值") (By.XPATH,"属性值") (By.CLASS_NAME,"属性值")
        :param timeout: 搜索超时时间
        :param poll: 搜索间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,"属性值") (By.XPATH,"属性值") (By.CLASS_NAME,"属性值")
        :param timeout: 搜索超时时间
        :param poll: 搜索间隔
        :return:
        """
        self.search_ele(loc, timeout, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=1.0):
        """
        文本框输入
        :param loc: 元组 (By.ID,"属性值") (By.XPATH,"属性值") (By.CLASS_NAME,"属性值")
        :param text: 输入文本内容
        :param timeout: 搜索超时时间
        :param poll: 搜索间隔
        :return:
        """
        # 定位
        input_value = self.search_ele(loc, timeout, poll)
        # 清空
        input_value.clear()
        # 输入
        input_value.send_keys(text)

    def swipe_screen(self, tag=1):
        """
        滑动屏幕操作
        :param tag: 1：向上 2：向下 3：向左 4：向右
        :return:
        """
        # 获取屏幕分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        # 滑动前等待
        time.sleep(2)
        # 滑动
        if tag == 1:
            """向上"""
            # 宽*0.5 高*0.8 宽*0.5 高*0.2
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            """向下"""
            # 宽*0.5 高*0.2 宽*0.5 高*0.8
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            """向左"""
            # 宽*0.8 高*0.5 宽*0.2 高*0.5
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            """向右"""
            # 宽*0.2 高*0.5 宽*0.8 高*0.5
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    # 获取手机toast消息
    def get_toast(self,ts):
        # 获取登录失败提示信息(账号或密码错误)
        # xpath
        message_xpath = (By.XPATH, "//*[contains(@text,'{}')]".format(ts))
        # 定位方法,3秒找10次 --> 一般toast消息展示3s左右
        return self.search_ele(message_xpath,timeout=3,poll=0.3).text

    def screen_png(self,name ="截图"):
        '''截图'''
        # 图片名字
        png_name = "{}.png".format(int(time.time()))
        # 截图
        self.driver.get_screenshot_as_file("./image" + os.sep + png_name)

        with open("./image" + os.sep + png_name, "rb") as f:  # rb二进制
            # 添加图片到allure报告
            allure.attach(name, f.read(), allure.attach_type.PNG)


    '''截图方案2'''
    # 以上方法不能生成截图用此方法,因为screenshot和截图方法发生冲突
    def screen_png_adb(self,name="截图"):
        # 图片名字
        png_name = "{}.png".format(int(time.time()))
        # 使用adb截图 adb shell screencap -p /sdcard/xx.png
        os.system("adb shell screencap -p /sdcard/{}.png".format(png_name))
        # 从手机通过adb拉取图片到截图目录 image adb pull /sdcard/xx.png ./image
        os.system("adb pull /sdcard/{}.png ./image".format(png_name))

        with open("./image" + os.sep + png_name, "rb") as f:  # rb二进制
            # 添加图片到allure报告
            allure.attach(name, f.read(), allure.attach_type.PNG)



