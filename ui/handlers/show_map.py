import jinja2
import base

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path as get_template_path
from google.appengine.ext import db


TEMPLATE_URI = 'ui/templates/map.html'
LEAFLET_TEMPLATE_URL = 'map/templates/leaflet_map.html'
class ShowMap(base.RequestHandler):
    def get(self, region):
	gql_string = 'SELECT * From AgeGroup'# WHERE status >= %s", where_string
	q = db.GqlQuery(gql_string)
	age_groups=q.run()
	gql_string = 'SELECT * From ProgramType'# WHERE status >= %s", where_string
	q = db.GqlQuery(gql_string)
	program_types = q.run()
	
	data = {
            "leaflet_map": template.render(get_template_path(LEAFLET_TEMPLATE_URL), {}),
            "map_page_current": True,
            "message": self.request.get("message"),
            "age_groups": age_groups,
            "program_types": program_types,
        }
        self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
        