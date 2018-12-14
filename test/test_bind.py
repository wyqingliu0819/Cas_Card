import unittest
import requests
import json

from lib import db
from lib import load_data
from lib.caselog import case_log_info
from conf import config

class TestBind(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "bind")
    #绑定成功
    def test_bind_success(self):
        case_data = load_data.get_case(self.sheet, "test_bind_success")
        url = case_data[1]
        data = json.loads(case_data[3])

        sql1 = "select userId from cardinfo where cardNumber='%s'" % data["CardInfo"]["cardNumber"]
        sql2 = "update cardinfo set cardstatus=null, userId=null where cardNumber='%s'" % data["CardInfo"][
            "cardNumber"]
        if db.db_query(sql1):        #判断加油卡是否被绑定
            db.db_change(sql2)      # 删除加油卡的绑定信息

        res = requests.post(url=url, json=data)
        case_log_info("test_bind_success", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))
        #删除加油卡的绑定信息
        db.db_change(sql2)

    #卡号为空
    def test_bind_cardnum_null(self):
        case_data = load_data.get_case(self.sheet, "test_bind_cardnum_null")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_bind_cardnum_null", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #只能绑定两张卡
    def test_bind_two(self):
        case_data = load_data.get_case(self.sheet, "test_bind_two")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_bind_two", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

    #加油卡号不存在
    def test_bind_card_noexist(self):
        case_data = load_data.get_case(self.sheet, "test_bind_card_noexist")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.post(url=url, json=data)
        case_log_info("test_bind_card_noexist", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))




if __name__ == '__main__':
    unittest.main(verbosity=2)