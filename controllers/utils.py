import functools

from flask import (
    request,
    jsonify,
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


def binding_schemma(schema):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            # 获取参数
            arguments = request.get_json() or request.form or request.args
            if not arguments:
                return failed(msg="请检查参数")

            # 校验
            data = schema().load(arguments)
            if data.errors:
                return failed(msg="{}".format(data.errors))

            # 执行函数
            return func(data.data, *args, **kwargs)

        return inner
    return wrapper
