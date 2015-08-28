"""
The leuchtschild module allows control of the LED sign on the storefront.
"""

from steuerwerk import app, ctrl_funcs
from flask import render_template, request

class Pattern():
	def __init__(self):
		pass

patterns = {
	"eye cancer": Pattern(),
	"red green blue": Pattern(),
	"CSD": Pattern(),
	"in Farbe und bunt": Pattern(),
	"custom color": Pattern()
}

active_pattern = "CSD"
custom_color = 0x0

ctrl_funcs["control Leuchtschild"] = "leuchtschild"
@app.route('/leuchtschild/',methods=["GET","POST"])
def show_sign():
	global active_pattern
	print(active_pattern)
	if request.form:
		active_pattern = request.form["pattern"]
		print("new pattern: ",active_pattern)
		global custom_color
		custom_color = request.form["color"]
	return render_template("leuchtschild.html",patterns=patterns,custom_color=custom_color, active_pattern = active_pattern)

## TODO ##
# Indicate currently active pattern in web interface
# Give previews/descriptions of patterns
# process submitted values
