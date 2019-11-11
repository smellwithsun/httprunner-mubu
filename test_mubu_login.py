import requests
import unittest
class TestmubuLogin(unittest.TestCase):
    def test_getHomepage(self):
        url ="https://mubu.com/"
        headers ={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        resp = requests.get(url,headers=headers)
        assert resp.status_code ==200

    def test_login(self):
        url ="https://mubu.com/login"
        headers ={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        resp = requests.get(url,headers=headers)
        assert resp.status_code ==200
    def test_loginpassword(self):
        url ="https://mubu.com/login"
        headers ={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
        }
        resp = requests.get(url,headers=headers)
        assert resp.status_code ==200
    def test_submit(self):
        url ="https://mubu.com/api/login/submit"
        headers ={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
        }
        data ="phone=13425463649&password=1354350240&remember=true"
        resp = requests.post(url,headers=headers,data=data)
        resp2 =resp.json()
        assert resp2["code"] ==0
        assert resp.status_code ==200
