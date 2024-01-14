
from model.page.registration_page import RegistrationPage

import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Регистрация пользователя")

def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Elena')
    registration_page.fill_last_name('Anisimova')
    registration_page.fill_email('test@gmail.com')
    registration_page.choose_a_gender('Female')
    registration_page.fill_number_phone('9123456789')
    registration_page.choose_date_of_birth(month='October', year=1990, day=20)
    registration_page.choose_subject('History')
    registration_page.choose_hobby_2('Reading')
    registration_page.scroll_into_view()
    registration_page.download_picture('iris.jpeg')
    registration_page.current_address('Volgograd')
    registration_page.choose_country('NCR')
    registration_page.choose_city('Noida')
    registration_page.submit_form()

    registration_page.user_must_be_registered(
        'Elena Anisimova',
        'test@gmail.com',
        'Female',
        '9123456789',
        '20 October,1990',
        'History',
        'Reading',
        'iris.jpeg',
        'Volgograd',
        'NCR Noida')
