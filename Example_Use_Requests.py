'''
Example of how to use the Request and Beautiful Soup libraries 
to grab, parse and extract data from the websites.
Autor: Masdesouza

'''

import requests

topics_url = 'https://github.com/topics' #this is the url of the page that we want to scrape

response = requests.get(topics_url) #this is the request to the page

if response.status_code != 200: #if the request is not successful
    raise Exception('Failed to load page {}'.format(topics_url))
else:
    page_content = response.text #this is the content of the page

    with open('topics.html', 'w', encoding='utf-8') as f:
        f.write(page_content)


    from bs4 import BeautifulSoup

    doc = BeautifulSoup(page_content, 'html.parser') #this is the document that we will parse
    
    #It grabing all the topics in github
    selection_class="f3 lh-condensed mb-0 mt-1 Link--primary"
    topic_title_tags=doc.find_all('p',{'class':selection_class}) #find_all('p',class_=selection_class) we can use this as well

    #How many topics?
    #print(len(topic_title_tags))

    #print all topics
    #print(topic_title_tags)

    #print the first topic
    #print(topic_title_tags[0])

    #print the text of the first topic
    #print(topic_title_tags[0].text.strip())

    #print the text of all topics
    topic_titles=[]
    for tag in topic_title_tags:
        topic_titles.append(tag.text.strip())
    
    #print(topic_titles)

    #It grabing all the describtion of topics in github
    desc_selector = "f5 color-fg-muted mb-0 mt-1"
    topic_desc_tags = doc.find_all('p', {'class': desc_selector})

    #print the first description
    #print(topic_desc_tags[0].text.strip())

    #print the description of all topics
    topic_descs=[]
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())

    #print(topic_descs) 
    
    #Demonstration of how to grab the link each the topic 
    topic_link_tags = doc.find_all('a', {'class': 'no-underline flex-1 d-flex flex-column'})

    topic_urls = []
    base_url = 'https://github.com'
    for tag in topic_link_tags:
        topic_urls.append(base_url + tag['href'])

    #print all the urls generated
    #print(topic_urls)

    #create a CSV file with the data
    import csv
    import pandas as pd

    #First, we create a dictionary with the data
    topic_dict = {'title': topic_titles, 'description': topic_descs, 'url': topic_urls}

    #Create a Pandas DataFrame from the dictionary
    topic_df = pd.DataFrame(topic_dict)

    topic_df.to_csv('topics.csv', index=None)

    #create a JSON file with the data
    topic_df.to_json('topics.json')




    #Getting information out of a topic page
    topic_page_url = topic_urls[0]
    response = requests.get(topic_page_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topic_page_url))
    else:
        topic_doc = BeautifulSoup(response.text, 'html.parser')
        
        #printing the html of the page
        #print(topic_doc)
        
        #It grabing the information of the topic
        div_p_selection_class = "markdown-body f5 mb-2"
        repo_tags = topic_doc.find_all('div', {'class': div_p_selection_class})

        #print the information of topic
        #print(repo_tags[0].text.strip()) 

        #It grab the all repository
        h3_selection_class = "f3 color-fg-muted text-normal lh-condensed"
        repo_tags = topic_doc.find_all('h3', {'class': h3_selection_class})

        #print the first repository
        #print(repo_tags[0])

        #print the text of the first repository
        #print(repo_tags[0].text.strip())

        a_tags = repo_tags[0].find_all('a')
        relative_repo_url = a_tags[1]['href']

        #print the url of the first repository
        #print(base_url + relative_repo_url)

        #It grab the first repository
        url_first_repo = base_url + relative_repo_url
        response = requests.get(url_first_repo)
        if response.status_code != 200:
            raise Exception('Failed to load page {}'.format(url_first_repo))            
        else:
            #It grabing the README file of the first repository
            repo_doc = BeautifulSoup(response.text, 'html.parser')
            h2_selection_class = "Box-title"
            readme_h2 = repo_doc.find_all('h2',h2_selection_class)

            #it url relative of the README file
            readme_relative_url = readme_h2[0].find_all('a')[0]['href']
            #print(readme_relative_url)

            #it url absolute of the README file
            readme_absolute_url = base_url + readme_relative_url

            #it grabing the README file
            response = requests.get(readme_absolute_url)

            if response.status_code != 200:
                raise Exception('Failed to load page {}'.format(readme_absolute_url))  
            else:
                #it grabing the README file
                print(response.text)          














        







