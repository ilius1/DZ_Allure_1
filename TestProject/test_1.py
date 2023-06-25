import pytest
import allure
from selenium.webdriver import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'


@pytest.mark.usefixtures('setup')
class Test:

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store1(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select/option[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            element1 = self.browser.find_element(By.XPATH,
                                                 '/html/body/div/div/div[2]/div/form/div/select/option[2]').is_enabled()
        assert element1 == True

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store2(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store3(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store4(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
            element4 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert element4 == "Hermoine Granger", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store5(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').click()
            element5 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element5 == "Harry Potter", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store6(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').click()
            element6 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element6 == "Ron Weasly", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store7(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').click()
            element7 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element7 == "Albus Dumbledore", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store8(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').click()
            element8 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element8 == "Neville Longbottom", "Ошибка!!!!"

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store9(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
            element9 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert element9 == "Hermoine Granger", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store10(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').click()
            element10 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element10 == "Harry Potter", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store11(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').click()
            element11 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element11 == "Ron Weasly", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store12(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').click()
            element12 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element12 == "Albus Dumbledore", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, ' /html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store13(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').click()
            element13 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        assert element13 == "Neville Longbottom", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store14(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
            element14 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert element14 == "Hermoine Granger", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест банка')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store15(self):
        with allure.step('Открывает ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').click()
            element15 = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').text
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert element15 == "Hermoine Granger", "Ошибка!!!!"
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
