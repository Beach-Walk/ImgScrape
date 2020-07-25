# ImgScrape
VSCO image scraper. Scrapes images on a profile at highest quality using Selenium & BeautifulSoup. Written in Python3.

## Limitations
- Currently only works on VSCO profiles

## Requrements
- Chrome Browser
- Chrome Driver
- Python 3 & pip
- Dependencies in requirements.txt

## To Run (assuming you have py3)
1. Download ZIP or clone repository 

2. Install dependencies
    - pip install -r requirements.txt
3. Download chrome driver
    - https://chromedriver.chromium.org/
     - Be sure your downloaded driver is the same version as the regular chrome browser you have installed.
      you can check chrome version by going to help>about chrome
    - Unzip and place .exe in the folder: drivers/chrome
  
  ## To Do
  - Add more driver support
  - Clean up code / user input
  - Add support for more than just VSCO
  - Automatically download driver?
  - ~~Fix file naming for scraped websites~~
  - ~~Fix crash on vsco profiles without "LOAD MORE" button~~
  - ~~make headless~~
