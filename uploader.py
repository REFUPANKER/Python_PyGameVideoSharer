from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import json


def ClickToButtonNow(driver, xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()


def ClickToButton(driver, until, xpath):
    button = WebDriverWait(driver, until).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()


def SendKeys(driver, until, sendkeys, xpath):
    button = WebDriverWait(driver, until).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    button.send_keys(sendkeys)


def Run():
    print("Uploader started")

    # Instagram bilgilerinizi girin
    # uses credential.json
    with open(".credential", "r") as file:
        credential = json.load(file)
        """
        {"email":"","password":""}
        """
    username = credential["email"]
    password = credential["password"]

    # get account info from environment 
    #username = os.environ["email"]
    #password = os.environ["password"]


    image_path = os.path.abspath("ballbounce.mp4")
    content_size = os.path.getsize(image_path)
    content_uploadSize = int(content_size / (1024 * 1024)) + 1
    # multiline description > [!] includes pre-spaces
    post_description = """its damn problem! here is the info about big planes...
#software #python #pygame #fyp #instagram #game #adhd
#explore #colors #rgb #gaming #gamer #aldous #alruad
#nerd #donkey #daily
why are you still reading ? """

    # WebDriver'ı başlat
    chrome_options = Options()
    # #chrome_options.add_argument('--headless')
    # chrome_options.add_argument("start-maximized")

    # uncomment this 2 lines below
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=650,650")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.instagram.com/accounts/login")

    # Giriş yapmayı bekleyin
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        # Kullanıcı adı ve şifre girin
        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        print("Giriş yapılıyor...")
    except Exception as e:
        print("Bir hata oluştu:", e)
        driver.quit()

    # Giriş yaptıktan sonra bekleyin
    time.sleep(5)

    # Yeni gönderi oluşturmak için
    try:
        ClickToButton(
            driver, 10, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[4]/div/span/div/a/div")
        print("Yeni gönderi butonuna tıklandı...")

        ClickToButton(
            driver, 10, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[4]/div/span/div/div/div/div[1]/a[1]/div[1]")
        print("Gönderi oluşturma butonuna tıklandı...")
    except Exception as e:
        print("Yeni gönderi butonu bulunamadı:", e)
        driver.quit()

    # Görüntü yükleme
    try:
        print("Görüntü yükleniyor...")
        SendKeys(driver, 10, image_path, "//input[@type='file']")
        print("Görüntü yükleme başarılı.")
    except Exception as e:
        print("Görüntü yükleme başarısız:", e)
        driver.quit()

    time.sleep(content_uploadSize)

    try:
        ClickToButton(
            driver, 10, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button")
        print("Popup işlem gördü.")
    except:
        pass
    # İleri butonuna basmak
    try:
        nextButton = "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"
        ClickToButton(
            driver, 10, nextButton)
        print("İleri butonuna tıklandı.")

        # time.sleep(5)  # Bir sonraki sayfanın yüklenmesi için bekleyin

        ClickToButton(
            driver, 15, nextButton)
        print("İleri butonuna tekrar tıklandı.")
    except Exception as e:
        print("İleri butonu bulunamadı:", e)
        driver.quit()

    # time.sleep(5)

    # Başlık eklemek ve paylaşmak
    try:
        SendKeys(driver, 10, post_description, "//div[@role='textbox']")
        print("Gönderi açıklaması yazıldı")

        time.sleep(3)

        ClickToButton(
            driver, 15, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div")
        print("Gönderi paylaşma butonuna tıklandı.")
    except Exception as e:
        print("Gönderi paylaşma başarısız:", e)
        driver.quit()

    # Paylaşımın tamamlanması için bekleyin
    time.sleep(30+(content_uploadSize*content_uploadSize))

    # Çıkış yapma
    try:
        ClickToButtonNow(
            driver, "/html/body/div[6]/div[1]/div/div[2]/div")
        print("Popup işlem gördü")

        # time.sleep(3)
        ClickToButton(driver, 10,
                      "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[6]/div/span/div/a")
        print("Profil butonuna tıklandı.")

        # time.sleep(3)

        ClickToButton(
            driver, 10, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div[1]/div[2]/div")
        print("Ayarlar butonuna tıklandı.")

        # time.sleep(3)

        ClickToButton(driver, 15,
                      "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/button[8]")
        print("Çıkış butonuna tıklandı.")
    except Exception as e:
        print("Çıkış yapma başarısız:", e)
        driver.quit()

    # Tarayıcıyı kapatın
    time.sleep(5)
    driver.quit()

    print("Upload tamamlandı")


if __name__ == "__main__":
    Run()
