import allure, os


class TestAddPng:

    def test_001(self):
        # 添加txt附件到allure报告
        # allure.attach("附件名字", "附件内容")

        with open("./image" + os.sep + "abc.png", "rb") as f:  # rb二进制读
            # 添加图片到allure报告  allure.attach_type.PNG->指定图片类型
            # allure.attach("图片名字", "图片内容", allure.attach_type.PNG)
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert True
