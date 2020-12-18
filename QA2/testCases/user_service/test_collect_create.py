import json
import pytest_check as ck
from jsonschema import validators


def test_collect_create(case_data, api, db):
    data = case_data
    res = api.api_function(data[0], data[1], data[2], **data[3])
    print(res)
    result = json.loads(res)
    try:
        ck.equal(result["code"], "200")
        ck.equal(result["data"], True)
        ck.equal(result["message"], "成功!")

    except Exception as err:
        print(err)

    schema = {
        "type": "object",
        "properties": {
            "code": {"type": "string"},
            "data": {"type": "boolean"},
            "message": {"type": "string"}
        },
        "required": ["code", "data"]
    }
    va = validators.Draft4Validator(schema)
    va.validate(result)

