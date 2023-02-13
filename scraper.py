import requests
from bs4 import BeautifulSoup
import urllib.parse


class Teacher_Scraper:

    def __init__(self, listing_url, school_name):
        self.listing_url = listing_url
        self.school_name = school_name
        print(f"Scraping teachers for school: {self.school_name}")
        print(f"url: {self.listing_url}")

    def get_course_listings(self):
        page = requests.get(self.listing_url)
        soup = BeautifulSoup(page.content, "html.parser")
        course_list = soup.select("dl.course-list")
        self.course_links = course_list[0].find_all("a", limit=3) # limit to avoid a ton of traffic while figuring this out

    def get_info_from_listings(self):
        for course in self.course_links: 
            course_url = course.get("href") # markup specific
            course_name = course.get_text() # markup specific 
            course_page = requests.get(course_url)
            course_soup = BeautifulSoup(course_page.content, "html.parser")
            session_links = course_soup.select("table.jxScheduleSortable tbody td a", limit=4) # markup specific selector  
            for link in session_links:
                # find each instructor (there are other links in here)
                if (link.get("href").startswith("https://www.pcc.edu/staff/directory/")): # markup specific selector
                    print(link.get("href")) # bio page url
                    print(link.get_text()) # teacher name
                    print(f"https://google.com/search?q={urllib.parse.quote(link.get_text())}")
                    print(f"https://www.etsy.com/search_results_people.php?search_query={urllib.parse.quote(link.get_text())}")

    def print_course_listings(self):    
        print(f"Found {self.course_links} course listings")
        print(self.course_links)



if __name__ == "__main__": 
    url = "https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&topicid=ART"
    school_name = "Portland Community College"
    scraper = Teacher_Scraper(url, school_name)
    scraper.get_course_listings()
    scraper.print_course_listings()
    scraper.get_info_from_listings()
   

    
        # de duping would be nice
        # save instructor info
        # save instroctor + class info




"""
output json

{
    teacher_name : "person's name",
    listings : [
        {
            school : "name of school",
            bio_page : "teachers bio page at this school",
            teacher_email : "teacher@scholl.com",
            classes : [
                {
                    class_name: "name of class",
                    class_description: "description of class",
                    class_url: "class url"
                }
            ]
        }
    ]
}

teacher name

class name
school name
class url



"""