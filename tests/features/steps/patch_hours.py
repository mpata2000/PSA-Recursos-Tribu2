import json

import requests
from behave import *


@when("patch is requested")
def step_impl(context):
    context.response = requests.patch(context.url, json=context.json_patch)


@step('a patch body with "{json_patch}"')
def step_impl(context, json_patch):
    context.json_patch = json.loads(json_patch)


@then("hours is updated")
def step_impl(context):
    assert context.response.status_code == 202
    data = json.loads(context.response.text)

    for key in context.json_patch.keys():
        assert data[key] == context.json_patch[key]
