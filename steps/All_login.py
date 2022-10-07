import time

from behave import given, when, then

from pageobjects.Login import LoginPageObjects


@given('the Login page is open')
def step_impl(context):
    context.current_page = LoginPageObjects()
    context.current_page.open()
    time.sleep(2)


@when('the user logs in with "{username}" username and "{password}" password')
def step_impl(context, username, password):
    context.current_page = LoginPageObjects()
    user = {'username': username, 'password': password}
    context.current_page.login_input(user)
    # time.sleep(5)


@when('clicks button login')
def step_impl(context):
    context.current_page = LoginPageObjects()
    context.current_page.click()
    time.sleep(5)


@then('the message "{message}" is shown')
def step_impl(context, message):
    context.current_page = LoginPageObjects()
    assert message in context.current_page.find_message()
    time.sleep(5)
