from playwright.sync_api import Page
from utils.config_reader import config


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = config.base_url

    def navigate(self, url="/"):
        full_url = f"{self.base_url}{url}" if url.startswith("/") else url
        self.page.goto(full_url)

    def get_title(self):
        return self.page.title()

    def wait_for_element(self, selector, timeout=30000):
        self.page.wait_for_selector(selector, timeout=timeout)