import unittest
import requests
import json

from lib import load_data
from lib.caselog import case_log_info
from conf import config

class TestQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "query")
    #查询成功
    def test_query_success(self):
        case_data = load_data.get_case(self.sheet, "test_query_success")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.get(url=url, params=data)
        case_log_info("test_bind_success", url, case_data[3], case_data[4], res.text)
        #print(res.text)
        self.assertEqual(res.json()["code"], case_data[5])
        self.assertEqual(res.json()["msg"], case_data[6])

    #无查询信息
    def test_query_nomessage(self):
        case_data = load_data.get_case(self.sheet, "test_query_nomessage")
        url = case_data[1]
        data = json.loads(case_data[3])
        res = requests.get(url=url, params=data)
        case_log_info("test_query_nomessage", url, case_data[3], case_data[4], res.text)
        self.assertDictEqual(res.json(), json.loads(case_data[4]))

if __name__ == '__main__':
    unittest.main(verbosity=2)