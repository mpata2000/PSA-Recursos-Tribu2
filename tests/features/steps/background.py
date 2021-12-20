import json
import random
import socket
import string
from datetime import datetime

import requests
from behave import *


@given('a running api')
def step_impl(context):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        assert s.connect_ex(('localhost', 8000)) == 0


@given("an existing hours url id")
def step_impl(context):
    response = requests.get("http://127.0.0.1:8000/hours")

    data = json.loads(response.text)

    if data["count"] < 1:
        test = "test_id:" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

        hour = {
            "user_id": test,
            "task_id": test,
            "day": datetime.now().strftime("%Y-%m-%d"),
            "hours": random.randint(0, 23),
            "minutes": random.randint(0, 23),
            "seconds": random.randint(0, 23),
            "note": test
        }

        response = requests.post("http://127.0.0.1:8000/hours", json=hour)
        context.json = json.loads(response.text)
    else:
        context.json = data["hours"][0]

    context.url = "http://127.0.0.1:8000/hours/" + context.json["id"]

@given("a random hours url id")
def step_impl(context):
    context.id = "xd"
    context.url = "http://127.0.0.1:8000/hours/" + context.id

@then("not found error is returned")
def step_impl(context):
    assert context.response.status_code == 404


@step("id doest return hours")
def step_impl(context):
    params = {
        "ids": context.id
    }

    context.response = requests.get("http://127.0.0.1:8000/hours", params=params)
    assert context.response.status_code == 200
    data = json.loads(context.response.text)
    assert data["count"] == 0
