# mpcs_app.py
#
# Copyright (C) 2011-2017 Vas Vasiliadis
# University of Chicago
#
# Application logic for the GAS
#
##
__author__ = 'Vas Vasiliadis <vas@uchicago.edu>'

import base64
import datetime
import hashlib
import hmac
import json
import sha
import string
import time
import urllib
import urlparse
import uuid
import boto3
import botocore.session
from boto3.dynamodb.conditions import Key

from mpcs_utils import log, auth
from bottle import route, request, redirect, template, static_file

'''
*******************************************************************************
Set up static resource handler - DO NOT CHANGE THIS METHOD IN ANY WAY
*******************************************************************************
'''
@route('/static/<filename:path>', method='GET', name="static")
def serve_static(filename):
  # Tell Bottle where static files should be served from
  return static_file(filename, root=request.app.config['mpcs.env.static_root'])

'''
*******************************************************************************
Home page
*******************************************************************************
'''
@route('/', method='GET', name="home")
def home_page():
	log.info(request.url)
	return template(request.app.config['mpcs.env.templates'] + 'home', auth=auth)

'''
*******************************************************************************
Registration form
*******************************************************************************
'''
@route('/register', method='GET', name="register")
def register():
	log.info(request.url)
	return template(request.app.config['mpcs.env.templates'] + 'register',
		auth=auth, name="", email="", username="", 
		alert=False, success=True, error_message=None)

@route('/register', method='POST', name="register_submit")
def register_submit():
	try:
		auth.register(description=request.POST.get('name').strip(),
									username=request.POST.get('username').strip(),
									password=request.POST.get('password').strip(),
									email_addr=request.POST.get('email_address').strip(),
									role="free_user")
	except Exception, error:
		return template(request.app.config['mpcs.env.templates'] + 'register', 
			auth=auth, alert=True, success=False, error_message=error)	

	return template(request.app.config['mpcs.env.templates'] + 'register', 
		auth=auth, alert=True, success=True, error_message=None)

@route('/register/<reg_code>', method='GET', name="register_confirm")
def register_confirm(reg_code):
	log.info(request.url)
	try:
		auth.validate_registration(reg_code)
	except Exception, error:
		return template(request.app.config['mpcs.env.templates'] + 'register_confirm',
			auth=auth, success=False, error_message=error)

	return template(request.app.config['mpcs.env.templates'] + 'register_confirm',
		auth=auth, success=True, error_message=None)

'''
*******************************************************************************
Login, logout, and password reset forms
*******************************************************************************
'''
@route('/login', method='GET', name="login")
def login():
	log.info(request.url)
	redirect_url = "/annotations"
	# If the user is trying to access a protected URL, go there after auhtenticating
	if request.query.redirect_url.strip() != "":
		redirect_url = request.query.redirect_url

	return template(request.app.config['mpcs.env.templates'] + 'login', 
		auth=auth, redirect_url=redirect_url, alert=False)

@route('/login', method='POST', name="login_submit")
def login_submit():
	auth.login(request.POST.get('username'),
						 request.POST.get('password'),
						 success_redirect=request.POST.get('redirect_url'),
						 fail_redirect='/login')

@route('/logout', method='GET', name="logout")
def logout():
	log.info(request.url)
	auth.logout(success_redirect='/login')


'''
*******************************************************************************
*
CORE APPLICATION CODE IS BELOW...
*
*******************************************************************************
'''

'''
*******************************************************************************
Subscription management handlers
*******************************************************************************
'''
import stripe

# Display form to get subscriber credit card info
@route('/subscribe', method='GET', name="subscribe")
def subscribe():
  pass

# Process the subscription request
@route('/subscribe', method='POST', name="subscribe_submit")
def subscribe_submit():
  pass


'''
*******************************************************************************
Display the user's profile with subscription link for Free users
*******************************************************************************
'''
@route('/profile', method='GET', name="profile")
def user_profile():
  pass


'''
*******************************************************************************
Creates the necessary AWS S3 policy document and renders a form for
uploading an input file using the policy document
*******************************************************************************
'''
@route('/annotate', method='GET', name="annotate")
def upload_input_file():
  pass


'''
*******************************************************************************
Accepts the S3 redirect GET request, parses it to extract 
required info, saves a job item to the database, and then
publishes a notification for the annotator service.
*******************************************************************************
'''
@route('/annotate/job', method='GET')
def create_annotation_job_request():
  pass


'''
*******************************************************************************
List all annotations for the user
*******************************************************************************
'''
@route('/annotations', method='GET', name="annotations_list")
def get_annotations_list():
  pass


'''
*******************************************************************************
Display details of a specific annotation job
*******************************************************************************
'''
@route('/annotations/<job_id>', method='GET', name="annotation_details")
def get_annotation_details(job_id):
  pass


'''
*******************************************************************************
Display the log file for an annotation job
*******************************************************************************
'''
@route('/annotations/<job_id>/log', method='GET', name="annotation_log")
def view_annotation_log(job_id):
  pass


### EOF