from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E7%BF%BB%E8%AF%91%E5%9C%A8%E7%BA%BF")

text = "input text"
js = "var sum=jQuery('div.op_translation_text_div:nth-child(1)'); sum.value='" + text + "';"
driver.execute_script(js)
# 有误，没能对textarea文本框赋值
