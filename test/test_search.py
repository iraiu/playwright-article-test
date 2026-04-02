from utils.config_reader import config
from typing import List
from utils.config_reader import ConfigReader

config = ConfigReader()

def test_search_and_price_sorting(page, main_page, test_data):
    article_name, articles_count, filter_type, filter_display = test_data

    page.goto(config.base_url)

    search_results = main_page.search(article_name)
    search_results.apply_filter(filter_type.value)

    prices = search_results.get_all_prices(articles_count)

    is_sorted = _are_prices_sorted_correctly(filter_type, prices)
    assert is_sorted, f"Prices not sorted correctly for filter '{filter_display}': {prices}"
    assert len(prices) > 0, f"No prices found for '{article_name}'"


def _are_prices_sorted_correctly(filter_type, prices: List[float]) -> bool:
    from utils.enums import SortType

    if len(prices) < 2:
        return True

    if filter_type == SortType.PRICE_ASC:
        return all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))
    elif filter_type == SortType.PRICE_DESC:
        return all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1))

    return True