
from playwright.sync_api import Page
import pytest


def test_practice_form(page: Page):
   
    page.goto("https://demoqa.com/automation-practice-form")
    first_name_field = page.get_by_role("textbox", name="First Name")
    last_name_field = page.get_by_role("textbox", name="Last Name")
    email_field =  page.get_by_role("textbox", name="name@example.com")
    gender_check_box = page.get_by_text("MaleFemaleOther")
    date_of_birth = page.locator("#dateOfBirthInput")
    subjects_field = page.locator("#subjectsContainer div")
    mobile_field = page.locator("#userNumber")
    check_box_reading = page.get_by_text("Reading")
    check_box_music =  page.get_by_text("Music")
    check_box_sports =  page.get_by_text("Sports")
    subjects_input = page.locator("#subjectsInput")
    picture_input = page.locator("#uploadPicture")
    address_field = page.locator("#currentAddress")
    state_dropdown = page.locator("#state svg")
    city_dropdown = page.locator("#city svg")
    submit_button = page.locator("#submit")
    modal_title = page.get_by_text("Thanks for submitting the form")

    
    first_name_field.fill("Mihai")
    first_name_field.press("Tab")
    last_name_field.fill("Buzila")
    last_name_field.press("Tab")
    email_field.fill("mihaibuzila1478@gmail.com")
    gender_check_box.page.get_by_role("radio", name="Male", exact=True).check()
    mobile_field.fill("3027276099")
    date_of_birth.fill("10 Sep 1996")
    subjects_field.nth(3).click()
    subjects_input.fill("m")
    page.get_by_role("option", name="Maths").click()
    subjects_input.fill("c")
    page.get_by_role("option", name="Computer Science").click()
    check_box_reading.click()
    check_box_music.click()
    check_box_sports.click()
    assert check_box_reading.is_checked()
    assert check_box_music.is_checked()
    assert check_box_sports.is_checked()
    picture_input.set_input_files("Tests/test_data/Screenshot 2026-07-09 at 9.49.27 PM.png")
    address_field.fill("1300 SE FL")
    state_dropdown.click()
    page.get_by_role("option", name="Haryana").click()
    city_dropdown.click()
    page.get_by_role("option", name="Karnal").click()
    submit_button.click()
    assert modal_title.is_visible()
    assert page.get_by_text("Mihai Buzila").is_visible()

    

    
    
    
    
    



    
   
    