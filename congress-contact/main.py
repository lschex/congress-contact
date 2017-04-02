import webapp2
from google.appengine.ext import ndb
import logging
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class State(ndb.Model):
    state = ndb.StringProperty()
    name1 = ndb.StringProperty()
    party1 = ndb.StringProperty()
    address1 = ndb.StringProperty()
    phone1 = ndb.StringProperty()
    fax1 =ndb.StringProperty()
    name2 = ndb.StringProperty()
    party2 = ndb.StringProperty()
    address2 = ndb.StringProperty()
    phone2 = ndb.StringProperty()
    fax2 = ndb.StringProperty()
    stateCode = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template("index.html")
        self.response.write(template.render())
    def post(self):

        info = self.request.get('info')
        infoList = info.split(',')

        state = infoList[0]
        name1 = infoList[1]
        party1 = infoList[2]
        address1 = infoList[3]
        phone1 = infoList[4]
        fax1 = infoList[5]
        name2 = infoList[6]
        party2 = infoList[7]
        address2 = infoList[8]
        phone2 = infoList[9]
        fax2 = infoList[10]
        stateCode = infoList[11]

        state = State (state = state, name1 = name1, party1 = party1, address1 = address1, phone1 = phone1, fax1 = fax1, name2 = name2, party2 = party2, address2 = address2, phone2 = phone2, fax2 = fax2, stateCode = stateCode)

        state.put()


        template = jinja_environment.get_template("index.html")
        self.response.write(template.render())

        self.redirect('/')

class StateHandler(webapp2.RequestHandler):
    def get(self):
        tempCode = self.request.get('state')

        theState = State.query(State.stateCode == tempCode).fetch()



        template = jinja_environment.get_template("state.html")

        template_values = {'state': theState}
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
