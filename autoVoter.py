from selenium import webdriver
import os
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
web = webdriver.Firefox(firefox_profile=profile)


NlUsage = 0 #9 max
JpUsage = 0 #3 max
UsUsage = 0 #4 max
voteCount = 0
while True:

    vpnCountry = ""
    vpnNum = 0

    if NlUsage <= 9:
        vpnCountry = "NL"
        NlUsage += 1
        vpnNum = NlUsage
        print(f"Using NetherLands server number {NlUsage}")

    elif JpUsage <= 3:
        vpnCountry = "JP"
        JpUsage += 1
        vpnNum = JpUsage
        print(f"Using Japan server number {JpUsage}")

    elif UsUsage <= 4:
            vpnCountry = "US"
            UsUsage += 1
            vpnNum = UsUsage
            print(f"Using US server number {JpUsage}")
    else:
        print("Out of servers, breaking.")
        break

    vpnServer = f'{vpnCountry}-FREE#{vpnNum}'
    print(f"vpnServer: {vpnServer}")
    os.system(f"protonvpn-cli c {vpnServer}")
    time.sleep(10)
    web.refresh()

    web.get('https://topminecraftservers.org/server/16816')


    voteButton = web.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/a")
    voteButton.click()


    vote2 = web.find_element_by_xpath('//*[@id="voteButton"]')
    vote2.click()
    voteCount += 1
    print(f"Vote {voteCount} done successfully!")
