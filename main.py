from selenium import webdriver

chrome_driver_path = r"C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.in/Toblerone-Switzerland-Combo-Chocolate-Swiss/dp/B08FX78D46/ref=sr_1_3?dchild=1&keywords=toblerone&qid=1631011319&sr=8-3")

price = driver.find_element_by_id("priceblock_ourprice")
print("The price of the chocolate is:", price.text)
