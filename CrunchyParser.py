#The functions in this script parse parts of cruncyroll, for anime info
import selenium.webdriver
import selenium.common
import json

#Start our fake browser we will use to peruse crunchyroll
browser = selenium.webdriver.Firefox()

#Gets the "short descriptions" for the most recent episodes of popular anime
def getShortDescriptions(anime):
    #Make sure our anime name is correct
    anime_name = anime.lower().replace(' ','-')
    browser.get("https://www.crunchyroll.com/"+anime_name)
    #Diiig into the HTML for the description
    element = browser.find_element_by_tag_name('body')
    ids = ['template_scroller',
           'template_container',
           'template_body',
           'source_showview',
           'container',
           'main_content',
           'showview_content',
           'showview_content_videos']
    tags = ['ul',
            'li',
            'ul']
    try:
        for name in ids:
            element = element.find_element_by_id(name)
        for tag in tags:
            element = element.find_element_by_tag_name(tag)
        elements = element.find_elements_by_tag_name('script')
        json_descriptions = []
        for script in elements:
            data = script.get_attribute('innerHTML')
            json_start = data.index('{"')
            json_end   = json_start + data[json_start:].index('}')+1
            json_data  = json.loads(data[json_start:json_end])
            json_descriptions.append(json_data)
    except selenium.common.exceptions.NoSuchElementException:
        raise(ValueError('Could not find data for '+anime))
    
    return(json_descriptions)

def cleanup():
    browser.quit()
    
    
