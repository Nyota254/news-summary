class News_source:
    '''
    Class for instantiating Source objects
    '''
    def __init__(self,name,description,category,url):
        '''
        Method for instantiating the movie variables
        '''
        self.name = name
        self.description = description
        self.category =category
        self.url = url

class News_article:
    '''
    Class for instantiating article objects
    '''

    def __init__(self,image,description,timecreated,articlelink):
        '''
        Method for instantiating article variables
        '''
        self.image = image
        self.description = description
        self.timecreated = timecreated
        self.articlelink = articlelink
