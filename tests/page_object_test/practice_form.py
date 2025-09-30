import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.page_object_test.student_registration_form import StudentRegistrationPage
from tests.page_object_test.submitting_form import StudentSubmittingForm


def create_driver_with_page_load_strategy():
    options = Options()
    options.page_load_strategy = 'eager'
    return webdriver.Chrome(options=options)


@pytest.fixture
def student_data():
    return {
        "first_name": "Sergey",
        "last_name": "Ermolaev",
        "email": "Ermolaev@mail.ru",
        "gender": "Male",
        "phone": "8934999000"
    }


def test_successful_completion_of_form(student_data):
    student_registration_form = StudentRegistrationPage()
    submitting_from = StudentSubmittingForm()
    browser.config.driver = create_driver_with_page_load_strategy()

    (
        student_registration_form
        .open_form('https://demoqa.com/automation-practice-form')
        .set_first_name(student_data['first_name'])
        .set_last_name(student_data['last_name'])
        .set_email(student_data['email'])
        .choose_gender(student_data['gender'])
        .set_phone_number(student_data['phone'])
        .set_date_of_birth(6, 1999, 10)
        .set_subjects('History')
        .choose_hobbies('Reading')
        .upload_file('pin.png')
        .set_address('Rus')
        .select_country('NCR')
        .select_city('Noida')
        .click_submit()

    )

    (
        submitting_from
        .check_heading_form("Thanks for submitting the form")
        .check_content_form("Sergey Ermolaev")
        .check_content_form("Ermolaev@mail.ru")
        .check_content_form("Male")
        .check_content_form("8934999000")
        .check_content_form("10 July,1999")
        .check_content_form("History")
        .check_content_form("Reading")
        .check_content_form("pin.png")
        .check_content_form("Rus")
        .check_content_form("NCR Noida")
    )
