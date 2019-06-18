from flask import (
    Blueprint,
    render_template,
)

from models import (
    get_session,
    Kindle,
)


kindle_bp = Blueprint("kindle", __name__, url_prefix="/kindle")


@kindle_bp.route("/<email>")
def get_by_email(email):
    with get_session() as s:
        item = Kindle.get_by_email(s, email)
        return render_template("kindle.html", item=item)
