import requests
from bs4 import BeautifulSoup

# Set the base URL of the site
base_url = "https://thegarynullshow.podbean.com/page/"

# Set the range of pages you want to scrape
start_page = 1
end_page = 100

# Open the file in write mode
with open("health-news.md", "w") as file:
    # Iterate through the pages
    for page in range(start_page, end_page + 1):
        # Make the HTTP request to the page
        url = base_url + str(page) + "/"
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the div elements with class "episode-description"
        episode_divs = soup.find_all("div", class_="episode-description")

        # Extract the contents of each div and write it to the file
        for div in episode_divs:
            content = div.get_text(strip=True)
            file.write(content + "\n")
            file.write("-" * 40 + "\n")
