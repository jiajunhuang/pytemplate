from flask import (
    Blueprint,
)

from controllers.validators import (
    HelloWorldSchema,
)
from controllers.utils import (
    succeed,
    binding_schemma,
)
from models import (
    get_session,
    HelloLog,
)

hello_bp = Blueprint("hello", __name__, url_prefix="/v1/hello")


@hello_bp.route("/")
@binding_schemma(HelloWorldSchema)
def hello(data):
    """hello world"""
    with get_session() as s:
        s.add(HelloLog(name=data["name"]))
        s.commit()

        return succeed()
