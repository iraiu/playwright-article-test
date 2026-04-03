import pytest
from utils.config_reader import ConfigReader
from pages.main_page import MainPage

config = ConfigReader()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": config.viewport,
    }

@pytest.fixture
def main_page(page):
    return MainPage(page)