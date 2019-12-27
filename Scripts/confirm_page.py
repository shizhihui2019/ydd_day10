from selenium.webdriver.common.by import By

from Base.getDriver import get_android_driver
from Base.page import Page

"""调用各个页面确定方法正确性"""

# 实例化统一入口类
page = Page(get_android_driver("com.bjcsxq.chat.carfriend", ".module_main.activity.MainActivity"))
# 首页-点击稍后更新
page.get_home_page().click_after_btn()
# 首页-点击我
page.get_home_page().click_my_btn()
# 个人中心-点击登录注册
page.get_person_page().click_login_sigin_btn()
# 登录页面-登录操作-登录成功
# page.get_login_page().login("18722024314", "123456")

# 登录页面-登录操作-登录失败
page.get_login_page().login("18722024314", "159357")

# 获取登录提示消息 启动参数 desired_caps['automationName'] = 'Uiautomator2'
# # xpath
# message_xpath = (By.XPATH, "//*[contains(@text,'错误')]")
# # 定位方法 3s内多次循环查找
# value = page.get_setting_page().search_ele(message_xpath, timeout=3, poll=0.3).text
#
# print("提示消息:{}".format(value))

print(page.get_setting_page().get_toast("错误"))


# # 登录页面-返回按钮
# page.get_login_page().click_return_btn()


# # 登录页面-登录确认
# page.get_login_page().click_login_acc_btn()
# # 个人中心 -获取用户名
# print("用户名:{}".format(page.get_person_page().get_username()))
# # 个人中心-点击设置
# page.get_person_page().click_setting_btn()
# # 设置页面-退出操作
# page.get_setting_page().logout()
