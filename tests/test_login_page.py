from playwright.sync_api import Page
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage  

def test_login_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    # assert (login_page.get_login_credentials.all_text_contents()).to_contain_text("standard_user")
    assert "standard_user" in login_page.get_login_credential().inner_html()  # ← Fixed: singular
    assert "secret_sauce" in login_page.get_login_password().inner_html()

def test_login_successful(page: Page):
    
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login_standard_user()
    
    inventory_page = InventoryPage(page)  # ← Uncommented!
    assert inventory_page.get_title().text_content() == "Products"