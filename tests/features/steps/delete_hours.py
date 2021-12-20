import json
import socket

import requests
from behave import *


@when("delete is requested")
def step_impl(context):
    context.response = requests.delete(context.url)


@then("hours are deleted")
def step_impl(context):
    assert context.response.status_code == 202
    data = json.loads(context.response.text)
    assert data["user_id"] == context.json["user_id"]
    assert data["task_id"] == context.json["task_id"]
    assert data["day"] == context.json["day"]


