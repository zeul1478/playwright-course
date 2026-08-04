import pytest

from pages.InventoryPage import InventoryPage


# TEMPORARY HELPER
# Adding a product to the cart happens on the INVENTORY page, so really this
# belongs on InventoryPage as add_item_to_cart(item_id). Until that method
# exists, we keep it here in ONE place so there is only one line to move later.
def add_item_to_cart(inventory_page: InventoryPage, item_id: str):
    # item_id looks like "sauce-labs-backpack"
    inventory_page.page.locator(f"[data-test=\"add-to-cart-{item_id}\"]").click()


def test_cart_page_loads(inventory_page: InventoryPage):
    cart_page = inventory_page.open_cart()

    assert cart_page.get_title().text_content() == "Your Cart"
    assert cart_page.get_checkout_button().is_visible()


def test_added_item_appears_in_cart(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")
    cart_page = inventory_page.open_cart()

    assert cart_page.get_item_count() == 1
    assert cart_page.get_item_names() == ["Sauce Labs Backpack"]


@pytest.mark.parametrize(
    "item_id, item_name",
    [
        ("sauce-labs-backpack", "Sauce Labs Backpack"),
        ("sauce-labs-bike-light", "Sauce Labs Bike Light"),
        ("sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"),
        ("sauce-labs-onesie", "Sauce Labs Onesie"),
    ],
)
def test_each_product_can_be_added(inventory_page: InventoryPage, item_id, item_name):
    add_item_to_cart(inventory_page, item_id)
    cart_page = inventory_page.open_cart()

    assert cart_page.get_item_count() == 1
    assert item_name in cart_page.get_item_names()


def test_remove_one_item_from_cart(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")
    add_item_to_cart(inventory_page, "sauce-labs-bike-light")

    cart_page = inventory_page.open_cart()

    assert cart_page.get_item_count() == 2
    names = cart_page.get_item_names()
    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Bike Light" in names

    cart_page.remove_item("sauce-labs-backpack")

    assert cart_page.get_item_count() == 1
    assert cart_page.get_item_names() == ["Sauce Labs Bike Light"]


def test_remove_both_items_by_chaining(inventory_page: InventoryPage):
    add_item_to_cart(inventory_page, "sauce-labs-backpack")
    add_item_to_cart(inventory_page, "sauce-labs-bike-light")

    cart_page = inventory_page.open_cart()
    cart_page.remove_item("sauce-labs-backpack").remove_item("sauce-labs-bike-light")

    assert cart_page.get_item_count() == 0


def test_logout_from_cart(inventory_page: InventoryPage):
    cart_page = inventory_page.open_cart()
    login_page_again = cart_page.logout()

    assert login_page_again.get_login_credentials().is_visible()
