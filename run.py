"""
    @File: run.py
    @Author: Shieh
    @Date: 2020/12/29 10:34
    @Description： 
"""
import unittest

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover("./scripts/", pattern="test_*.py")
    unittest.TextTestRunner().run(discover)
