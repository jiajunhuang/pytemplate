from flask import (
    Blueprint,
    render_template,
)
from lxml import html

from models import (
    get_session,
    Kindle,
)


kindle_bp = Blueprint("kindle", __name__, url_prefix="/kindle")


def html_to_text(s):
    etree = html.fromstring(s)

    for i in etree.find_class("noteText"):
        yield i.text


@kindle_bp.route("/<email>")
def get_by_email(email):
    with get_session() as s:
        item = Kindle.get_by_email(s, email)
        return render_template("kindle.html", items=html_to_text(item.content) if item else [])
