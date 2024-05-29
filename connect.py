from imports import *
import buttons


url = "https://app.0xterminal.game/"
options = webdriver.ChromeOptions()
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"--user-agent={agent}")
options.add_extension('m.crx')
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)


wait = WebDriverWait(driver, 10)


def get_words():
    words = buttons.get_buttons_words(driver)
    return words


def start():
    driver.get(url)
    driver.set_window_size(800, 800)


def get_coml(button):
    while True:
        compl = wait.until(EC.presence_of_element_located((By.XPATH, button)))
        match = re.search(r'{(\d+)', compl.text)
        result = int(match.group(1)) if match else None
        if result is not None:
            return result


def word_click(index):
    xpath = buttons.buttons_xpath(index)
    button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()