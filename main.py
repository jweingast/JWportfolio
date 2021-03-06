#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

JINJA_ENVIRONMENT= jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	if self.request.path == '/home.html':
        	dic = {
        		'title': 'Home',
        		'header': 'Welcome',
        		'path': self.request.path
        	}
        elif self.request.path == '/personal.html':
        	dic = {
        		'title': 'Personal',
        		'header': 'Personal',
        		'path': self.request.path
        	}

        elif self.request.path == '/resume.html':
        	dic = {
        		'title': 'Family',
        		'header': 'Family',
        		'path': self.request.path
        	}
        elif self.request.path == '/contact.html':
            dic = {
                'title': 'Contact',
                'header': 'Family',
                'path': self.request.path
            }
        else:
        	self.response.write(template.render('This should not occur'))
        	return

        template = JINJA_ENVIRONMENT.get_template('templates' + self.request.path)
    	self.response.write(template.render(dic))


class HomeHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("asdf")
		template=JINJA_ENVIRONMENT.get_template('templates/home.html')
		dic= {
			'title':'Home',
			'header':'Welcome',
			'path':'/home.html'
			}
		self.response.write(template.render(dic))
		
app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/home.html', MainHandler),
    ('/personal.html',MainHandler),
    ('/resume.html',MainHandler),
    ('/contact.html',MainHandler),
], debug = True)