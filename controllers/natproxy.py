from flask import (
    Blueprint,
    request,
)

from controllers.utils import (
    json_required,
    succeed,
    failed,
)
from models import (
    get_session,
    User,
)

natproxy_bp = Blueprint("natproxy", __name__, url_prefix="/api/v1/natproxy")


@natproxy_bp.route("/check_token")
def check_token():
    with get_session() as s:
        token = request.args.get("token")
        if not token:
            return failed(msg="需要一个token")

        user = User.get_by_token(s, token)
        if not user:
            return failed(msg="token无效")

        return succeed(msg="找到用户", data={"addr": user.addr or ""})


@natproxy_bp.route("/addr")
def check_addr():
    addr = request.args.get("addr")
    if not addr:
        return failed(msg="需要addr")

    with get_session() as s:
        user = User.get_by_addr(s, addr)
        if not user:
            return failed(code=404, msg="无此addr")

        return succeed(msg="此addr已经存在")


@natproxy_bp.route("/addr", methods=["POST"])
@json_required
def natproxy(json_dict):
    token = json_dict["token"]
    addr = json_dict["addr"]

    with get_session() as s:
        user = User.get_by_token(s, token)
        if not user:
            return failed(msg="token无效")

        user.addr = addr
        s.add(user)
        s.commit()

        return succeed(msg="成功更新用户分配的公网地址")
