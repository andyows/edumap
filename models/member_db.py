import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users

class Member(db.Expando):
    email = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    # List of the different permissions a user will have
    # For instance, Admin. Or import_csv
    permissions_list = db.StringListProperty(required=True)
    
    
    def getAllCached():
        pass
    
    def getCachedById():
        pass
    
    def putAndCache():
        pass
    
    def importCSV():
        pass
    
    def deleteAndResetCache():
        # delete from cache and save new cache to db
        pass
    