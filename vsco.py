import sys

from selenium import webdriver;
import time;
import random;
import urllib;
import os;
import urllib.request
import re
from bs4 import BeautifulSoup;

def get_vsco_un(driver):#find username with xpath, if it cant find choose random number
    try:
        url = driver.current_url
        uName = re.search(".*\.(?:co|com)\/(?P<userid>.*?)\/.*",url).group('userid')

        return uName
    except:
        randGalName = str("gallery_" + str(int(random.uniform(0, 10000000))))  # generate random number
        print("Username element not found, using '" + randGalName + "' for folder name...")
        return randGalName

def get_vsco_imgs(profileLink,driver): #get images and return an array/list of the urls

    time.sleep(random.uniform(2, 5))# time to wait

    try:
        loadMoreButton = driver.find_element("xpath","/html/body/div[1]/div/main/div/div[3]/section/div[2]")  # click load more button
        loadMoreButton.click()

        time.sleep(random.uniform(2, 5))# time to wait

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        print("LOAD MORE Button Found...")
        print("Scrolling.", end='')
        while True:
            print(".", end='')
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(random.uniform(0.5, 1))

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("DONE")
                break
            last_height = new_height

    except:

        print("No LOAD MORE Button Found... Skipping Scroll...")

    htmlSource=driver.page_source#get html code from selenium loaded site

    soup= BeautifulSoup(htmlSource,"html.parser")#input html code from selenium to beautiful soup

    imgTags = soup.findAll('img')

    finalImgUrls=[]

    for imgs in imgTags:
        if imgs.get("srcset") != None:#make sure it has the set of img res (x1 x2 x3)
            string = imgs.get("srcset")#set it to a var for manipulation
            start = (string.rindex("2x,"))+3 #find this string to start from
            end = string.rindex("?")# end
            #print(string[start:end])
            beforeStrip = string[start:end]
            afterStrip = beforeStrip.strip()
            makeValid = "http://" + afterStrip[2:]  # add http in front so the code to get the image can understand the link
            finalImgUrls.append(str(makeValid))
    return finalImgUrls


