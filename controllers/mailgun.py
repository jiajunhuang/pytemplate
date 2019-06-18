import logging

from flask import (
    Blueprint,
    request,
)
from controllers.utils import (
    succeed,
)
from models import (
    get_session,
    Kindle,
)


mailgun_bp = Blueprint("mailgun", __name__, url_prefix="/mailgun")


@mailgun_bp.route("/kindle", methods=["POST"])
def kindle():
    sender = request.form["sender"]
    subject = request.form["subject"]
    recipient = request.form["recipient"]
    attachment = request.files["attachment-1"]
    logging.info("sender: {}, recipient: {}, subject: {}, files: {}".format(sender, recipient, subject, attachment))

    with get_session() as s:
        item = Kindle(sender=sender, content=attachment.read())
        s.add(item)
        s.commit()

        return succeed()
