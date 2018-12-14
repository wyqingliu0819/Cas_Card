import unittest
from conf import config
from lib import send_report

from lib.HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(config.test_path)
#unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    with open (config.report_file, "wb") as f:
        HTMLTestRunner(stream=f, title="加油卡测试报告", description="测试报告").run(suite)
        if config.is_send_report:
            send_report.send_mail()
            config.logging.info('邮件发送成功')