import time
import mechanicalsoup
#enter ID
your_id = ""
your_password = ""
browser = mechanicalsoup.Browser()
login_page = browser.get("https://markattendance.webapps.snu.edu.in/public/application/login/login")
login_form = login_page.soup.select("form")[0]
login_form.select("#login_user_name")[0]['value'] = your_id
login_form.select("#login_password")[0]['value'] = your_password
page2 = browser.submit(login_form, login_page.url)	
while 1:
    page2 = browser.submit(login_form, login_page.url)
    time.sleep(10) #check every 10 seconds 
    page3 = browser.submit(login_form, login_page.url)
    if(page2.text!=page2.text):
        print("Initiated!")
        break
    else:
        print('Not yet..')
 

