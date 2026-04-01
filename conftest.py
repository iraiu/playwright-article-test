import pytest
from utils.config_reader import config

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": config.viewport,
    }
