from marshmallow import (
    Schema,
    fields,
)


class HelloWorldSchema(Schema):
    name = fields.Str(required=True)
