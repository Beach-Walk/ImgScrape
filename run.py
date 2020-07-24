from selenium import webdriver
import time
import random
import urllib
import os;
import urllib.request
from bs4 import BeautifulSoup

chrome_path =r"C:\bin\chromedriver.exe" #driver needs to be the same version as your chrome version
profileLink = ""
driver = webdriver.Chrome(chrome_path)
driver.get(profileLink)
option = 1
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
    profileName = profileLink[profileLink.index("vsco.co/")+8:profileLink.rindex("/")]#cut out the username from the link
    saveDir= "img/"+profileName

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
            finalImgUrls.append(str(afterStrip))


count = 0;
print("Found ",len(finalImgUrls)," images!")

if not os.path.exists(saveDir):#create folder with the name of the vcso account.
    os.mkdir(saveDir)
    print("Directory " , saveDir ,  " Created ")
else:
    print("Directory " , saveDir ,  " already exists")

for imgs in finalImgUrls:
    #makeValid="http://"+imgs[2:]#add http in front so the code to get the image can understand the link
    print("Saving: "+imgs)
    #print("As: "+saveDir+"/"+str(makeValid[makeValid.rindex("/")+1:]))
    #imagefile = open(saveDir+"/"+str(makeValid[makeValid.rindex("/")+1:]),"wb")
    imagefile = open(saveDir + "/" + str(count)+".jpg", "wb")
    #time.sleep(random.uniform(3, 10))
    #imagefile.write(urllib.request.urlopen(makeValid).read())
    imagefile.write(urllib.request.urlopen(str(imgs)).read())
    imagefile.close()
    print("DONE!")
    count=count+1

print("IMAGE SCRAPE COMPLETE")