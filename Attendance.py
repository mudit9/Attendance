import mechanicalsoup
browser = mechanicalsoup.Browser()
login_page = browser.get("https://markattendance.webapps.snu.edu.in/public/application/login/login")
login_form = login_page.soup.select("form")[0]
login_form.select("#login_user_name")[0]['value'] = "ms418"
login_form.select("#login_password")[0]['value'] = "Rakhi@17"
page2 = browser.submit(login_form, login_page.url)
login_page=browser.get("https://markattendance.webapps.snu.edu.in/public/application/index/index")
login_form = login_page.soup.select("form")[0]
page3 = browser.submit(login_form, login_page.url)
print(page3.text)
