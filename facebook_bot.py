from selenium import webdriver 
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def login():
    usr=input('Enter Email Id:')
    pwd=input('Enter Password:')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    sleep(1)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print ("Password entered")

    login_box = driver.find_element_by_id('u_0_b')
    login_box.click()
    sleep(4)
    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")

def add_friends():
    usr=input('Enter Email Id:')
    pwd=input('Enter Password:')

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com/')
    print ("Opened facebook")
    sleep(1)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print ("Password entered")

    login_box = driver.find_element_by_id('u_0_b')
    login_box.click()
    sleep(4)

    driver.get("https://www.facebook.com/friends")
    driver.find_element_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.j83agx80.cbu4d94t.buofh1pr.l9j0dhe7 > div > a:nth-child(3) > div.bp9cbjyn.j83agx80.btwxx1t3.buofh1pr.i1fnvgqd.hpfvmrgz").click()
    

    print ("Done")
    input('Press anything to quit')
    driver.quit()
    print("Finished")

def main():
    while True:
        txt=input("Hello, how I can help you?")
        x=txt.lower()
        if 'login' in x:
            login()
        elif 'friends' in x or 'friend' in x:
            add_friends()
        else:
            print("Sorry I can not do your work because I am not allowed to do that thing")
            print("Thank you")
            R=input("Do you wan't to do anything more?")
            r=r.lower()
            if 'yes' in r or 'y' in r or 'ya' in r:
                main()
            else:
                break

main()