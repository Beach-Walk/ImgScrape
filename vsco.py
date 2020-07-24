from selenium import webdriver;
import time;
import random;
import urllib;
import os;
import urllib.request
from bs4 import BeautifulSoup;

def get_vsco_un(profileLink):

    profileName = profileLink[profileLink.rindex("/")+1:]  # cut out the username from the link
    saveDir = "img/" + profileName
    print(saveDir)
    return saveDir

def get_vsco_imgs(profileLink,driver):

    time.sleep(random.uniform(3, 10))# time to wait

    loadMoreButton = driver.find_elements_by_xpath("/html/body/div/div/main/div/div[5]/section/div[2]/button")[0]#click load more button
    loadMoreButton.click()

    time.sleep(random.uniform(3, 10))# time to wait

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(random.uniform(0.5, 1))

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

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


