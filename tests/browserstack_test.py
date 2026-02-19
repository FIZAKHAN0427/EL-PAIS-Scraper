
def test_elpais(driver):
    driver.get("https://elpais.com/opinion/")
    assert "Opinión" in driver.title