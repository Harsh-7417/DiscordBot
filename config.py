import os
from dotenv import load_dotenv
from pymongo import MongoClient
"""import logging #Can log information as well if required"""

"""load env file"""
project_folder = os.path.expanduser('~/Desktop/DiscordBOT')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


def load_db_configuration():
    """To connect & return MongoDB collection instance"""
    cluster = MongoClient(os.getenv('DB_URL'))
    db = cluster[os.getenv('DB_NAME')]
    collection = db[os.getenv('Collection')]
    return collection
