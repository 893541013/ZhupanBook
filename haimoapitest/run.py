import pytest
import datetime
# flask跑server运行网页


# 自动运行所有的测试用例
report_html = "--html=./report/{}/report/test.html".format(datetime.datetime.now().strftime('%Y%m%d'))


# pytest-html测试报告
pytest.main(
    ['-s', report_html]
)

# allure命令行模式：jenkins持续集成


# 指定每次运行case都使用同一个日志文件来解决： 时间戳（理解为时间点）
# 取当前的这个时间点来作为唯一的id值
# 2021-07-27-20-53-30

# c_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')    # 获取当前时间并且转换成时间戳
# print(c_time)
# c1 = datetime.datetime.now().strftime('%Y%m%d%H')
# print(c1)

# log_file = "./report/{}/{}.log".format(datetime.datetime.now().strftime('%Y%m%d%H'), datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
# print(log_file)
# log_file = "./report/{}/{}.log".format(
#                     datetime.datetime.now().strftime('%Y%m%d'), 
#                     datetime.datetime.now().strftime('%Y%m%d%H')
#                 )
# print(log_file)

# 规定日志的格式 ./report/2021072721/
