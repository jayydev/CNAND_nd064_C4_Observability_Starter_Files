#import logging
#import re
import requests

from flask_opentracing import FlaskTracing
from jaeger_client import Config
#from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
#from opentelemetry.instrumentation.flask import FlaskInstrumentor
#from opentelemetry.instrumentation.requests import RequestsInstrumentor
#from prometheus_flask_exporter import PrometheusMetrics

from flask import Flask, render_template, request, jsonify

#import pymongo
#from flask_pymongo import PyMongo

app = Flask(__name__)

#FlaskInstrumentor().instrument_app(app)
#RequestsInstrumentor().instrument()

#metrics = PrometheusMetrics(app)
# static information as metric
#metrics.info("app_info", "Application info", version="1.0.3")

#logging.getLogger("").handlers = []
#logging.basicConfig(format="%(message)s", level=logging.DEBUG)
#logger = logging.getLogger(__name__)


#app.config["MONGO_DBNAME"] = "example-mongodb"
#app.config[
#    "MONGO_URI"
#] = "mongodb://my-user:PHlvdXItcGFzc3dvcmQtaGVyZT4=@example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

#mongo = PyMongo(app)


#def init_tracer(service):

config = Config(
    config={
        "sampler": 
        {"type": "const", 
        "param": 1},
        "logging": True,
        "reporter_batch_size": 1,
            #'local_agent': {
            #    'reporting_host': '127.0.0.1',
            #    'reporting_port': '5775',
            #}
        },
        service_name="backend",
        #validate=True,
        #metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
 #   return config.initialize_tracer()


tracer = config.initialize_tracer()
#init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)

home_api_count = 0


@app.route("/")
def homepage():
    parent_span = flask_tracer.get_span()
    with tracer.start_span("homepage", child_of=parent_span) as span:
        answer = "Hello World"
        global home_api_count
        home_api_count += 1
        span.log_kv({"event": "homepage", "home_api_count": home_api_count})
        return answer


@app.route("/api")
def my_api():
    parent_span = flask_tracer.get_span()
    with tracer.start_span("my_api", child_of=parent_span) as span:
        answer = "something"
        span.log_kv({"api":"api invoked"})
        return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    parent_span = flask_tracer.get_span()
    #star = mongo.db.stars
    with tracer.start_span("star", child_of=parent_span) as span:
        name = request.json["name"]
        distance = request.json["distance"]
        span.log_kv({"event": "add_star", "name": name, "distance": distance})

        with tracer.start_span("name-distance", child_of=span) as db_span:
            #star_id = star.insert({"name": name, "distance": distance})
            new_star = f"""name_{name}_distance_{distance}"""
            #star.find_one({"_id": star_id})
            db_span.log_kv(
                {"name": name, "distance": distance, "new_star_id": id})
            output = new_star #{"name": new_star["name"], "distance": new_star["distance"]}
            answer = jsonify({"result": output})
            span.set_tag("answer", answer)
            return answer


if __name__ == "__main__":
    app.run()
