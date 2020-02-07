import string
import cgi

from flask import Flask, render_template, request
app = Flask(__name__)

if __name__ == '__main__':
	app.run(ssl_context='adhoc')
