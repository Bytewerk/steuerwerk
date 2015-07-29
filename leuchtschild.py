"""
The leuchtschild module allows control of the LED sign on the storefront.
"""

from steuerwerk import app, ctrl_funcs
from flask import render_template, request

class Pattern():
	def __init__(self, selected=False):
		self.selected = selected

patterns = {
	"eye cancer": Pattern(),
	"red green blue": Pattern(),
	"CSD": Pattern(),
	"in Farbe und bunt": Pattern()
}

patterns["CSD"].selected = True


ctrl_funcs["control Leuchtschild"] = "leuchtschild"
@app.route('/leuchtschild/',methods=["GET","POST"])
def show_sign():
	if request.form:
		pattern = request.form["pattern"]
		color = request.form["color"]
	return render_template("leuchtschild.html",patterns=patterns)

## TODO ##
# Indicate currently active pattern in web interface
# Give previews/descriptions of patterns
# process submitted values
