from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json



def Run():
    print("Uploader started")
    
    # Instagram bilgilerinizi girin
    # uses credential.json
    with open("credential.json", "r") as file:
        credential = json.load(file)
        """
        {"email":"","password":""}
        """
    username = credential["email"]
    password = credential["password"]

    image_path = os.path.abspath("ballbounce.mp4")
    content_size = os.path.getsize(image_path)
    content_uploadSize = int(content_size / (1024 * 1024)) + 1
    caption = "test1" + str(content_size)

    # WebDriver'ı başlat
    # Alternatif olarak, 'webdriver.Firefox()' kullanabilirsiniz
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    # Giriş yapmayı bekleyin
    try:
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
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
        new_post_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "svg[aria-label='Yeni Gönderi']"))
        )
        new_post_button.click()
        print("Yeni gönderi butonuna tıklandı...")

        new_post_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/div/div/div[1]/a[1]/div[1]"))
        )
        new_post_button.click()
        print("Gönderi oluşturma butonuna tıklandı...")
    except Exception as e:
        print("Yeni gönderi butonu bulunamadı:", e)
        driver.quit()

    # Görüntü yükleme
    try:
        print("Görüntü yükleniyor...")
        upload_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/form/input"))
        )
        upload_input.send_keys(image_path)
        print("Görüntü yükleme başarılı.")
    except Exception as e:
        print("Görüntü yükleme başarısız:", e)
        driver.quit()

    time.sleep(5)

    # İleri butonuna basmak
    try:
        try:
            closePopUp_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]")))
            closePopUp_button.click()
            print("Popup kapatma butonuna tıklandı.")
        except Exception as e:
            print(e)
            
        
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div")))
        next_button.click()
        print("İleri butonuna tıklandı.")
        time.sleep(2)  # Bir sonraki sayfanın yüklenmesi için bekleyin
        next_button = driver.find_element(
            By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div")
        next_button.click()
        print("İleri butonuna tekrar tıklandı.")
    except Exception as e:
        print("İleri butonu bulunamadı:", e)
        driver.quit()

    time.sleep(2)

    # Başlık eklemek ve paylaşmak
    try:
        share_button = driver.find_element(
            By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div")
        share_button.click()
        print("Gönderi paylaşma butonuna tıklandı.")
    except Exception as e:
        print("Gönderi paylaşma başarısız:", e)
        driver.quit()

    # Paylaşımın tamamlanması için bekleyin
    time.sleep(30+(content_uploadSize*content_uploadSize))

    # Çıkış yapma
    try:
        try:
            closePopUp_button = driver.find_element(
                By.CSS_SELECTOR, "svg[aria-label='Kapat']")
            closePopUp_button.click()
            print("Popup kapatma butonuna tıklandı.")
        except:
            pass

        time.sleep(3)
        options_button = driver.find_element(
            By.CSS_SELECTOR, "svg[aria-label='Ayarlar']")
        options_button.click()
        print("Ayarlar butonuna tıklandı.")

        time.sleep(3)
        logout_button = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]")
        logout_button.click()
        print("Çıkış butonuna tıklandı.")
    except Exception as e:
        print("Çıkış yapma başarısız:", e)
        driver.quit()

    # Tarayıcıyı kapatın
    time.sleep(5)
    driver.quit()

    print("Upload tamamlandı")