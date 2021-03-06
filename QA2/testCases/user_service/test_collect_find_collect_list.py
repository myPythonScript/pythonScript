import json
import pytest_check as ck
from jsonschema import validators


def test_collect_find_collect_list(case_data, api):
    data = case_data
    res = api.api_function(data[0], data[1], data[2], **data[3])
    print(res)
    result = json.loads(res)
    ck.equal(result["code"], "200")
    # ck.equal(result["data"], True)
    ck.equal(result["message"], "成功!")

    schema = {
        "type": "object",
        "properties": {
            "code": {"type": "string"},
            "data": {"type": "array",
                     "items": {
                         "properties": {
                             "contentCount": {
                                 "type": "integer",
                                 "minimum": 0
                             },
                             "id": {"type": "string"},
                             "name": {"type": "string"},
                             "time": {"type": "integer"}
                         }
                     },
                     "message": {"type": "string"}
                     },
            "required": ["code", "data"]
        }
    }
    va = validators.Draft4Validator(schema)
    va.validate(result)