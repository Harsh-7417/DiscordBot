from googleapiclient.discovery import build
import os
from dotenv import load_dotenv


project_folder = os.path.expanduser('~/Desktop/DiscordBOT')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


def google_search(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=os.getenv('API_KEY'))
    res = service.cse().list(q=search_term, cx=os.getenv('CSE_ID'), num=5,**kwargs).execute()
    webhook_urls =[search['link'] for search in res['items']]
    return "\n".join(webhook_urls)

def welcome_user(user, **kwargs):
    return "Hello "+str(user) + """\n I am running with limited capabilities, but still I can do google search for you.\n!google <what you are looking for>"""

def recent_search():
    pass







