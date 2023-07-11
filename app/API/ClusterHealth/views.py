try:
    from Flask import Flask
    from Flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    print("Fully imported")
except Exception as e:
    print("Error: {}".format(e))

class HealthController(MethodResource, Resource):

    @doc(description='FlaskAPI Health Endpoint Here', tag=['Health Endpoint'])
    def get(self):



        return {'Returned message':  'API response'},200