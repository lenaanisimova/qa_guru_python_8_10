from resource import resources

from selene import browser, have, be, command

class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def choose_a_gender(self, gender):
        gender = f'//label[@for="gender-radio-2" and text()="{gender}"]'
        browser.element(gender).click()

    def fill_number_phone(self, value):
        browser.element("#userNumber").type(value)

    def choose_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def choose_subject(self, value):
        browser.element('#subjectsInput').type('History').press_enter()

    def choose_hobby_2(self, hobby):
        hobby = f'//label[@for="hobbies-checkbox-2" and text()="{hobby}"]'
        browser.element(hobby).should(be.clickable).click()

    def scroll_into_view(self):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)

    def download_picture(self, value):
        browser.element('#uploadPicture').should(be.visible).type(resources.path(value))
        return self

    def current_address(self, value):
        browser.element('#currentAddress').type(value)

    def choose_country(self, value):
        browser.element('#react-select-3-input').should(be.visible).type(value).press_enter()

    def choose_city(self, value):
        browser.element('#react-select-4-input').should(be.visible).type(value).press_enter()

    def submit_form(self):
        browser.element('#submit').execute_script('element.click()')

    def user_must_be_registered(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture,
                                country, city):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            full_name,
            email,
            gender,
            phone_number,
            date_of_birth,
            subject,
            hobby,
            picture,
            country,
            city
        ))


