from pages.InventoryPage import InventoryPage


class LoginPage:
    # __init__
    def __init__(self, page: Page) -> None:
        # Locators
        self.page = page
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.login_credential = page.locator("[data-test=\"login-credentials\"]")
        self.login_password = page.locator("[data-test=\"login-password\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    # Methods
    def open(self):
        self.page.goto("/")

    def login_standard_user(self):
        self.username.fill("standard_user")
        self.password.fill("secret_sauce")
        self.login_button.click()  
        return InventoryPage(self.page)

    def login_user(self, username: str, password: str):  
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()  
        return InventoryPage(self.page)

    # Getters
    def get_login_credential(self):
        return self.login_credential
    
    def get_login_password(self):
        return self.login_password
    
    def get_error_message(self):
        return self.error_message