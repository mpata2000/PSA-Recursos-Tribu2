import json
import socket

import requests
from behave import *



@given('a running api')
def step_impl(context):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        assert s.connect_ex(('localhost', 8000)) == 0


@given('hours with "{user_id}","{task_id}","{hours}","{minutes}","{seconds}","{date}" and "{note}"')
def step_impl(context, user_id, task_id, hours, minutes, seconds, date, note):
    context.json_hours_1 = {
        "user_id": user_id,
        "task_id": task_id,
        "day": date,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "note": note
    }


@when("we request a create hours")
def step_impl(context):
    context.response = requests.post("http://127.0.0.1:8000/hours", json=context.json_hours_1)


@then("a hours is created correctly")
def step_impl(context):
    assert context.response.status_code == 201
    assert context.response.json() == context.json_hours_1


@step('it isnt created already with "{user_id}","{task_id}" and "{date}"')
def step_impl(context, user_id, task_id, date):
    params = {
        "user_id": "xd",
        "task_id": task_id,
        "day": date
    }

    context.response = requests.get("http://127.0.0.1:8000/hours", params=params)
    data = json.loads(context.response.text)

    if len(data) > 0:
        url = "http://127.0.0.1:8000/hours/" + data.id
        requests.delete(url)
