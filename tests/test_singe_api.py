import os
import unittest
from httprunner_mubu.load import load_yaml
from httprunner_mubu.runner import run_yaml


class TestSingeApi(unittest.TestCase):
    """
    加载与原始请求数据一样的接口请求参数
    """
    def test_loader_singe_api(self):
        #相对路径
        singe_api_yaml =os.path.join(os.path.dirname(__file__),"api","get_homepage.yaml")
        load_json =load_yaml(singe_api_yaml)
        self.assertEqual(load_json["request"]["url"],"https://mubu.com/")
    def test_run_singe_yaml(self):
        singe_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_login.yaml")
        result = run_yaml(singe_api_yaml)
        self.assertEqual(result,True)

        singe_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_homepage.yaml")
        result = run_yaml(singe_api_yaml)
        self.assertEqual(result, True)
    def test_run_single_jsonpath(self):
        singe_api_yaml = os.path.join(os.path.dirname(__file__), "api", "get_login_submit.yaml")
        result = run_yaml(singe_api_yaml)
        self.assertEqual(result, True)
