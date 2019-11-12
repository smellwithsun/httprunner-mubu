import requests
import jsonpath
from requests import sessions
from httprunner_mubu.load import load_yaml
from httprunner_mubu.validate import is_api, is_testcase
session = sessions.Session()
#requests默认每次发起请求都会发起一次session，所以需要session共享
def extact_json_field(resp,json_field):
    value =jsonpath.jsonpath(resp.json(),json_field)
    return value[0]

def run_api(api_info):
    pass
    request = api_info["request"]

    method = request.pop("method")
    url = request.pop("url")
    resp = session.request(method, url, **request)

    validator_mapping = api_info["validate"]

    for key in validator_mapping:
        if "$" in key:
            actual_key = extact_json_field(resp, key)
        else:
            actual_key = getattr(resp, key)  # resp.key
        expected_value = validator_mapping[key]
        assert actual_key == expected_value
    return True

def run_api_yaml(yml_file):
    load_json = load_yaml(yml_file)
    return run_api(load_json)

#运行testcase yaml 文件
def run_testcase(testcase_yml_file):
    load_api_list = load_yaml(testcase_yml_file)
    for apiinfo in load_api_list:
        run_api(apiinfo)
def run_yaml(yml_file):
    load_content = load_yaml(yml_file)
    result = []
    if is_api(load_content):
        success = run_api(load_content)
        result.append(success)
    elif is_testcase(load_content):
        for apiinfo in load_content:
            success = run_api(apiinfo)
            result.append(success)
    else:
        raise Exception("yaml file is bad:{}".format(yml_file))

    print("result:",result)
    return result


