import pytest
from utils.config_reader import config
from pages.main_page import MainPage
from utils.enums import SortType
from utils.config_reader import ConfigReader

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

@pytest.fixture(params=[
    ("city", 10, SortType.PRICE_ASC, "Price: low to high"),
    ("city", 15, SortType.PRICE_DESC, "Price: high to low"),
    ("habits", 10, SortType.PRICE_ASC, "Price: low to high"),
    ("habits", 15, SortType.PRICE_DESC, "Price: high to low"),
])
def test_data(request):
    return request.param