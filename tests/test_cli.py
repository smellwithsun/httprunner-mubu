import os
import unittest
import subprocess


class TestCli(unittest.TestCase):

    def test_hogrun_single_yaml(self):
        pass
        #todo
        # singe_api_yaml = os.path.join(
        #     os.path.dirname(__file__), "api", "get_login_submit.yaml")
        # subprocess.run("hogrun {}".format(singe_api_yaml))