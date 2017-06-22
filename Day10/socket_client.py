from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://baidu.com")

element  = WebDriverWait(driver, 5, 0.5) .until(EC.presence_of_all_elements_located((By.ID, "kw")))
#print(type(a))
element.send_keys()

driver.quit()




# import socket
#
# HOST = 'localhost'
# PORT = 9000
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
#
# while True:
#     msg = bytes(input(">>:"),encoding="utf8")
#     s.sendall(msg)
#     data = s.recv(1024)
#     print('received:', data)
# s.close()