from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

PROFILE_PATH = os.path.abspath("chrome_profile")


def create_driver():
    options = webdriver.ChromeOptions()
    
    # 🔥 أهم سطر (حفظ الجلسة)
    options.add_argument(f"user-data-dir={PROFILE_PATH}")
    
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    return driver


def open_facebook(driver):
    driver.get("https://www.facebook.com/")
    time.sleep(5)


def ensure_logged_in(driver):
    driver.get("https://www.facebook.com/")
    time.sleep(5)

    # لو لم يكن مسجل دخول → سيظهر زر login
    if "login" in driver.current_url:
        print("🔐 سجل دخولك يدويًا مرة واحدة...")
        input("اضغط Enter بعد تسجيل الدخول...")
    else:
        print("✅ Session جاهزة")


def post_to_facebook(driver, page_url, text, image_path):
    driver.get(page_url)
    time.sleep(7)

    try:
        # مربع الكتابة
        post_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        post_box.click()
        time.sleep(2)

        post_box.send_keys(text)
        time.sleep(2)

        # رفع الصورة
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(image_path)

        time.sleep(5)

        # زر النشر
        post_button = driver.find_element(By.XPATH, "//div[@aria-label='Post']")
        post_button.click()

        print("✅ تم النشر")
        time.sleep(10)

    except Exception as e:
        print("❌ خطأ أثناء النشر:", e)
