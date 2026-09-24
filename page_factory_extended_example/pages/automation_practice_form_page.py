from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from page_factory_extended_example.pages.base_page import BasePage


class AutomationPracticeFormPage(BasePage):
    locators = {
        "first_name": ("ID", "firstName"),
        "last_name": ("ID", "lastName"),
        "user_email": ("ID", "userEmail"),
        "banner_button": ("XPATH", "//div[@id='fixedban']//button[@aria-label='Close']"),
        "gender_male": ("XPATH", "//label[@for='gender-radio-1']"),
        "gender_female": ("XPATH", "//label[@for='gender-radio-2']"),
        "gender_other": ("XPATH", "//label[@for='gender-radio-3']"),
        "user_number": ("ID", "userNumber"),
        "date_of_birth_input": ("ID", "dateOfBirthInput"),
        "calendar_month_select": ("CLASS_NAME", "react-datepicker__month-select"),
        "calendar_year_select": ("CLASS_NAME", "react-datepicker__year-select"),
        "calendar_target_day": ("XPATH", "//span[contains(@class, 'react-datepicker__day') and @data-day='{day}']"),
        "subjects_input": ("ID", "subjectsInput"),
        "hobby_sports": ("XPATH", "//label[@for='hobbies-checkbox-1']"),
        "hobby_reading": ("XPATH", "//label[@for='hobbies-checkbox-2']"),
        "hobby_music": ("XPATH", "//label[@for='hobbies-checkbox-3']"),
        "upload_picture_btn": ("ID", "uploadPicture"),
        "current_address": ("ID", "currentAddress"),
        "state_dropdown": ("ID", "state"),
        "city_dropdown": ("ID", "city"),
        "state_city_option": ("XPATH", "//div[@id='stateCity-wrapper']//div[contains(@class, 'state-city-option')"
                                       " and normalize-space()='{value}']"),
        "submit_button": ("ID", "submit"),
        "modal_title": ("ID", "example-modal-sizes-title-lg"),
        "modal_table_rows": ("XPATH", "//tbody[@id='resultBody']/tr")
    }

    def _close_commercial_banner(self):
        self.banner_button.click_button()

    def fill_personal_info(self, first_name: str, last_name: str, email: str, gender: str, mobile: str):
        self._close_commercial_banner()
        self.first_name.set_text(first_name)
        self.last_name.set_text(last_name)
        self.user_email.set_text(email)

        gender_map = {
            "male": self.gender_male,
            "female": self.gender_female,
            "other": self.gender_other
        }

        gender_map[gender.lower()].click_button()
        self.user_number.set_text(mobile)

    def select_date_of_birth(self, year: str, month: str, day: str):
        self.date_of_birth_input.click_button()
        self.calendar_year_select.select_element_by_value(year)
        self.calendar_month_select.select_element_by_text(month)

        xpath = self.locators["calendar_target_day"][1].format(day=day)
        day_element = WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        day_element.click()

    def enter_subjects(self, subjects: list[str]):
        for subject in subjects:
            self.subjects_input.set_text(subject)
            self.subjects_input.send_keys(Keys.ENTER)

    def select_hobbies(self, hobbies: list[str]):
        hobbies_map = {
            "sports": self.hobby_sports,
            "reading": self.hobby_reading,
            "music": self.hobby_music
        }

        for hobby in hobbies:
            hobbies_map[hobby.lower()].click_button()

    def upload_file(self, file_path: str):
        self.upload_picture_btn.send_keys(file_path)

    def fill_address_and_location(self, address: str, state: str, city: str):
        self.current_address.set_text(address)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.state_dropdown)

        self.state_dropdown.click_button()
        self._select_state_city_option(state)

        self.city_dropdown.click_button()
        self._select_state_city_option(city)

    def _select_state_city_option(self, value: str):
        xpath = self.locators["state_city_option"][1].format(value=value)
        option = WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        option.click()

    def fill_form(self, first_name: str, last_name: str, email: str, gender: str, mobile: str, year: str, month: str,
                  day: str, subjects: list[str], hobbies: list[str], file_path: str, address: str, state: str,
                  city: str):
        self.fill_personal_info(first_name=first_name, last_name=last_name, email=email, gender=gender, mobile=mobile)
        self.select_date_of_birth(year=year, month=month, day=day)
        self.enter_subjects(subjects)
        self.select_hobbies(hobbies)
        self.upload_file(file_path)
        self.fill_address_and_location(address=address, state=state, city=city)

    def submit_form(self):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.submit_button)
        self.submit_button.click_button()

    def get_modal_results(self) -> dict[str, str]:
        self.modal_title.visibility_of_element_located()

        result = {}
        xpath = self.locators["modal_table_rows"][1]
        rows = self.driver.find_elements(By.XPATH, xpath)

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")

            if len(cells) == 2:
                label = cells[0].text.strip()
                value = cells[1].text.strip()
                result[label] = value

        return result
