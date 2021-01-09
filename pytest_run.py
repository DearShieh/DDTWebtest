"""
    @File: pytest_run.py
    @Author: Shieh
    @Date: 2020/12/29 13:38
    @Description： 
"""

import os

import pytest

pytest.main(['./scripts', '--alluredir', './report', '-s'])
os.system('allure generate ./report -o ./report --clean')
