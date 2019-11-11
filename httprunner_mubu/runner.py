import requests
import jsonpath

from httprunner_mubu.load import load_yaml
def extact_json_field(resp,json_field):
    value =jsonpath.jsonpath(resp.json(),json_field)
    return value[0]
def run_yaml(yml_file):
    load_json = load_yaml(yml_file)
    request = load_json["request"]

    method =request.pop("method")
    url =request.pop("url")
    resp =requests.request(method,url,**request)

    validator_mapping =load_json["validate"]

    for key in validator_mapping:
        if "$" in key:
            actual_key = extact_json_field(resp,key)
        else:
            actual_key = getattr(resp,key) #resp.key
        expected_value = validator_mapping[key]
        assert actual_key == expected_value

    return True

