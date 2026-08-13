import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        pytest.param("problem_user", "secret_sauce", marks=pytest.mark.xfail(reason="problem_user is expected to fail at checkout")),
        ("performance_glitch_user", "secret_sauce"),
    ]
)
def test_checkout_happy_path(page: Page, username: str, password: str) -> None:
    page.goto("/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    
    expect(page.locator("[data-test=\"secondary-header\"]")).to_be_visible()
    
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    
    page.locator("[data-test=\"firstName\"]").fill(username)
    page.locator("[data-test=\"lastName\"]").fill(username)
    page.locator("[data-test=\"postalCode\"]").fill("33301")
    page.locator("[data-test=\"continue\"]").click()
    
    # This will fail for problem_user (expected)
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"complete-header\"]")).to_have_text("Thank you for your order!")


def test_locked_out_user(page: Page) -> None:
    page.goto("/")
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    error_banner = page.locator("[data-test=\"error\"]")
    expect(error_banner).to_be_visible()
    expect(error_banner).to_have_text("Epic sadface: Sorry, this user has been locked out.")