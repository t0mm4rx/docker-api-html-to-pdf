from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
import subprocess
import hashlib
from datetime import datetime
import os

class PDF(Resource):

	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument("url", required=True)
		parser.add_argument("args", required=False)
		args = parser.parse_args()

		if (not args['args']):
			args['args'] = ""

		now = datetime.now()
		filename = hashlib.md5(str.encode(f"{args['url']}-{now.month}-{now.year}")).hexdigest() + ".pdf"

		if (not os.path.isfile(filename)):
			job = subprocess.Popen(f"wkhtmltopdf {args['args']} {args['url']} {filename}", shell=True)
			job.wait()

		return send_from_directory("./", filename)

app = Flask(__name__)
api = Api(app)

api.add_resource(PDF, "/pdf")

app.run()