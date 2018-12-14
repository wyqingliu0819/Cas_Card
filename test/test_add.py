import unittest
import requests
import json

from lib import db
from lib import load_data
from lib.caselog import case_log_info
from conf import config

class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "add")
    #添加卡成功
    def test_add_normal(self):
        case_data = load_data.get_case(self.sheet, "test_add_normal")
        url = case_data[1]
        data = json.loads(case_data[3])
        card_numeber = data["CardInfo"]["cardNumber"]
        if card_numeber:    #数据准备
            db.del_card(card_numeber)
        res = requests.post(url=url, json=data)

        case_log_info("test_add_normal", url, case_data[3], case_data[4], res.text)

        self.assertDictEqual(res.json(), json.loads(case_data[4]))
        db.del_card(card_numeber)

    #加油卡已存在
    def test_add_card_exist(self):
        case_data = load_data.get_case(self.sheet, "test_add_card_exist")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_add_card_exist", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #业务id无效
    def test_add_methodId_invalid(self):
        case_data = load_data.get_case(self.sheet, "test_add_methodId_invalid")
        url = case_data[1]
        data = json.loads(case_data[3])
        #print(data)
        res = requests.post(url=url, json=data)
        case_log_info("test_add_methodId_invalid", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

if __name__ == '__main__':
    #print("main")
    unittest.main(verbosity=2)