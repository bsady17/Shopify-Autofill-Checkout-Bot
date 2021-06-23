# Shopify Autofill Checkout-Bot

A Python3 and Selenium script that allows you to automatically add a product to your cart and checkout on any Shopify store.

<h3>About:</h3>
The main goal of this project is to automate the checkout process on any Shopify site and find a workaround to bot protection and queues. The bot should act as human as possible but also checkout fast enough to secure the targeted product.

<h3>Current Features:</h3>
<ul>
  <li>Add product to cart using quick link</li>
  <li>Pause script from running if captcha challenge page shows, resume script manually (hit ENTER) once captcha solved and going to checkout</li>
  <li>Auto select first available shipping rate</li>
  <li>Fill credit card information and process payment</li>
  <li>Headless (No browser popup)</li>
  <li>Checkout progress updates</li>
  <li>Average checkout time of 30-35 seconds</li>
</ul>

<h3>What still needs to be tackled:</h3>
<ul>
  <li>Popup browser to solve captcha if needed</li>
  <li>Add the ability to check if element is needed and update ID accordingly - Some sites don't require email and phone which causes the ID of the input to change. The same goes with the phone number field at the botton of the customer info form - Some sites may not require a phone number to be entered</li>
  <li>Add a condition to determine if a checkout captcha is needed.</li>
  <li>Create a bypass for the checkout queue - Generate checkout link/token before drop and use that link after updating cart with targeted product. Have seen success using this method in the past but not sure how well it works anymore.</li>
  <li>Add discord webhook support<li>
</ul>

<h3>Wishlist:</h3>
<ul>
  <li>Add proxy support</li>
  <li>Drop checkout time to 20 seconds</li>
</ul>

<h3>Usage:</h3>
<ol>
  <li>Python3</li>
  <li>Selenium</li>
  <li>Chromedriver
</ol>

```
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
```

<h3>Disclaimer:</h3>
The script will likely not work perfectly out of the box. This project was started just for fun and learning purposes so feel free to throw any suggestions my way.
