from selenium import webdriver 



driver = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
driver.get("https://auth.sieg.com/login?ReturnUrl=https%3a%2f%2fadmin.sieg.com%2fsuporte%2fpesquisar-cliente%3fcnpj%3d15759005000170%26email%3d")

driver.find_element_by_name("txtEmail").send_keys("gustavo.morais@s..")

driver.find_element_by_name("txtPassword").send_keys("1234")


