# import time
#
# from behave import given, when, then
#
# from pageobjects.Login import LoginPageObjects
#
#
# @given('the Login page is open')
# def step_impl(context):
#     context.current_page = LoginPageObjects()
#     context.current_page.open()
#     time.sleep(2)
#
#
# @when('the user logs in with username and password')
# def step_impl(context):
#     context.current_page = LoginPageObjects()
#     context.current_page.input_field()
#     # time.sleep(5)
#
#
# @when('clicks button login')
# def step_impl(context):
#     context.current_page = LoginPageObjects()
#     context.current_page.click()
#     time.sleep(5)
#
#
# @then('the message "{message}" is shown')
# def step_impl(context, message):
#     assert message in context.current_page.get_message()
#     time.sleep(2)
#
#
# @then('the user clicks on the menu and click on logout')
# def step_impl(context):
#     context.current_page = LoginPageObjects()
#     context.current_page.menu_burger()
#     time.sleep(2)
#     context.current_page = context.current_page.logout_btn()
#
