#+

from model.page.registration_page import RegistrationPage
from model.user import User
import allure
from allure_commons.types import Severity

registration_page = RegistrationPage()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Регистрация пользователя")
def test_registration_form():
    user = User(first_name='Elena',
                last_name='Anisimova',
                email='test@mail.ru',
                gender='Female',
                phone_number='9123456789',
                month_of_birth='October',
                year_of_birth='1990',
                day_of_birth='20',
                subject='History',
                hobby='Reading',
                picture='iris.jpeg',
                current_address='Volgograd',
                country='NCR',
                city='Noida')

    registration_page.open()
    registration_page.register(user)
    registration_page.user_must_be_registered(user)
