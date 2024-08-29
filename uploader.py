import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import json


def TryToClickButton(driver,until,xpath):
    try:
        ClickToButton(driver,until,xpath)
    except:
        print("Cant click to")
        print(xpath)

def ClickToButton(driver, until, xpath):
    button = WebDriverWait(driver, until).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()

def SendKeys(driver, until, sendkeys, xpath):
    element = WebDriverWait(driver, until).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(sendkeys)

def SaveCookies(driver):
    cookies = driver.get_cookies()
    print("Saving auth cookies...")
    with open("cookies.pkl", "wb") as file:
        pickle.dump(cookies, file)
    print("Cookies saved")

def FillCookieManual(driver):
    print("Receiving cookie data...")
    while input("Type 'ready' to finish manual filling: ") != "ready":
        pass
    SaveCookies(driver)

def Run():
    print("Uploader started")

    # Instagram credentials
    with open(".credential", "r") as file:
        credential = json.load(file)
    username = credential["email"]
    password = credential["password"]

    image_path = os.path.abspath("ballbounce.mp4")
    content_size = os.path.getsize(image_path)
    content_uploadSize = int(content_size / (1024 * 1024)) + 1
    post_description = """its damn problem! here is the info about big planes...
#software #python #pygame #fyp #instagram #game #adhd
#explore #colors #rgb #gaming #gamer #aldous #alruad
#nerd #donkey #daily
why are you still reading ? """
    logOutAfterPost = False

    # Initialize WebDriver
    chrome_options = Options()
    # Uncomment for headless mode and debugging
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=650,650")
    chrome_options.add_argument("--lang=en")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.instagram.com/accounts/login")

    #FillCookieManual(driver)

    print("Checking cookies...")
    if os.path.exists("cookies.pkl"):
        print("Cookie data exists.")
        with open("cookies.pkl", "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
    else:
        try:
            ClickToButton(driver, 10, "//input[@name='username']")
            ClickToButton(driver, 10, "//input[@name='password']")

            username_input = driver.find_element(By.NAME, "username")
            password_input = driver.find_element(By.NAME, "password")

            username_input.send_keys(username)
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)
            print("Logging in...")
        except Exception as e:
            print("An error occurred:", e)
            driver.quit()
    
    # FillCookieManual(driver)
    # driver.quit()
    # return
    
    # Wait for login to complete
    print("waiting for load screen (3sec)")
    time.sleep(3)

    print("closing open notifications popup")
    TryToClickButton(driver,10,"//button[text()='Not Now']")

    # Create a new post
    try:
        print("----- Progress started -----")
        ClickToButton(driver, 10, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[4]/div/span/div/a/div/div/div/div")
        print("Create button clicked...")
        ClickToButton(driver, 10, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[4]/div/span/div/div/div/div[1]/a[1]")
        print("Create new post button clicked...")
    except Exception as e:
        print("Create new post button not found:", e)
        driver.quit()

    # Upload image
    try:
        print("Uploading image...")
        SendKeys(driver, 10, image_path, "//input[@type='file']")
        print("Image upload successful.")
        TryToClickButton(driver,10,"//button[text()='OK']")
    except Exception as e:
        print("Image upload failed:", e)
        driver.quit()

    time.sleep(content_uploadSize)

    try:
        ClickToButton(driver, 10, "//div[text()='Next']")
        print("Next button clicked.")
        ClickToButton(driver, 10, "//div[text()='Next']")
        print("Filter Next button clicked.")
    except:
        pass

    # Add description and share
    try:
        SendKeys(driver, 10, post_description, "//div[@role='textbox']")
        print("Post description entered")

        time.sleep(3)

        ClickToButton(driver, 15, "//div[text()='Share']")
        print("Post share button clicked.")
    except Exception as e:
        print("Post sharing failed:", e)
        driver.quit()

    # Wait for the post to be completed
    time.sleep(30 + (content_uploadSize * content_uploadSize))

    if logOutAfterPost:
        try:
            ClickToButton(driver, 10, "//div[@aria-label='Account']")
            print("Popup processed")
            ClickToButton(driver, 10, "//div[text()='Settings']")
            print("Settings button clicked.")
            ClickToButton(driver, 15, "//button[text()='Log Out']")
            print("Log out button clicked.")
        except Exception as e:
            print("Log out failed:", e)
            driver.quit()

    # Close the browser
    SaveCookies(driver)
    time.sleep(5)
    driver.quit()

    print("Upload completed")

if __name__ == "__main__":
    Run()
