#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self, path):
        self.redirect("https://www.rohitagarwal.org/" + path, code=301)

app = webapp2.WSGIApplication([
    ('/(.*)', MainHandler),
], debug=False)
