"""
    @File: base_action.py
    @Author: Shieh
    @Date: 2020/12/29 9:32
    @Description： 封装操作浏览器页面方法
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


class BaseAction:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def open_browser(self, browser='chrome'):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            print("ERROR: %s not found." % browser)

    def open_url(self, url=None):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator=None):
        try:
            element = self.driver.find_element_by_xpath(locator)
        except:
            print(f"元素{locator}未找到")
            element = None
        return element

    def click(self, locator=None):
        element = self.find_element(locator)
        element.click()

    def mouse_over(self, locator=None):
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def input_info(self, locator=None, data=None):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(data)

    def refresh_page(self):
        """
        刷新页面
        :return:
        """
        self.driver.refresh()

    def into_iframe(self, locator=None):
        """
        切换表单
        :param locator: 表单的定位元素
        :return:
        """
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)

    def select_info(self, locator=None, value1=None, value2=None, value3=None, value4=None, value5=None):
        """
        下拉框选择多个值
        :param locator:
        :param value1:
        :param value2:
        :param value3:
        :param value4:
        :param value5:
        :return:
        """
        element = self.find_element(locator)
        element.click()
        select_value1 = self.find_element(value1)
        select_value1.click()
        if value2 is not None:
            select_value2 = self.find_element(value2)
            select_value2.click()
        if value3 is not None:
            select_value3 = self.find_element(value3)
            select_value3.click()
        if value4 is not None:
            select_value4 = self.find_element(value4)
            select_value4.click()
        if value5 is not None:
            select_value5 = self.find_element(value5)
            select_value5.click()

    def assert_info(self, locator=None, text=None):
        if text is not None:
            try:
                assert text == str(self.find_element(locator).text)
                print("The test case succeeded.")
            except AssertionError:
                print("The test case Failed.")
                raise
        else:
            print("%s not existent." % text)

    @staticmethod
    def sleep_time(t=1):
        time.sleep(int(t))

    def close(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    a = 'zbc'
    b = '1zbc'
    try:
        assert a == b
    except AssertionError:
        print("The test case Failed.")
        raise
    else:
        print("The test case succeeded.")
