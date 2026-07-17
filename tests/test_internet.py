from playwright.sync_api import Page, expect
import pytest

# Test Case 1: Click Action

def test_click_action(page: Page):
    add_element_button = page.get_by_role("button", name="Add Element")
    delete_button = page.get_by_role("button", name="Delete")
    # 1. Go to Page
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    # 2. Click on the Add Element button
    add_element_button.click()
    add_element_button.click()
    # 3. Click on the Delete button
    delete_button.first.click()
    # for b in delete_button.all():
    #    b.click()
    expect(delete_button).to_be_visible()
    assert delete_button.is_visible()


def test_fill_and_press(page: Page):
    # 1. Go to Page
    page.goto("https://the-internet.herokuapp.com/login")
    username_field = page.get_by_label("Username")
    password_field = page.get_by_label("Password")

    username_field.fill("tomsmith")
    username_field.press("Tab")
    password_field.fill("SuperSecretPassword!")
    password_field.press("Enter")

    #Store the text frpm the pahe as actuial restiult them compare against Expected Restult in assert statemen
    test = page.get_by_role("heading", name="Welcome to the Secure Area.").text_content()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."




def test_checkboxes(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    boxes = page.get_by_role("checkbox")

    boxes.first.check()
    boxes.last.uncheck()




def test_dropdown(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    dropdown = page.locator("#dropdown")

    dropdown.select_option("2")
    dropdown.select_option(label="Option 1")
    dropdown.select_option(index=2)
    

def test_hovers(page: Page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    images = page.locator(".figure").first
    images.hover()


def test_upload(page: Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    # locator of the input    path to the file
    page.locator("#file-upload").set_input_files("test_data/resume.txt")
    page.locator("#file-submit").click()
    

def test_drag_and_drop(page: Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    a = page.locator("#column-a")
    b = page.locator("#column-b")

    a.drag_to(b)
    b.drag_to(a)

   
def test_context_menu(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/context_menu")
    # assert page.on("dialog", lambda dialog: dialog.accept(), dialog.value)
    page.locator("#hot-spot").click(button="right")


@pytest.mark.parametrize(
    "link",
    [
        "random_data.txt",           
        "Sample.pdf"         
    ],
)
def test_download(page: Page, link: str) -> None:
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.get_by_role("link", name=link).click()
    download = download_info.value
    
    assert download.suggested_filename == link



def test_hidden_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")
    
    # 1. Wait for the modal to appear
    modal = page.locator("#modal")
    modal.wait_for(state="visible", timeout=5000)  # Wait up to 5 seconds
    
    # 2. Assert it's visible
    assert modal.is_visible()
    
    # 3. Click the close button (more specific locator)
    page.locator(".modal-footer").get_by_text("Close").click()
    
    # 4. Wait for the modal to disappear
    modal.wait_for(state="hidden")
    
    # 5. Assert it's gone
    assert not modal.is_visible()








    

    