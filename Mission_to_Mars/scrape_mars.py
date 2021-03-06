
#Start beautiful soup
def scrape():
    from bs4 import BeautifulSoup as bs

    #Define variable for url for news page for NASA
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    #start webdriver to connect to chrome and open the url
    from selenium import webdriver
    # followed example from https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("/Users/rosaicelaroman/Desktop/Data_BootCamp/APIs/chromedriver", options=options)

    driver.get(url)
    page_source = driver.page_source
    soup = bs(page_source, 'lxml')

    #Initialize list for article titles and paragraphs
    news_articles = []
    par_articles = []

    #Use soup to parse through page; create loop to add the articles and paragraphs to the lists 
    articles_finder = soup.find_all('div', class_='list_text')

    for article in articles_finder:
        division = article.find('div', class_='content_title')
        title = division.find('a').get_text()
        news_articles.append(title)
        par_division = article.find('div', class_='article_teaser_body')
        par = par_division.get_text()
        par_articles.append(par)
    print('--------- News Article Titles Found!')
    print('--------- News Article Titles Paragraphs Found!')

    #create variables for the first article and paragraph
    news_title = [news_articles[0]]
    news_par = [par_articles[0]]

    print('--------- First Article Title Found!')
    print('--------- First Article Paragraph Found!')


    #---------------------------------
    #Find featured image:
    #example found in https://evancalz.medium.com/web-automation-with-splinter-db2fe006ea45

    #import splinter to interact with browser
    from splinter import Browser
    import time

    next_URL = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    # un-comment this if you are using Windows!
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path)
    # this will open up a new headless browser and navigate to our URL
    browser = Browser('chrome')
    browser.visit(next_URL)
    # tell python to pause for 10s so we can observe the browser

    # first_found = browser.find_by_partial_text('featured').first
    links_found = browser.click_link_by_partial_href('featured')
    image_url = browser.url
    featured_url = image_url
    print('--------- Featured Image Found!')
    time.sleep(5)
    browser.quit()

    #----------------------------------
    #Create dataframe from webpage content
    import pandas as pd
    #example followed: https://pythonbasics.org/pandas-web-scraping/

    pd_url = 'https://space-facts.com/mars/'

    mars_facts = pd.read_html(pd_url)
    df = mars_facts[0]
    mars_facts_df = df.rename(columns={0: "Parameters", 1: "Values"})
    mars_facts_df

    print('--------- Mars Facts Found!')

    #----------------------------------
    #Interact with the hemisphere webpage to get the url for the full image of the hemispheres
    image_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    driver.get(image_url)
    page_source = driver.page_source
    soup = bs(page_source, 'lxml')

    image_links = []

    links_finder = soup.find_all('div', class_='item')

    for link in links_finder:
    
        link = link.a['href']
    
        image_links.append(link)
        
    print('--------- Image Links Found!')

    base_url = 'https://astrogeology.usgs.gov'

    browser = Browser('chrome')

    img_urls = []

    for link in image_links:
        browser.visit(base_url + link)
        img_urls.append(browser.url)
        
        time.sleep(5)
    browser.quit()

    images = []
    for url in img_urls:
        driver.get(url)
        page_source = driver.page_source
        soup = bs(page_source, 'lxml')

        links_finder = soup.find_all('div', class_='downloads')
        for link in links_finder:
    
            link = link.a['href']
            images.append(link)

    time.sleep(5)
    print('--------- List of Image Links Created!')

    titles = []

    for url in img_urls:
        driver.get(url)
        page_source = driver.page_source
        soup = bs(page_source, 'lxml')

        links_finder = soup.find_all('div', class_='content')
        
        for link in links_finder:
    
            link = link.find('h2', class_='title').text
            titles.append(link)

    time.sleep(5)

    print('--------- List of Image Titles Created!')

    img_info = []
    for title in titles:
        for image in images:
            dict_info = {}
            # keys = ['title', 'img_url']
            dict_info['title'] = title
            dict_info['img_url'] = image
            img_info.append(dict_info)

    mars_facts_df_redo = mars_facts_df.set_index('Parameters')
    dict_object = mars_facts_df_redo.to_dict()
    print('--------- Dictionary of Images and Titles Created!')
    print('--------------Process Done!')
    
    dict_news = {'title_news': news_title}
    dict_pars = {'article_par': news_par}
    dict_feat = {'featured_image': featured_url}
    dict_facts ={'mars_facts': dict_object}
    dict_imgs = {'mars_images_full': img_info}

    # # from collections import ChainMap
    # chain = ChainMap(dict_news,dict_pars, dict_feat, dict_facts, dict_imgs)
    
    # dict_data = {'news': dict_news, 'news info': dict_pars, "featured image": dict_feat, 'mars facts': dict_facts, 'mars images': dict_imgs}

    return dict_news, dict_pars, dict_feat, dict_facts, dict_imgs
    # print(mars_facts_df) 
    # print(mars_facts_df_redo) 
    # print(dict_facts) 
    # print(dict_mars)

# scrape()