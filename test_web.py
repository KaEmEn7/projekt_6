import pytest
from playwright.sync_api import Page

"""
test_web.py: šestý projekt do Engeto Online Python Akademie

author: Kamil Mach
email: kamil.machuj@gmail.com
"""

def test_page_title(page: Page):
    # Otevření stránky
    page.goto("https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana")
    
    # Ověření, že stránka má správný titulek
    assert page.title() == "Wikipedie, otevřená encyklopedie", "Titulek stránky není správný"

def test_search_functionality(page: Page):
    # Otevření stránky
    page.goto("https://cs.wikipedia.org/wiki/Hlavn%C3%AD_strana")
    
    # Zadání vyhledávacího dotazu do vyhledávacího pole
    search_input = page.locator("input#searchInput.cdx-text-input__input[name=\"search\"]") # .cdx-search-input__text-input > input
    search_input.fill("Python (programovací jazyk)")
    
    # Odeslání vyhledávacího dotazu
    search_input.press("Enter")
    
    # Ověření, že výsledky vyhledávání obsahují správný článek
    assert "Python_(programovac%C3%AD_jazyk)" in page.url, "URL neobsahuje očekávaný článek"

def test_find_in_text(page: Page):
    # Otevření stránky
    page.goto("https://cs.wikipedia.org/wiki/Python_(programovac%C3%AD_jazyk)")
    
    # Ověření, že stránka obsahuje text "interpreted"
    content = page.locator("body").inner_text()
    assert "Guido van Rossum" in content, "Text 'Guido van Rossum' nebyl nalezen na stránce"