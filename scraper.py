import requests
from bs4 import BeautifulSoup

url = "https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&topicid=ART"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
course_list = soup.select("dl.course-list")
course_links = course_list[0].find_all("a", limit=1)
print(course_links)
print(type(course_links))
print(len(course_links))

# for each course name listed 
for course in course_links:
    print(course.get("href")) # course url
    print(course.get_text()) # course name
    # save the course info
    # keep course id handy
    course_page = requests.get(course.get("href"))
    course_soup = BeautifulSoup(course_page.content, "html.parser")
    session_links = course_soup.select("table.jxScheduleSortable tbody td a", limit=10)
    for link in session_links:
        # find each instructor (there are other links in here)
        if (link.get("href").startswith("https://www.pcc.edu/staff/directory/")):
            print(link.get("href")) # bio page url
            print(link.get_text()) # teacher name

    
    
        # save instructor info
        # save instroctor + class info





"""
output

teacher name

class name
school name
class url



"""