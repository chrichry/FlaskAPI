try:
    from Flask import Flask
    from Flask_restful import Resource, Api
    from apispec import APISpec
    from marshmallow import Schema, fields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs
    from API.clusteHealth.views import HealthController

except Exception as e:
    print("_init_ Failed -> ".format(e))

app = Flask(__name__)
api = Api(app)
app.confg.update({
    'APISPEC_SPEC': APISpec(
        title='FlaskAPI',
        version='v1',
        plugins=[MarshmallowPlugin()],
        apenapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
})
docs = FlaskApiSpec(app)