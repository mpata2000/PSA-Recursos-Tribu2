import json
import requests
from behave import *

from tests.features.steps.background import create_random_hour


@when("get hours is requested")
def step_impl(context):
    context.response = requests.get("http://127.0.0.1:8000/hours")


@then("All existing hours are returned")
def step_impl(context):
    assert context.response.status_code == 200
    data = json.loads(context.response.text)
    assert len(data['hours']) >= 0
    assert data['count'] >= 0
    assert data['count'] == len(data['hours'])


@step('get hours is requested with "{json_get}"')
def step_impl(context, json_get):
    params = json.loads(json_get)
    context.response = requests.get("http://127.0.0.1:8000/hours", params=params)


@given("a created hour")
def step_impl(context):
    hour = create_random_hour()
    response = requests.post("http://127.0.0.1:8000/hours", json=hour)
    context.json = json.loads(response.text)


@then("only one existing hour is return")
def step_impl(context):
    assert context.response.status_code == 200
    data = json.loads(context.response.text)
    assert data['count'] == 1


@when("get hours is requested with id")
def step_impl(context):
    data = {
        "ids": context.json["id"]
    }
    context.response = requests.get("http://127.0.0.1:8000/hours")


@then("get is succesful and empty")
def step_impl(context):
    assert context.response.status_code == 200
    data = json.loads(context.response.text)
    assert data['count'] == 0


@when("get hours is requested with created data")
def step_impl(context):
    data = {
        "ids": context.json["id"],
        "user_id": context.json["user_id"],
        "task_id": context.json["task_id"],
        "day": context.json["day"]
    }
    context.response = requests.get("http://127.0.0.1:8000/hours", params=data)
