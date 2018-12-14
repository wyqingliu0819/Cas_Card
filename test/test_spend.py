import unittest
import requests
import json

from lib import load_data
from lib.caselog import case_log_info
from conf import config

class TestSpend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "spend")
    #消费成功
    def test_spend_normal(self):
        case_data = load_data.get_case(self.sheet, "test_spend_normal")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_spend_normal", url, case_data[3], case_data[4], res.text)
        #print(res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #消费金额为空
    def test_spend_money_null(self):
        case_data = load_data.get_case(self.sheet, "test_spend_money_null")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_spend_money_null", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #余额不足
    def test_spend_money_noenough(self):
        case_data = load_data.get_case(self.sheet, "test_spend_money_noenough")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_spend_money_noenough", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

if __name__ == '__main__':
    unittest.main(verbosity=2)