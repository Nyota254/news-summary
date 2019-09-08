# News Highlight
#### Web app that shows various news sources and shows a user articles written from the sources, 8-Sep-2019
#### By **Kingecha Kevin Nyota**
## Link to live site
https://news-summary.herokuapp.com

## Description
This is a web based site that takes various news sources and displays them to a user. a user can then navigate to view the various articles written by the site.The main reoson behind its creation is to allow users to catch up on the latest news
## User Stories
- [x] User can see various news sources on the homepage of the application.
- [x] User can select a news source and see all news articles from the selected news source in the application.
- [x] User can see the image, description and the time a news article was created.
- [x] User can click on an article and read the full article on the source website.  

## Setup/Installation Requirements
* Ensure that Python is installed on your machine if not please visit the python website and download the latest version python 3.6
* Fork the repository and either download the project or clone it to your machine
* Navigate to the newsapi site here -> https://newsapi.org and register for an api key
* Register the api key as an environment variable in your terminal as follows
```
export NEWS_API_KEY=<your-api-key>
```
* run the application from your terminal using the following command
```
python3.6 manage.py server
```
* To edit the code if you will need any dependancys you will need to navigate to the virtual environment in order to install them from there to avoid version conflicts
```
source virtualenv/bin/activate
```
## Known Bugs
There are no known bug if any dont hesitate to contact me
## Technologies Used
1. Python Version 3.6
2. Flask Framework
3. Html
4. Bootstrap
5. Css
## Support and contact details
if you run into any issues please contact knyota66@gmail.com
### License
*MIT*
Copyright (c) 2019 **Kingecha Kevin Nyota**