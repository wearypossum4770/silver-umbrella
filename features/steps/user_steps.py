from behave import given, step, then, when


@given("user object")
def step_impl(context):
    ...


@when("user accesses profile")
def step_impl(context):
    ...


@then("user can view profile.")
def step_impl(context):
    ...
