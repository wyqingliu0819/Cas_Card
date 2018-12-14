import unittest
import requests
import json

from lib import load_data
from lib.caselog import case_log_info
from conf import config

class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "recharge")
    #充值成功
    def test_recharge_normal(self):
        case_data = load_data.get_case(self.sheet, "test_recharge_normal")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)

        case_log_info("test_recharge_normal", url, case_data[3], case_data[4], res.text)
        res_code = res.json()["code"]
        res_msg = res.json()["msg"]
        #print(res.text)
        self.assertEqual(res_code, case_data[5])
        self.assertEqual(res_msg, case_data[6])

    #金额不能为空
    def test_recharge_money_null(self):
        case_data = load_data.get_case(self.sheet, "test_recharge_money_null")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_recharge_money_null", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #加油卡号不存在
    def test_recharge_cardnum_no(self):
        case_data = load_data.get_case(self.sheet, "test_recharge_cardnum_no")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_recharge_cardnum_no", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))


if __name__ == '__main__':
    unittest.main(verbosity=2)