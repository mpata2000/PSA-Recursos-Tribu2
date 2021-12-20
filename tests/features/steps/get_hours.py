import json

import requests
from behave import *


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


@when('get hours is requested with "json"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When get hours is requested with "json"')
