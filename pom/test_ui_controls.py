import pytest
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.hover_page import HoverPage

@pytest.mark.usefixtures("setup")
class TestUIControls:

    def test_checkboxes(self):
        page = CheckboxPage(self.driver)
        page.load()
        page.check_first_uncheck_second()

    def test_dropdown(self):
        page = DropdownPage(self.driver)
        page.load()
        page.select_option("Option 2")

    def test_hover_action(self):
        page = HoverPage(self.driver)
        page.load()
        page.hover_first_figure()
        assert "not found" not in self.driver.page_source.lower()
