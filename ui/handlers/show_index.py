#import models.users_db as users_db
import jinja2
import base
from models import site_db
from models import member_db
from gaesessions import get_current_session
from workers.get_hash import get_hash

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login
from google.appengine.ext import db


TEMPLATE_URI = 'ui/templates/index.html'

class ShowIndex(base.RequestHandler):
    def get(self):
	#gql_string = 'SELECT * From Site'# WHERE status >= %s", where_string
	#q = db.GqlQuery(gql_string)
	#for site in q.run():
	  #db.delete(site.key())
        data = {
	  "show_banner": True,
	  "home_page_current": True,
	  "message": self.request.get("message"),
	  "logged_in": check_login(),
	}
	
	q = db.Query(member_db.Member)
	q.filter("email =", "admin@admin.com")
	admin_exists = q.get()
	
	if not admin_exists:
	  m = member_db.Member(email = "admin@admin.com", password_hash = get_hash("temporary_password"), permissions_list=["Administrator"])
	  m.put()
	  session=get_current_session()
	  session.clear()
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        