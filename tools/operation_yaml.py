"""
    @File: operation_yaml.py
    @Author: Shieh
    @Date: 2020/12/29 9:40
    @Description： 获取yaml中数据
"""

import yaml


def read_yml_date(data_name):
    with open("./date/" + data_name + ".yaml", 'r', encoding='utf-8') as f:
        date = yaml.safe_load(f)
        return date

# with open("./date/test_case.yaml", 'r', encoding='utf-8') as f:
#     date = yaml.safe_load(f)
# print(date)

# if __name__ == '__main__':
#     data = read_yml_date("test_case")["add_device"][0]
#     # print(data)
#     cases = data["cases"]
#     # print(cases)
#     for case in cases:
#         list_case = list(case.values())
#         print(list_case)
