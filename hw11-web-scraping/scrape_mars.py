# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

# Execute all of the scraping code from `mission_to_mars.ipynb` and return one Python dictionary containing all of the scraped data
def scrape():

    # Initialize browser
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # 1. NASA Mars News
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Browser visit
    browser.visit(url)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Extract news title and paragraph text
    latest_news = soup.find("li", class_="slide")
    news_title = latest_news.find("h3").text
    news_p = latest_news.find(class_="article_teaser_body").text


    # 2. JPL Mars Space Images - Featured Image
    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Browser visit
    browser.visit(url)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find image URL for current featured Mars image
    # soup.find(class_="main_feature").footer.a["data-fancybox-href"]
    base_url = "https://www.jpl.nasa.gov"
    style = soup.find(class_="main_feature").find(class_="carousel_items").article["style"]
    featured_image_url = base_url + style.split("url")[1].strip(";(')")


    # 3. Mars Weather
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    # Browser visit
    browser.visit(url)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest Mars weather tweet
    mars_weather = soup.find("li", class_="js-stream-item").find("p", class_="tweet-text").text


    # 4. Mars Facts
    # URL of page to be scraped
    url = 'https://space-facts.com/mars/'

    # Return a list of dataframes for any tabular data that Pandas found
    table = pd.read_html(url)[0]

    # Rename table columns
    table.rename(columns={0:"metric", 1:"value"}, inplace=True)

    # Convert dataframe to HTML table string
    table_html = table.to_html(index=False)

    # Strip unwanted newlines to clean up the table
    table_html = table_html.replace('\n', '')

    # Strip table tag for easier html formatting
    table_html = table_html.replace("<table border=\"1\" class=\"dataframe\">", "").replace("</table>", "").strip()


    # 5. Mars Hemispheres
    # URL of page to be scraped
    url_parent = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Browser visit
    browser.visit(url_parent)

    # Create a Beautiful Soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Child website links for each hemisphere
    base_url = "https://astrogeology.usgs.gov"
    links = [base_url + item.find(class_="description").a["href"] for item in soup.find_all("div", class_="item")]

    # Extract hemisphere title and image url from each child website
    hemisphere_image_urls = []

    for url in links:
        
        # from url to soup
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract data
        title = soup.find("div", class_="content").find("h2", class_="title").text.replace(" Enhanced", "")
        img_url = base_url + soup.find("img", class_="wide-image")["src"]
        
        # Store in list
        hemisphere_image_urls.append({"title": title, "img_url": img_url})


    # Quit browser
    browser.quit()


    # Store in dictionary
    mars = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "table_html": table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Return results
    return mars
