from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# Flask config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def show_index():
    """ Show an index of available bhbctrl functionality. """
    strings = {"appname": "bhbctrl"}
    return render_template("index.html", **strings)

if __name__ == "__main__":
    app.run()
