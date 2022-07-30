from selenium import webdriver;
from selenium.webdriver.chrome.options import Options
import time;
import random;
import urllib;
import os;
import urllib.request
from bs4 import BeautifulSoup;
from vsco import *
menu=True
while menu is True:
    chrome_path =r"drivers\chrome\chromedriver.exe" #driver needs to be the same version as your chrome version
    options = Options()
    options.headless=True
    driver = webdriver.Chrome(chrome_path,chrome_options=options)

    profileLink = input("Enter a VSCO profile url...\n")
    driver.get(profileLink)
    print("Trying: ",profileLink," ...")

    uName= get_vsco_un(driver)
    saveDir="img/"+uName

    finalImgUrls= get_vsco_imgs(profileLink,driver)

    count = 0;
    print("Found "+str(len(finalImgUrls))+" images!")

    if not os.path.exists(saveDir):#create folder with the name of the vcso account.
        os.mkdir(saveDir)
        print("Directory '"+str(saveDir)+"' Created ")
    else:
        print("Directory '"+str(saveDir)+"' already exists. Files may be overwritten...")
        time.sleep(3)

    for imgs in finalImgUrls:
        print("Saving: "+imgs,end='')

        fname= re.search(".*\.(?:co|com)\/.*\/(?P<fname>.*\.\w{0,5}$)",imgs).group("fname")#parse out file name from URL

        imagefile = open(saveDir + "/" + str(fname), "wb")
        imagefile.write(urllib.request.urlopen(str(imgs)).read())
        imagefile.close()
        print(" DONE!")
        count=count+1

    print("IMAGE SCRAPE COMPLETE")
    driver.quit()
    print("Driver closed\n=====")
    print("0. Exit")
    print("1. Scrape Another")
    userOption = int(input("\n"))
    if userOption == 0 or userOption > 1:
        menu=False
