from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# assert 'Selenium Easy Demo' in chrome_browser.title
#Selectors to grab Items
# button = chrome_browser.find_element_by_class_name('btn btn-default')
# print(button.__getattribute__('innerHTML'))


#select the input Field
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys("This Is Nitesh")

#Select the button 
# Show_message_button = chrome_browser.find_element_by_class_name("btn btn-default")
# Show_message_button.click()

#addition input

assert 'Get Total' in chrome_browser.page_source
get_Sum1 = chrome_browser.find_element_by_id("sum1")
get_Sum1.clear()
get_Sum1.send_keys(1)
get_Sum2 = chrome_browser.find_element_by_id("sum2")
get_Sum2.clear()
get_Sum2.send_keys(4)
get_total_button = chrome_browser.find_elements_by_css_selector('.btn').click()

chrome_browser.close()
chrome_browser.close()
chrome_browser.quit()