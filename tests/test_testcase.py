import os
import unittest
from httprunner_mubu.load import load_yaml
from httprunner_mubu.runner import run_yaml


class TestSingeApi(unittest.TestCase):
    """
    加载与原始请求数据一样的接口请求参数
    """
    def test_loader_testcase(self):
        #相对路径
        singe_api_yaml =os.path.join(os.path.dirname(__file__),"testcase","mubu_login.yaml")
        load_json =load_yaml(singe_api_yaml)
        print(load_json)
        # self.assertEqual(load_json["request"]["url"],"https://mubu.com/")
        self.assertIsInstance(load_json,list)
        self.assertEqual(len(load_json),3)
    def test_run_yaml_yaml(self):
        testcase_api_yaml = os.path.join(os.path.dirname(__file__), "testcase", "mubu_login.yaml")
        r= run_yaml(testcase_api_yaml)
        self.assertEqual(len(r),4)
