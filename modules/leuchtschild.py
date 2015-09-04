"""
The leuchtschild module allows control of the LED sign on the storefront.
"""

from steuerwerk import app, ctrl_funcs
from flask import render_template, request

patterns = {
	0: "led_clear",
	1: "fading",
	2: "fading_kitsch",
	-1: "custom color"
}

active_pattern = 0
custom_color = 0x0

ctrl_funcs["control Leuchtschild"] = "leuchtschild"
@app.route('/leuchtschild/',methods=["GET","POST"])
def show_sign():
	global active_pattern
	print(active_pattern)
	if request.form:
		active_pattern = int(request.form["pattern"])
		print("new pattern: ",active_pattern)
		global custom_color
		custom_color = request.form["color"]
	return render_template("leuchtschild.html",patterns=patterns,custom_color=custom_color, active_pattern = active_pattern)
