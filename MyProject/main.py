#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I update automatically pankaj git next level 45')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)