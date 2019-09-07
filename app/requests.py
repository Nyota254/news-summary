from .models import News_article,News_source
import urllib.request,json

api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    This function gets json response from the news site
    '''

    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response ['sources']:
            sources_result_list = get_sources_response['sources']
            sources_results = process_results(sources_result_list)

    return sources_results

def process_results(sources_list):
    '''
    Functions that takes in list of sources results and transforms them into objects
    '''
    source_list = []
    for source_item in sources_list:
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        url = source_item.get('url')

        source_object = News_source(name,description,category,url)
        source_list.append(source_object)
    
    return source_list

