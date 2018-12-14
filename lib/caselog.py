import logging

def case_log_info(case_name, url, data, excepted_res, actual_res):

    logging.info("="*100)
    logging.info("请求用例：{}".format(case_name))
    logging.info("接口地址：{}".format(url))
    logging.info("请求数据：{}".format(data))
    logging.info("期望结果：{}".format(excepted_res))
    logging.info("实际结果：{}".format(actual_res))