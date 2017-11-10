import requests
from bs4 import BeautifulSoup

def zipCode(storeNumber):
    url='https://www.walmart.com/store/' + storeNumber
    source_code=requests.get(url)
    plain_text=source_code.text
    if not plain_text.endswith("</html>"):
        print("It is an correct Store Number.")
    else:
        soup = BeautifulSoup(plain_text, "lxml")
        # print(soup)
        for link in soup.findAll('span', itemprop="postalCode"):
            postalcode = link.string
            if str(postalcode) != "None":
                print("Zipcode of walmart store number %s is : " %storeNumber+postalcode)


storeNumber=input("Enter the Walmart Store Number: ")
if storeNumber.isdigit():
    zipCode(storeNumber)
else:
    print("Value not a valid Walmart code.")