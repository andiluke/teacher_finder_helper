import requests
from bs4 import BeautifulSoup

url = "https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&topicid=ART"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
course_list = soup.select("dl.course-list a")
print(course_list)
print(type(course_list))
#course_list.find_all("a")


# for each course name listed 
    # save the course info
    # keep course id handy

    # find each instructor
        # save instructor info
        # save instroctor + class info





"""
output

teacher name

class name
school name
class url



"""