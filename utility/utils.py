BASE_URL = "https://magento.softwaretestingboard.com/"

from selenium import webdriver
import random
import string

def get_browser():
    return webdriver.Chrome()

def generate_random_email(domain = "example.com", length = 10):
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{username}@{domain}"
