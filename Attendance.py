import mechanicalsoup
browser = mechanicalsoup.Browser()
#enter Id
#Enter Password.
your_id = "enter your id here "
your_password = "enter your password here" 
login_page = browser.get("https://markattendance.webapps.snu.edu.in/public/application/login/login")
login_form = login_page.soup.select("form")[0]
#mechanicalSoup
login_form.select("#login_user_name")[0]['value'] = your_id
login_form.select("#login_password")[0]['value'] = your_password
page2 = browser.submit(login_form, login_page.url)
login_page=browser.get("https://markattendance.webapps.snu.edu.in/public/application/index/index")
login_form = login_page.soup.select("form")[0]
page3 = browser.submit(login_form, login_page.url)
print(page3.text)
