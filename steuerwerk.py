from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('STEUERWERK_CFG', silent=True)

ctrl_funcs = {}

@app.route('/')
def show_index():
    """ Show an index of available steuerwerk functionality. """
    return render_template("index.html", appname="steuerwerk", ctrl_funcs=ctrl_funcs)

from modules.infrared import *
from modules.leuchtschild import *

if __name__ == "__main__":
    app.run()
