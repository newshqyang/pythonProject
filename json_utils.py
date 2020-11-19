import json


# 成功json
def success():
    str = {
        'code': 1
    }
    r = json.dumps(str, ensure_ascii=False)
    return r


# 失败json
def failure(msg):
    str = {
        'code': 0,
        'message': msg
    }
    r = json.dumps(str, ensure_ascii=False)
    return r

