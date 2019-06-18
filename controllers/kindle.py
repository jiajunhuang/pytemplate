from flask import (
    Blueprint,
    request,
)
from controllers.utils import (
    succeed,
)


mailgun_bp = Blueprint("mailgun", __name__, url_prefix="/mailgun")


@mailgun_bp.route("/kindle", methods=["POST"])
def kindle():
    print(request.data)
    return succeed()
