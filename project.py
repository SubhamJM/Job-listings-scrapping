from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

query = 'python'
driver = webdriver.Firefox()
d = {}
i = 0

for page in range(1,101):  
    driver.get(f"https://www.naukri.com/{query}-jobs-{page}?k={query}")

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    jobs = soup.find_all('div','cust-job-tuple')


    for job in jobs:
        knowledge = ''
        title = job.find('a','title').get('title')
        try:
            experience = job.find('span','expwdth').text
        except:
            experience = 'no mention'
        try:
            knowledges = job.find('ul','tags-gt').find_all('li')
            for j in knowledges:
                knowledge = knowledge + j.text + ','
            knowledge = knowledge.strip(',')
        except:
            knowledge = 'not mentioned'
        salary = job.find('span','sal-wrap').span.span.text
        try:
            location = job.find('span','locWdth').text
        except:
            location = 'not mentioned'
        day_of_post = job.find('span','job-post-day').text
        try:
            rating = job.find('span','main-2').text
        except:
            rating = 'no rating'
        try:
            num_reviews = job.find('a','review ver-line').text.strip('Reviews ')
        except:
            num_reviews = ' - '

        d[i] = [title,experience,knowledge,salary,location,day_of_post,rating,num_reviews]
        i += 1

driver.quit()

with open('Naukri_project/result.csv','w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['job','experience','knowledge','salary','location','day of post','rating','number of reviews'])
    for i in range(len(d)):
        writer.writerow(d[i])
    


