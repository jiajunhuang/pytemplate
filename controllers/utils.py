import functools

from flask import (
    jsonify,
    request,
)


def response(code, msg, data):
    r = {
        "code": code,  # 业务code
        "msg": msg,  # 提示消息
        "data": data or {},
    }
    return jsonify(r)


def succeed(code=200, msg="", data=None):
    return response(code, msg, data)


def failed(code=400, msg="", data=None):
    return response(code, msg, data)


def json_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        json_dict = request.get_json()
        if not json_dict:
            return failed()

        return func(json_dict, *args, **kwargs)
    return wrapper
