import flask
import os
from db import get_all_events, get_event_by_id, search_events

folder = os.getcwd()
app = flask.Flask(__name__, template_folder=folder, static_folder=folder)
app.config["SECRET_KEY"] = "my_secret_key"


@app.route("/")
def index():
    events = get_all_events()
    return flask.render_template("index.html", events=events)


@app.route("/event/<int:event_id>")
def event(event_id):
    event = get_event_by_id(event_id)
    return flask.render_template("event.html", event=event)


@app.route("/search")
def search_page():
    query = flask.request.args.get("query")
    events = search_events(query)  # множина — список подій
    return flask.render_template("index.html", events=events)


if __name__ == "__main__":
    app.run(debug=True)