import pytest
from utils.config_reader import ConfigReader
from utils.enums import SortType

config = ConfigReader()


@pytest.mark.parametrize("article_name", ["city", "habits"])
@pytest.mark.parametrize("articles_count", [10, 15])
@pytest.mark.parametrize("filter_type",
                         [SortType.PRICE_ASC, SortType.PRICE_DESC])
def test_search_and_price_sorting(page, main_page, article_name,
                                  articles_count, filter_type):
    filter_display = "Price: low to high" if filter_type == SortType.PRICE_ASC else "Price: high to low"

    page.goto(config.base_url)
    search_results = main_page.search(article_name)
    search_results.apply_filter(filter_type)

    prices = search_results.get_all_prices(articles_count)

    is_sorted = _are_prices_sorted_correctly(filter_type, prices)
    assert is_sorted, f"Prices not sorted correctly for filter '{filter_display}': {prices}"
    assert len(prices) > 0, f"No prices found for '{article_name}'"


def _are_prices_sorted_correctly(filter_type: SortType,
                                 prices: list[float]) -> bool:
    if len(prices) < 2:
        return True

    if filter_type == SortType.PRICE_ASC:
        return prices == sorted(prices)
    elif filter_type == SortType.PRICE_DESC:
        return prices == sorted(prices, reverse=True)

    return True