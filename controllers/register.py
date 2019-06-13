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

register_bp = Blueprint("register", __name__, url_prefix="/api/v1/register")


@register_bp.route("", methods=["POST"])
@json_required
def register(json_dict):
    email = json_dict["email"]
    password = json_dict["password"]

    with get_session() as s:
        user = User.get_by_email(s, email)
        if user:
            return failed(msg="用户已经存在")

        user = User.register(s, email, email, password)
        return succeed(msg="注册成功，请认证")
