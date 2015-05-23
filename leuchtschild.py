"""
The leuchtschild module allows control of the LED sign on the storefront.
"""

from steuerwerk import app, ctrl_funcs
from flask import render_template

patterns = {
	"eye cancer": None,
	"red green blue": None,
	"CSD": None,
	"in Farbe und bunt": None
}

ctrl_funcs["control Leuchtschild"] = "leuchtschild"
@app.route('/leuchtschild/',methods=["GET","POST"])
def show_sign():
	return render_template("leuchtschild.html",patterns=patterns)

## TODO ##
# Indicate currently active pattern in web interface
# Give previews/descriptions of patterns
# process submitted values
