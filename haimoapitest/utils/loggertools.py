"""
    author: liuyun
    time: 2021/07/27
"""
import datetime
from loguru import logger


class Logger():

    def __init__(self, need_log=True):
        self.my_logger = logger

        # 判断是否需要写入日志
        if need_log is True:
            log_file = log_file = "./report/{}/{}.log".format(
                    datetime.datetime.now().strftime('%Y%m%d'), 
                    datetime.datetime.now().strftime('%Y%m%d%H')
                )
            self.my_logger.add(log_file, encoding='utf-8')
    
    def info(self, content):
        """
            info日志
        """
        self.my_logger.info(content)

    def debug(self, content):
        """
            debug日志
        """
        self.my_logger.debug(content)

    def error(self, content):
        """
            error日志
        """
        self.my_logger.error(content)

    def critical(self, content):
        """
            critical日志
        """
        self.my_logger.critical(content)

    def log_before_info(self, datas, param=None):
        """
            打印接口请求的前置信息
        """
        self.info("*" * 100)
        self.info("开始请求接口:{}".format(datas[1]))
        self.info("接口地址:{}".format(datas[2]))
        if param is None:
            self.info("接口参数:{}".format(datas[3]))
        else:
            self.info("接口参数:{}".format(param))
        self.info("接口请求头:{}".format(datas[4]))

    def log_behind_info(self, res):
        """
            打印接口的返回信息
        """
        self.info(res.text)   # 返回返回值打印出来
        self.info("http状态码为{},code值为{}".format(res.status_code, res.json()["code"]))
        self.info("*" * 100)

    def log_sql_info(self, sql, res):
        """
            打印sql和sql查询结果
        """
        self.info("查询的sql语句:{}".format(sql))
        self.info("查询的sql结果:{}".format(res))

logger = Logger()


if __name__ == "__main__":
    logger = Logger()
    logger.info("12312312")
    logger.error("12312312")
    logger.debug("12312312")
    logger.critical("12312312")
