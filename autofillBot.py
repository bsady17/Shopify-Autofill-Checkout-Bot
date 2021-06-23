import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Product/store information
storeUrl = "guru-testing-store1.myshopify.com"
variantID = "39323260223510"

#Perrsonal information
email = "jbcholmes@gmail.com"
firstName = "John"
lastName = "Doe"
address = "1203-700 9 St SW"
city = "Calgary"
country = "Canada"
province = "Alberta"
postal = "T2P2B5"
phone = "5879172864"

CCNumber = "4242"
CCNumber2 = "4242"
CCNumber3 = "4242"
CCNumber4 = "4242"
CCName = "John Doe"
CCExpiry = "12/"
CCExpiry2 = "34"
CCVerification = "123"

#Start timing the checkout duration
start = time.time()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#Create WebDriver to prompt what browser should open
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
driver.set_window_size(1024, 768)
#Add to cart
print("Adding to cart...")
driver.get("https://" + storeUrl + "/cart/add?id=" + variantID + "&quantity=1")
#Go to checkout
driver.get("https://" + storeUrl + "/checkout")

captchaUrl = driver.current_url

#Check if captcha is needed, if so, the script will pause until captcha is manually completed and then continue to the customer info page.
if "challenge" in captchaUrl:
    print("Captcha found! Please solve manually...")
    input("Press Enter to continue...")
else:
    print("No captcha found! Going to Checkout...")

#Once captcha is solved or no captcha was found, start filling out the customer information section
print("Filling contact information...")
myEmail = driver.find_element_by_id("checkout_email_or_phone")
myEmail.send_keys(email)
time.sleep(0.1)

fName = driver.find_element_by_id("checkout_shipping_address_first_name")
fName.send_keys(firstName)
time.sleep(0.1)

lName = driver.find_element_by_id("checkout_shipping_address_last_name")
lName.send_keys(lastName)
time.sleep(0.1)

address1 = driver.find_element_by_id("checkout_shipping_address_address1")
address1.send_keys(address)
time.sleep(0.1)

mycity = driver.find_element_by_id("checkout_shipping_address_city")
mycity.send_keys(city)
time.sleep(0.1)


myCountry = driver.find_element_by_id("checkout_shipping_address_country")
myCountry.send_keys(country)
time.sleep(0.1)

myProvince = driver.find_element_by_id("checkout_shipping_address_province")
myProvince.send_keys(province)
time.sleep(0.1)

zipCode = driver.find_element_by_id("checkout_shipping_address_zip")
zipCode.send_keys(postal)
time.sleep(0.1)

#phoneNumber = driver.find_element_by_id("checkout_shipping_address_phone")
#phoneNumber.send_keys(phone)
#time.sleep(0.1)

#Go to the Shipping page (it will keep the default shipping rate selection)
time.sleep(1)
toShipping = driver.find_element_by_id('continue_button').click()
print("Selecting shipping rate...")

#Go to the payment page
time.sleep(1.5)
toPayment = driver.find_element_by_id('continue_button').click()

#Fill credit card info
print("Adding payment details...")

driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-number-')]"))
driver.find_element_by_id("number").send_keys(CCNumber)
time.sleep(0.1)
driver.find_element_by_id("number").send_keys(CCNumber2)
time.sleep(0.1)
driver.find_element_by_id("number").send_keys(CCNumber3)
time.sleep(0.1)
driver.find_element_by_id("number").send_keys(CCNumber4)
time.sleep(0.1)

driver.switch_to.parent_frame()

driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-name-')]"))
driver.find_element_by_id("name").send_keys(CCName)
time.sleep(0.1)

driver.switch_to.parent_frame()

driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-expiry-')]"))
driver.find_element_by_id("expiry").send_keys(CCExpiry)
time.sleep(0.5)
driver.find_element_by_id("expiry").send_keys(CCExpiry2)
time.sleep(0.5)

driver.switch_to.parent_frame()

driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id, 'card-fields-verification_value-')]"))
driver.find_element_by_id("verification_value").send_keys(CCVerification);
time.sleep(0.1)

driver.switch_to.parent_frame();

#Press the pay now button to start processing payment
driver.find_element_by_id('continue_button').click()
print("Processing Payment...")

#Check to see if order was successfully processed
time.sleep(11)
orderConfirmation = driver.current_url
if "thank_you" in orderConfirmation:
    print("Copped!")
else:
    print("Better luck next time...")

order = driver.find_element_by_xpath("//span[@class='os-order-number']").get_attribute('innerHTML');
print(order);
print('[[ Duration: ', time.time()-start, 'seconds ]]')

#exit()
