import os
import datetime
import urllib
from google.appengine.ext import db
from google.appengine.api import users

class Site(db.Expando):
    name = db.StringProperty(required=True)
    address = db.StringProperty(required=True)
    latitude = db.FloatProperty(required=True)
    longitude =db.FloatProperty(required=True)
    region = db.StringProperty(required=True)
    #city = db.StringProperty()
    #state = db.StringProperty()
    #country = db.StringProperty()
    #notes = db.TextProperty()
    #website = db.StringProperty()
    #email = db.StringProperty()
    #phone1 = db.StringProperty()
    #phone2  = db.StringProperty()
    
    
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
    