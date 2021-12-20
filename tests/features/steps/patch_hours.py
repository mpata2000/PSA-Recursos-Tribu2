import json

import requests
from behave import *


@when("patch is requested")
def step_impl(context):
    context.response = requests.patch(context.url, json=context.json_patch)


@step('a patch body with "{json_patch}"')
def step_impl(context, json_patch):
    context.json_patch = json.loads(json_patch)


