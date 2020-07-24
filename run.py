from selenium import webdriver;
import time;
import random;
import urllib;
import os;
import urllib.request
from bs4 import BeautifulSoup;
from vsco import *

chrome_path =r"drivers\chrome\chromedriver.exe" #driver needs to be the same version as your chrome version
profileLink = input("enter a vsco profile url")
driver = webdriver.Chrome(chrome_path)
driver.get(profileLink)
print("trying: ",profileLink," ...")
option = 0
if option ==1:
    profileName = "test23"
    saveDir = "img/" + profileName


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


    time.sleep(random.uniform(3, 10))  # time to wait

    htmlSource=driver.page_source#get html code from selenium loaded site

    soup= BeautifulSoup(htmlSource,"html.parser")#input html code from selenium to beautiful soup

    galleryItems = soup.find_all("figure", {"class": "gallery-item"})

   # imgTagsInGallery = galleryItems.find_all('img')

    finalImgUrls = []

    for imgs in galleryItems:
        if imgs.find("img") != None:  # make sure it has the set of img res (x1 x2 x3)
            singleImg = imgs.find("img")

            string = singleImg.get("src")  # set it to a var for manipulation

            finalImgUrls.append(str(string))

if option ==0:
    saveDir= get_vsco_un(profileLink)
    finalImgUrls= get_vsco_imgs(profileLink,driver)


count = 0;
print("Found ",len(finalImgUrls)," images!")

if not os.path.exists(saveDir):#create folder with the name of the vcso account.
    os.mkdir(saveDir)
    print("Directory " , saveDir ,  " Created ")
else:
    print("Directory " , saveDir ,  " already exists")

for imgs in finalImgUrls:
    print("Saving: "+imgs)
    imagefile = open(saveDir + "/" + str(count)+".jpg", "wb")
    imagefile.write(urllib.request.urlopen(str(imgs)).read())
    imagefile.close()
    print("DONE!")
    count=count+1

print("IMAGE SCRAPE COMPLETE")