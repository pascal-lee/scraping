from selenium.webdriver import Firefox, FirefoxOptions

USER = "id"
PASS = "PASS"

#start firefox
options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

#access login page
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("Access login page.")

e = browser.find_element_by_id("id")
print("e")
