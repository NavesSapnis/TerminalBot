from imports import *


WORD ="/html/body/div[1]/div/div[1]/main/div/main/div/button[1]/div/div[2]"
COMPL = "/html/body/div[1]/div/div[1]/main/div/header/div[4]/div[2]/div[2]/div/div/div/p[2]"
COMPL2 = "/html/body/div[1]/div/div[1]/main/div/header/div[4]/div[2]/div[2]/div/div[2]/div/p[2]"
COMPL3 = "/html/body/div[1]/div/div[1]/main/div/header/div[4]/div[2]/div[2]/div/div[3]/div/p[2]"


def buttons_xpath(index):
    return f"/html/body/div[1]/div/div[1]/main/div/main/div/button[{index}]/div/div[2]"


def get_buttons_words(driver):
    words = []
    i = 1
    while True:
        try:
            word = driver.find_element(By.XPATH,f"/html/body/div[1]/div/div[1]/main/div/main/div/button[{i}]/div/div[2]")
            words.append(word.text)
            i+=1
        except:
            break
    return words