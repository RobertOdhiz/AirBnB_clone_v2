#!/usr/bin/python3
"""Flask framework"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown db"""
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ list of state ids"""
    data = storage.all(State)
    return render_template('7-states_list.html', total=data.values())


@app.route("/cities_by_states", strict_slashes=False)
def route_city():
        pep_fix = models.dummy_classes["State"]
        data = models.storage.all(cls=pep_fix)
        states = data.values()
        return render_template('8-cities_by_states.html', states_list=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
