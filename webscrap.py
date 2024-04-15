from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# Create a new instance of the Firefox driver (you can also use Chrome, etc.)
driver = webdriver.Firefox()

# Define the URL you want to scrape
url = 'https://ch82142163308.ch.eng.run/?file=index.html'

# Load the webpage
driver.get(url)

# Get the page source after JavaScript has been rendered
page_source = driver.page_source

# Close the browser
driver.quit()

# Now you can use Beautiful Soup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract desired information using Beautiful Soup
# For example, get all text
all_text = soup.get_text()

# Define the filename for the text file
filename = 'webpage_text.txt'

# Save the text into a text file
with open(filename, 'w', encoding='utf-8') as file:
    file.write(all_text)
# Print out all the text
print(all_text)
