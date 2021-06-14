    
def scrape():  
    from bs4 import BeautifulSoup as bs

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    from selenium import webdriver
    # followed example from https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/Users/rosaicelaroman/Desktop/Data_BootCamp/APIs/chromedriver", options=options)

    driver.get(url)

    page_source = driver.page_source

    soup = bs(page_source, 'html')

    news_articles = []
    par_articles = []

    articles_finder = soup.find_all('div', class_='list_text')

    for article in articles_finder:
        division = article.find('div', class_='content_title')
        title = division.find('a').get_text()
        news_articles.append(title)
        par_division = article.find('div', class_='article_teaser_body')
        par = par_division.get_text()
        par_articles.append(par)
    print(news_articles)
    print(par_articles)


    news_title = news_articles[0]

    news_par = par_articles[0]

    print(news_title)
    print(news_par)

    from splinter import Browser
    import time

    URL = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    # un-comment this if you are using Windows!
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path)
    # this will open up a new headless browser and navigate to our URL
    browser = Browser('chrome')
    browser.visit(URL)
    # tell python to pause for 10s so we can observe the browser

    # first_found = browser.find_by_partial_text('featured').first
    links_found = browser.click_link_by_partial_href('featured')
    image_url = browser.url
    print(image_url)
    time.sleep(10)
    browser.quit()

    featured_image_url = image_url
    print(featured_image_url)

    import pandas as pd
    #example followed: https://pythonbasics.org/pandas-web-scraping/

    pd_url = 'https://space-facts.com/mars/'

    mars_facts = pd.read_html(pd_url)


    print(len(mars_facts))
    print(mars_facts[0])


    df = mars_facts[0]
    mars_facts_df = df.rename(columns={0: "Parameters", 1: "Values"})
    mars_facts_df

    driver.get(image_url)

    soup = bs(page_source, 'html')

    image_links = []

    links_finder = soup.find_all('div', class_='item')

    for link in links_finder:
    
        link = link.a['href']
    
        image_links.append(link)
        
    print(image_links)

    base_url = 'https://astrogeology.usgs.gov'

    browser = Browser('chrome')

    img_urls = []

    for link in image_links:
        browser.visit(base_url + link)
        img_urls.append(browser.url)
        
        time.sleep(30)
        

    browser.quit()
    print(img_urls)

    images = []
    for url in img_urls:
        driver.get(url)
        page_source = driver.page_source
        soup = bs(page_source, 'html')

        links_finder = soup.find_all('div', class_='downloads')
        for link in links_finder:
    
            link = link.a['href']
            images.append(link)
    
    


    print(images)

    time.sleep(10)

    titles = []

    for url in img_urls:
        driver.get(url)
        page_source = driver.page_source
        soup = bs(page_source, 'html')

        links_finder = soup.find_all('div', class_='content')
        
        for link in links_finder:
    
            link = link.find('h2', class_='title').text
            titles.append(link)


    print(titles)

    time.sleep(10)

    img_info = []
    for title in titles:
        for image in images:
            dict_info = {}
            # keys = ['title', 'img_url']
            dict_info['title'] = title
            dict_info['img_url'] = image
            img_info.append(dict_info)
    print(img_info)



