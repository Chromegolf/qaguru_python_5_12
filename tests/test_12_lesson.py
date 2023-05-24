from data.users import User, Gender, Subject, Hobby
from package.registration_page import RegistrationPage
from datetime import date
import allure

def test_student_registration_form():
    #GIVEN
    student = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivanov@gmail.com',
        phone='8800100300',
        gender=Gender.male.value,
        birthday=date(1990, 8, 1),
        subjects=[Subject.computer_science.value, Subject.english.value],
        hobbies=[Hobby.reading.value],
        upload_picture='test_picture.png',
        current_address='Russia, Moscow',
        state='Haryana',
        city='Karnal'
    )

    reg_page = RegistrationPage()

    with allure.step("Открываем страницу регистрации"):
        reg_page.open()

    #WHEN
    with allure.step("Заполняем данные студента"):
        reg_page.register(student)

    with allure.step("Сохраняем данные студента"):
        reg_page.submit()

    #THEN
    with allure.step("Проверяем соответствие заполненных данных переданным"):
        reg_page.should_registered_user(student)