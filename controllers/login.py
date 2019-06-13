from flask import (
    Blueprint,
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

login_bp = Blueprint("login", __name__, url_prefix="/api/v1/login")


@login_bp.route("", methods=["POST"])
@json_required
def login(json_dict):
    email = json_dict["email"]
    password = json_dict["password"]

    with get_session() as s:
        user = User.get_by_email(s, email)
        if not user:
            return failed(msg="邮箱或密码不对")

        user = User.login(s, email, password)
        if not user:
            return failed(msg="邮箱或密码不对")

        return succeed(msg="登录成功", data={"token": user.token})
