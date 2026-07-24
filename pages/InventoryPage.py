from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        #Locators
        self.title = page.locator("[data-test=\"title\"]")



    def get_title(self):
        return self.title
