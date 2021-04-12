from googleapiclient.discovery import build
import config # module maintaining DB connection(s) and env specific info
import os

__db_cxn = config.load_db_configuration()  # private mongo DB connection


def google_search(search_filter, **kwargs):
    """custom google search API to return top 5 search links"""
    if search_filter:
        service = build("customsearch", "v1", developerKey=os.getenv('API_KEY'))
        res = service.cse().list(q=search_filter, cx=os.getenv('CSE_ID'), num=5, **kwargs).execute()
        urls = [search['link'] for search in res['items']]
        return "\n".join(urls)
    return "OOPS! Seems like you haven't passed enough information to search. HINT : !google <text to search> "


def welcome_user(user, **kwargs):
    """Custom method to maintain welcome message for a user"""
    return "Hello " + user + """
I am running with limited capabilities, but still I can do google search for you.
HINT : !google <text to search>
HINT : !recent <text to search in history>"""


def add_history(user_id, search_filter, **kwargs):
    """To add search history of a user in Mongo DB"""
    __db_cxn.insert_one({"user_id": user_id, "search": search_filter.lower()})


def recent_search(user_id, search_filter):
    """To get search history of a user matching search_filter condition"""
    search_history = __db_cxn.find({"user_id": user_id, 'search': {'$regex': search_filter.lower()}}).distinct('search')
    if search_history:
        return "\n".join(search_history)
    return f"Seems like you haven't searched anything related to {search_filter}. HINT : !google <text to search>"
