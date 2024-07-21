from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_login():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:3000/")
    assert "Vota Ai" in driver.title
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/section[1]/div[1]/div/div[1]/button")
    login_button.click()
    # id username-label
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username-label")))
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("admin")
    password_input = driver.find_element(By.ID, "senha")
    password_input.send_keys("admin")
    login = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/button")
    login.click()
    # http://localhost:3000/home
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost:3000/home"))
    assert "http://localhost:3000/home" == driver.current_url
    driver.quit()

def test_auditar():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:3000/")
    assert "Vota Ai" in driver.title
    login_button = driver.find_element(By.XPATH, "/html/body/div/div/section[1]/div[1]/div/div[1]/button")
    login_button.click()
    # id username-label
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username-label")))
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("admin")
    password_input = driver.find_element(By.ID, "senha")
    password_input.send_keys("admin")
    login = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/button")
    login.click()
    # http://localhost:3000/home
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost:3000/home"))
    assert "http://localhost:3000/home" == driver.current_url
    driver.get("http://localhost:3000/auditoria")
    audit_title = driver.find_element(By.CLASS_NAME, "title-space").find_element(By.TAG_NAME,'h1').text
    assert audit_title == "AUDITORIA"
    audit_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/input')
    audit_input.send_keys("hash1")
    audit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div/div[1]/button')
    audit_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//html/body/div[2]/div[3]/div[2]/div[1]/h2')))
    modal_title = driver.find_element(By.XPATH, '//html/body/div[2]/div[3]/div[2]/div[1]/h2').text
    assert modal_title == 'Informações da Participação'
    driver.quit()
