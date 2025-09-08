from tortoise.models import Model
from tortoise import fields


class RequestLog(Model):
    id = fields.IntField(pk=True)  # unique id for each log entry
    operation = fields.CharField(
        max_length=50
    )  # which operation was called (eg "pow", "fib", "fact")
    input_data = fields.JSONField()  # JSON input received, stored as a string
    result = fields.CharField(max_length=50)  # output returned
    duration_ms = fields.FloatField()  # durr of request
    timestamp = fields.DatetimeField(
        auto_now_add=True
    )  # autofilled current at entry creation
