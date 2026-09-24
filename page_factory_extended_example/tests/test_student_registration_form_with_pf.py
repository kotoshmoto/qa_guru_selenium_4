import pytest

from page_factory_extended_example.pages.automation_practice_form_page import AutomationPracticeFormPage


@pytest.fixture
def upload_file(tmp_path):
    file_path = tmp_path / "demo_upload.txt"
    file_path.write_text("QA Guru PageFactory Demo File Content", encoding="utf-8")

    return file_path


@pytest.mark.parametrize(
    "first_name,last_name,email,gender,mobile",
    [
        ("Ivan", "Ivanov", "ivanov@university.edu", "Male", "1234567890"),
        ("Anna", "Petrova", "petrova@university.edu", "Female", "9876543210")
    ]
)
def test_student_registration_form(driver, upload_file, first_name, last_name, email, gender, mobile):
    page = AutomationPracticeFormPage(driver)
    page.open_url("https://qa-guru.github.io/one-page-form/automation-practice-form.html")

    page.fill_form(first_name=first_name, last_name=last_name, email=email, gender=gender, mobile=mobile, year="2000",
                   month="January", day="15", subjects=["Maths", "Computer Science"], hobbies=["Sports", "Music"],
                   file_path=str(upload_file), address="123 University Avenue, Tomsk, Russia", state="NCR",
                   city="Delhi")

    page.submit_form()

    actual_results = page.get_modal_results()

    expected_results = {
        "Student Name": f"{first_name} {last_name}",
        "Student Email": email,
        "Gender": gender,
        "Mobile": mobile,
        "Date of Birth": "15 Jan 2000",
        "Subjects": "Maths, Computer Science",
        "Hobbies": "Sports, Music",
        "Picture": upload_file.name,
        "Address": "123 University Avenue, Tomsk, Russia",
        "State and City": "NCR Delhi"
    }

    assert actual_results == expected_results
