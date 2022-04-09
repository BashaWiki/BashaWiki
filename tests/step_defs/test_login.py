from pytest_bdd import scenario, given, when, then, parsers, scenarios

# @scenario('features\login.feature', 'To verify the user login')
# def test_to_verify_the_user_login():
#     pass
scenarios('../tests/features/')


@given(parsers.parse('The user launched the "{pagename}"'))
def the_user_launched_the_home_page(browser, pagename):
    if pagename == "Google":
        browser.get("https://www.google.com")
    else:
        browser.get("https://www.facebook.com")



@given('user validates Home page is launched')
def user_validates_home_page_is_launched():
    print("Getting Started")


@when('user click on login button')
def user_click_on_login_button():
    """user click on login button."""
    pass


@when('user enters "Password" in password')
def user_enters_password_in_password():
    pass


@when('user enters "Username" in Username')
def user_enters_username_in_username():
    pass


@then('user should be logged into the page')
def user_should_be_logged_into_the_page():
    pass
