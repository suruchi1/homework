#Imports & Dependencies
from splinter import Browser
from bs4 import BeautifulSoup

#Site Navigation
executable_path = {"executable_path": "/Users/suruchichaudhary/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)