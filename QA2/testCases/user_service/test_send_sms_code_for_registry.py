import json
import pytest_check as ck
from jsonschema import validators


def test_send_sms_code_for_registry(case_data, api):
    data = case_data
    res = api.api_function(data[0], data[1], data[2], **data[3])
    result = json.loads(res)
    print(res)
    print(type(result))
    ck.equal(result["code"], "200")
    ck.equal(result["message"], "成功!")

    schema = {
        "type": "object",
        "properties": {
            "code": {"type": "string"},
            "data": {"type": "integer", "minimum": 0},
            "message": {"type": "string"}
        },
        "required": ["code", "data"]
    }
    va = validators.Draft4Validator(schema)
    va.validate(result)