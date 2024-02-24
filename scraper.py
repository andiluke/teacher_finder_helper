import requests
from bs4 import BeautifulSoup
import urllib.parse
from dbtest import *


class Teacher_Scraper:

    def __init__(self, listing_url, school_name):
        self.listing_url = listing_url
        self.school_name = school_name
        self.db = get_database()
        self.collection = self.db['teachers']
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
                    #print(f"https://google.com/search?q={urllib.parse.quote(link.get_text())}")
                    #print(f"https://www.etsy.com/search_results_people.php?search_query={urllib.parse.quote(link.get_text())}")
                    data_to_store = {
                        'teacher_name': link.get_text(),
                        'school_name': self.school_name,
                        'teacher_page': link.get("href"),
                        'teacher_email': 'email goes here',
                        'course_name': course_name
                    }
                    self.save_data(data_to_store)

    def save_data(self, data):
        print(data['teacher_name'])

        # add the teacher
        self.collection.update_one(
            {
                'teacher_name': data['teacher_name']
            },
            {
                '$set': {
                    'teacher_name': data['teacher_name']
                }
            },
        
            upsert=True
        )
        # add the school info
        self.collection.update_one(
            {
                'teacher_name': data['teacher_name']
            },
            {
                '$addToSet' : {
                    'listings.$[]': { 
                        'school_name': data['school_name'],
                        'teacher_page': data['teacher_page'],
                        'teacher_email': data['teacher_email'],
                    }
                }
            },
            #{
            #    arrayFilters: [
            #        {}
            #    ]
            #},
            upsert=True
        )
        ## add the course info
        #self.collection.update_one(
        #    {
        #        'teacher_name': data['teacher_name'],
        #        'listings.school_name': data['school_name']
        #    },
        #    {
        #        '$addToSet': {
        #            'listings.$.courses': {
        #                'course_name': data['course_name']
        #            }
        #        }
        #    },
        #    upsert=True)                

    def clear_records(self):
        print("Delete all records")
        self.collection.delete_many({})

    def print_course_listings(self):    
        print(f"Found {self.course_links} course listings")
        print(self.course_links)

    def print_db_listings(self):
        for listing in self.collection.find():
            print(listing)


if __name__ == "__main__": 
    url = "https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&topicid=ART"
    school_name = "PDX Community College"
    scraper = Teacher_Scraper(url, school_name)
    scraper.clear_records()
    scraper.get_course_listings()
    scraper.print_course_listings()
    scraper.get_info_from_listings()
    scraper.print_db_listings()
   

    
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
            courses : [
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