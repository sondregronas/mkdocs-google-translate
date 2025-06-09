import pytest

from mkdocs_google_translate import GoogleTranslatePlugin

base_extra = {
    "alternate": [
        {"name": "English", "link": "%GT_RELATIVE_URL%", "lang": "en"},
        {
            "name": "Norsk",
            "link": "https://translate.goog/?_x_tr_sl=en&_x_tr_tl=no",
            "lang": "no",
        },
        {
            "name": "test",
            "link": "https://translate.goog/?_x_tr_sl=en&_x_tr_tl=test",
            "lang": "test",
        },
    ]
}


@pytest.fixture
def plugin():
    plugin = GoogleTranslatePlugin()
    plugin.load_config(options={"site_url": "example.com", "extra": base_extra})
    plugin.on_config(plugin.config)
    return plugin


@pytest.fixture
def plugin_location():
    plugin = GoogleTranslatePlugin()
    plugin.load_config(
        options={"site_url": "https://example.com/subpath", "extra": base_extra}
    )
    plugin.on_config(plugin.config)
    return plugin


html = """
<li class="md-select__item">
  <a href="%GT_RELATIVE_URL%">
    English
  </a>
</li>
<li class="md-select__item">
  <a href="https://translate.goog/?_x_tr_sl=en&_x_tr_tl=no" hreflang="en" class="md-select__link">
    Norsk
  </a>
</li>
<li class="md-select__item">
  <a href="https://translate.goog/?_x_tr_sl=en&_x_tr_tl=test" hreflang="en" class="md-select__link">
    Test
  </a>
</li>
"""


class Page:
    def __init__(self, page):
        self.url = page


def test_plugin_location(plugin_location):
    test = str(plugin_location.on_post_page(html, Page("TestPage"), None))
    assert (
        "https://example-com.translate.goog/subpath/TestPage?_x_tr_sl=en&_x_tr_tl=no"
        in test
    )
    assert (
        "https://example-com.translate.goog/subpath/TestPage?_x_tr_sl=en&_x_tr_tl=test"
        in test
    )

    test = str(plugin_location.on_post_page(html, Page(""), None))  # index
    assert "https://example-com.translate.goog/subpath?_x_tr_sl=en&_x_tr_tl=no" in test

    assert (
        "https://example-com.translate.goog/subpath?_x_tr_sl=en&_x_tr_tl=test" in test
    )


def test_plugin(plugin):
    test = str(plugin.on_post_page(html, Page("TestPage"), None))
    assert "https://example-com.translate.goog/TestPage?_x_tr_sl=en&_x_tr_tl=no" in test

    assert (
        "https://example-com.translate.goog/TestPage?_x_tr_sl=en&_x_tr_tl=test" in test
    )

    test = str(plugin.on_post_page(html, Page(""), None))  # index
    assert "https://example-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=no" in test
    assert "https://example-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=test" in test
