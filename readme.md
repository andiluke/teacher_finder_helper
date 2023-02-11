purpose:

scrape class listings to create a db of art teachers for further processing


mongo notes:
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

running as a service 
 
to see if its running:
$ brew services list

to start as a service:
brew services start mongodb-community@6.0

to stop service:
brew services stop mongodb-community@6.0

connect & use:
$ mongosh

commands:
https://www.mongodb.com/docs/mongodb-shell/crud/

database: teachers


python venv
https://realpython.com/python-virtual-environments-a-primer/

~/Documents/projects/art_guild/scraper

$ source venv/bin/activate
$ …
$ deactivate