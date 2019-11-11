import os
import unittest
from httprunner_mubu.load import load_yaml


class TestSingeApi(unittest.TestCase):
    """
    加载与原始请求数据一样的接口请求参数
    """
    def test_loader_singe_api(self):
        #相对路径
        singe_api_yaml =os.path.join(os.path.dirname(__file__),"api","get_homepage.yaml")
        load_json =load_yaml(singe_api_yaml)
        self.assertEqual(load_json["url"],"https://mubu.com/")

