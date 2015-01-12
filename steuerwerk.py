from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# Flask config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

ctrl_funcs = {}

@app.route('/')
def show_index():
    """ Show an index of available steuerwerk functionality. """
    return render_template("index.html", appname="steuerwerk", ctrl_funcs=ctrl_funcs)

from infrared import *

if __name__ == "__main__":
    app.run()
