from selenium import webdriver
import time
driver=webdriver.Chrome(r"C:\Users\karni\PycharmProjects\ Q4SM3\drivers\chromedriver.exe")
url=r"https://www.facebook.com/"
driver.get(url)
time.sleep(2)
driver.minimize_window()
time.sleep(2)
# driver.minimize_window()
# time.sleep(2)
Title=driver.title
print(Title)
# driver.set_window_size(200,100)
# time.sleep(2)
# driver.set_window_position(300,500)
# driver.set_window_rect(200,300,500,600)
time.sleep(2)
url=r"https//google.com/"
driver.get(url)
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward(url)
time.sleep(2)
driver.close()











