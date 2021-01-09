"""
    @File: meishanporject.py
    @Author: Shieh
    @Date: 2020/12/29 9:44
    @Description：
"""
import time
import allure
import pytest
from tools.base_action import BaseAction
from tools.operation_yaml import read_yml_date


def read_yml(key):
    return read_yml_date("test_case")[key]


@allure.feature("Mei Shan Project")  # 项目名称
class TestAddDevice:

    @allure.title("Opening Browser")  # 标题
    def setup_class(self):
        """
        打开浏览器
        :return:
        """
        self.base_action = BaseAction()
        # self.base_action.open_browser()

    @pytest.mark.run(order=1)
    @allure.story("Add device")  # 模块分组（如：登录成功、登录失败都在登录模块）
    @pytest.mark.parametrize('add_device', read_yml("add_device"))
    def test_1add_device(self, add_device):
        """
        测试添加设备
        :param add_device:
        :return:
        """
        allure.dynamic.title(add_device["title"])  # 动态获取yaml中的title
        allure.description(add_device["description"])  # 用例描述
        test_cases = add_device["cases"]
        for cases in test_cases:
            list_case = list(cases.values())
            with allure.step(list_case[0]):  # 0在yaml文件中为name字段；1为方法名称；2为方法参数
                func = getattr(self.base_action, list_case[1])
                values = list_case[2:]
                try:
                    func(*values)
                except Exception as e:
                    png = self.base_action.driver.get_screenshot_as_png()
                    name = time.strftime('%Y-%m-%d %H:%M:%S')+list_case[0]
                    allure.attach(png, name, allure.attachment_type.PNG)
                    raise e

    @pytest.mark.run(order=2)
    @allure.story("Add monitor device")
    @pytest.mark.parametrize('add_monitor', read_yml("add_monitor_device"))
    def test_add_monitor(self, add_monitor):
        """
        测试添加监测设备（传感器）
        :param add_monitor:
        :return:
        """
        allure.dynamic.title(add_monitor["title"])  # 动态获取yaml中的title
        allure.description(add_monitor["description"])  # 用例描述
        test_cases = add_monitor["cases"]
        for cases in test_cases:
            list_case = list(cases.values())
            with allure.step(list_case[0]):  # 0在yaml文件中为name字段；1为方法名称；2为方法参数
                func = getattr(self.base_action, list_case[1])
                values = list_case[2:]
                try:
                    func(*values)
                except Exception as e:
                    png = self.base_action.driver.get_screenshot_as_png()
                    name = time.strftime('%Y-%m-%d %H:%M:%S')+list_case[0]
                    allure.attach(png, name, allure.attachment_type.PNG)
                    raise e

    @pytest.mark.run(order=3)
    @allure.story("Add NVR device")
    @pytest.mark.parametrize('add_nvr', read_yml("add_nvr_device"))
    def test_add_nvr(self, add_nvr):
        """
        测试添加NVR
        :param add_nvr:
        :return:
        """
        allure.dynamic.title(add_nvr["title"])
        allure.description(add_nvr["description"])
        test_cases = add_nvr["cases"]
        for cases in test_cases:
            list_case = list(cases.values())
            with allure.step(list_case[0]):
                func = getattr(self.base_action, list_case[1])
                values = list_case[2:]
                try:
                    func(*values)
                except Exception as e:
                    png = self.base_action.driver.get_screenshot_as_png()
                    name = time.strftime('%Y-%m-%d %H:%M:%S')+list_case[0]
                    allure.attach(png, name, allure.attachment_type.PNG)
                    raise e

    @pytest.mark.run(order=4)
    @allure.story("Add video device")
    @pytest.mark.parametrize('add_video', read_yml("add_video_device"))
    def test_add_video(self, add_video):
        """
        测试添加摄像机
        :param add_video:
        :return:
        """
        allure.dynamic.title(add_video["title"])
        allure.description(add_video["description"])
        test_cases = add_video["cases"]
        for cases in test_cases:
            list_case = list(cases.values())
            with allure.step(list_case[0]):
                func = getattr(self.base_action, list_case[1])
                values = list_case[2:]
                try:
                    func(*values)
                except Exception as e:
                    png = self.base_action.driver.get_screenshot_as_png()
                    name = time.strftime('%Y-%m-%d %H:%M:%S')+list_case[0]
                    allure.attach(png, name, allure.attachment_type.PNG)
                    raise e

    @pytest.mark.run(order=5)
    @allure.story("Add bind")
    @pytest.mark.parametrize('add_bind', read_yml("add_binging"))
    def test_add_binding(self, add_bind):
        """
        测试添加摄像机
        :param add_bind:
        :return:
        """
        allure.dynamic.title(add_bind["title"])
        allure.description(add_bind["description"])
        test_cases = add_bind["cases"]
        for cases in test_cases:
            list_case = list(cases.values())
            with allure.step(list_case[0]):
                func = getattr(self.base_action, list_case[1])
                values = list_case[2:]
                try:
                    func(*values)
                except Exception as e:
                    png = self.base_action.driver.get_screenshot_as_png()
                    name = time.strftime('%Y-%m-%d %H:%M:%S')+list_case[0]
                    allure.attach(png, name, allure.attachment_type.PNG)
                    raise e

    def teardown_class(self):
        time.sleep(1)
        self.base_action.close()
