import pytest


@pytest.mark.skip_browser("firefox")
def test_matrix_site(page):
    page.goto("https://www.matrix.co.il/")
    assert "לאתר הראשי הגלובלי" in page.inner_text("li.Matrix-global-site-btn")
