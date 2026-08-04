import pytest

from pages.InventoryPage import InventoryPage


# Same temporary helper as in test_cart.py — it belongs on InventoryPage later.
def add_item_to_cart(inventory_page: InventoryPage, item_id: str):
    inventory_page.page.locator(f"[data-test=\"add-to-cart-{item_id}\"]").click()


def test_checkout_happy_path(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")

    cart_page = inventory_page.open_cart()
    assert cart_page.get_item_count() == 1

    checkout_page = cart_page.start_checkout()
    checkout_page.fill_information("Solid", "Snake", "00001")

    assert checkout_page.get_title().text_content() == "Checkout: Overview"
    assert checkout_page.get_item_names() == ["Sauce Labs Backpack"]

    checkout_page.finish()

    assert checkout_page.get_complete_header().text_content() == "Thank you for your order!"


def test_checkout_chained(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-bike-light")

    checkout_page = inventory_page.open_cart().start_checkout()
    checkout_page.fill_information("Solid", "Snake", "00001").finish()

    assert checkout_page.get_complete_header().text_content() == "Thank you for your order!"


@pytest.mark.parametrize(
    "first_name, last_name, postal_code",
    [
        ("Solid", "Snake", "00001"),
        ("Ada", "Lovelace", "SW1A 1AA"),
        ("Grace", "Hopper", "12345"),
        ("Alan", "Turing", "M1 1AE"),
    ],
)
def test_checkout_with_different_customers(
    inventory_page: InventoryPage, first_name, last_name, postal_code
):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")

    checkout_page = inventory_page.open_cart().start_checkout()
    checkout_page.fill_information(first_name, last_name, postal_code).finish()

    assert checkout_page.get_complete_header().text_content() == "Thank you for your order!"


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, error",
    [
        ("", "Snake", "00001", "Error: First Name is required"),
        ("Solid", "", "00001", "Error: Last Name is required"),
        ("Solid", "Snake", "", "Error: Postal Code is required"),
    ],
)
def test_checkout_form_requires_all_fields(
    inventory_page: InventoryPage, first_name, last_name, postal_code, error
):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")

    checkout_page = inventory_page.open_cart().start_checkout()
    checkout_page.fill_information(first_name, last_name, postal_code)

    assert error in checkout_page.get_error_message().text_content()
    assert checkout_page.get_title().text_content() == "Checkout: Your Information"


def test_checkout_overview_subtotal(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")

    checkout_page = inventory_page.open_cart().start_checkout()
    checkout_page.fill_information("Solid", "Snake", "00001")

    assert checkout_page.get_subtotal() == 29.99
    assert checkout_page.get_total() > checkout_page.get_subtotal()


def test_back_home_after_order(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")

    checkout_page = inventory_page.open_cart().start_checkout()
    checkout_page.fill_information("Solid", "Snake", "00001").finish()

    inventory_page_again = checkout_page.back_home()

    assert inventory_page_again.get_title().text_content() == "Products"
