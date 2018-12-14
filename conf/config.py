import logging
import os

#数据库配置
db_host="115.28.108.130"
db_port=3306
db_user='test'
db_password='123456'
db_db="longtengserver"

#路径配置
config_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(config_path))    #项目的绝对路径

data_file = os.path.join(project_path, "data", "test_data.xlsx")
log_file = os.path.join(project_path, "log", "log.txt")
report_file = os.path.join(project_path, "report", "report.html")
test_path = os.path.join(project_path, "test")

#日志配置
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file)

#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'wyqingliu0819@163.com'
smtp_password = '5071yun10wy'
smtp_subject = '测试报告'

receive = '1150714303@qq.com'
body = '邮件为测试报告'
is_send_report = True  # 是否发送邮件


# if __name__ == "__main__":
#     logging.info("hzjdh都好都好")