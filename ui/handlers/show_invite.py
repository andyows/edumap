import jinja2
import base
from models import invite_db
from workers.get_hash import get_hash
from workers.send_invite import send_invite
from gaesessions import get_current_session
import settings

from google.appengine.ext.webapp import template
from workers.get_template_path import get_template_path
from workers.check_login import check_login
from google.appengine.api import users
from google.appengine.ext import db



TEMPLATE_URI = 'ui/templates/invite.html'
class ShowInvite(base.RequestHandler):
  def get(self):
    
    session = get_current_session()
    try:
      email = session['email']
      permissions_list = session['permissions_list']
    except:
      self.redirect("/authentication?destination=/invite")
      return
      
      
    if not email and permissions_list:
      self.redirect("/authentication?destination=/invite")
      return
      
    if not any("Administrator" in s for s in permissions_list):
      self.redirect("/authentication?destination=/invite&message=You do not have permission to view this page, if this is in error contact us")
      return

    login_url = users.create_login_url("/invite")
    user = users.get_current_user()
    

    if not user:
      self.response.out.write("<a href='%s'>Log in via google</a>" % login_url)
      return
    data = {
      "message": self.request.get("message"),
      "permission_dict": settings.PERMISSIONS_DICT,
      "logged_in": check_login(),
    }
    self.response.out.write(template.render(get_template_path(TEMPLATE_URI), data))         
      
  def post(self):
    # validate form
    email = self.request.get("email")
    confirm_email = self.request.get("confirm_email")
    permission = self.request.get("permission")
    if not permission:
      self.redirect("/invite?message=must specify which permission you are allowing the user.")
      return
    invite_hash = self.request.get("invite_hash")
    if not email == confirm_email:
      self.redirect("/invite?message=email and confirm email were not identical, please try again")
      return
      
    q = db.Query(invite_db.Invite)
    q.filter("email =", email)
    existing_invite = q.get()
    if existing_invite:
      db.delete(existing_invite.key())
      
      
    invite_hash = get_hash()

    i = invite_db.Invite(email = email, invite_hash = invite_hash, permission = permission)
    i.put()
    
    
    email_sucessful_boolean = send_invite(email, invite_hash)
    if not email_sucessful_boolean:
      self.redirect("/invite?message=There was an error sending email, please email us and let us know")
      return

    
    self.redirect("/invite?message=Invite sent to " + email)


      
         