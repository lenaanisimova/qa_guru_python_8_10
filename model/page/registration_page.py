from model import resources

from selene import browser, have, be, command
from allure import step

class RegistrationPage:
    @step('Открыть страницу сайта')
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    @step('Зарегистрировать пользователя')
    def register(self, user):
        #Имя, фамилия, электронная почта, пол и номер телефона
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('label[for="gender-radio-2"]').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').type(user.phone_number)
        # Дата рождения
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__month-select').type(user.month_of_birth)
        browser.element('.react-datepicker__year-select').type(user.year_of_birth)
        browser.element(f'.react-datepicker__day--0{user.day_of_birth}:not(.react-datepicker__day--outside-month)'). \
            click()
        # Предмет и хобби
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        if 'Sports' in user.hobby:
            browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
        if 'Reading' in user.hobby:
            browser.element('label[for=hobbies-checkbox-2]').should(be.visible).click()
        if 'Music' in user.hobby:
            browser.element('label[for=hobbies-checkbox-3]').should(be.visible).click()
        # Картинка
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').should(be.visible).type(resources.path(user.picture))
        # Адрес
        browser.element('#currentAddress').type(user.current_address)
        browser.element('#react-select-3-input').should(be.visible).type(user.country).press_enter()
        browser.element('#react-select-4-input').should(be.visible).type(user.city).press_enter()
        # Создание анкеты
        browser.element('#submit').execute_script('element.click()')


    @step('Проверить, что пользовательские данные сохранены корректно')
    def user_must_be_registered(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobby,
            user.picture,
            user.current_address,
            f'{user.country} {user.city}'
        ))


