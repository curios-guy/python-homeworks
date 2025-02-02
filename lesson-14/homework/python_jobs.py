import sqlite3
import requests
from bs4 import BeautifulSoup
from unique_id_generator import create_unique_id

res = requests.get("https://realpython.github.io/fake-jobs/")
print(res)
soup = BeautifulSoup(res.content, 'html.parser')
main_divs = soup.find_all(class_ = 'card-content')

jobs_data = []
for div in main_divs:
    job_title = div.find_all('h2')[0].text
    comp_name = div.find_all('h3')[0].text
    comp_location = div.find_all(class_ = 'location')[0].text
    lctn_comp = str(comp_location).strip()
    # print(lctn_comp)
    app_link = div.find_all(class_ = 'card-footer-item')[1]
    # print(app_link['href'])
    another_res = requests.get(app_link['href'])
    sub_soup = BeautifulSoup(another_res.content, 'html.parser')
    job_desc = (sub_soup.find_all(class_ = 'content')[0].find_all('p')[0].text)
    
    jobs_data.append((create_unique_id(), job_title, comp_name, lctn_comp, job_desc, app_link['href']))




with sqlite3.connect("fake_jobs.db") as con:
    cursor = con.cursor()
    
    # cursor.execute("DROP table if exists Jobs")
    cursor.execute("CREATE table IF NOT EXISTS Jobs(id int, job_title text, company_name text, location text, job_desc longtext, app_link longtext)")
    cursor.executemany(f"INSERT into Jobs Values(?, ?, ?, ?, ?, ?)", jobs_data)



# for test, ignore this part
"""def get_job(idd):
    cursor.execute(f"SELECT * from Jobs WHERE id = {idd}")
    job = cursor.fetchone()
    # cursor.close()
    print(type(job))
    return job


def insert_new_job(data):
    cursor.executemany("INSERT into Jobs Values(?, ?, ?, ?, ?)", data)

def update_job(idd, job_title, comp_name, location, job_desc, app_link):
    # job = get_job(idd)

    # edit = list(job)

    # edit[1] = job_title
    # edit[2] = comp_name
    # edit[3] = location
    # edit[4] = job_desc
    # edit[5] = app_link

    # data = tuple(edit)
    # try: 
    cursor.execute(f"UPDATE Jobs SET job_title = {job_title}, company_name = {comp_name}, location = {location}, job_desc = {job_desc}, app_link = {app_link} WHERE id = {idd}")
    print("Hooray!!!")
    # except None:
        # insert_new_job(data)



print(update_job(5754, "asdasda", "dasdasd", "sadasdasd", "dasdas", "google.com"))
"""