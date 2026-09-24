from seleniumpagefactory.Pagefactory import PageFactory


class BasePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.timeout = 10

    def open_url(self, url: str):
        self.driver.get(url)