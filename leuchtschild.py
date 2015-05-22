"""
The leuchtschild module allows control of the LED sign on the storefront.
"""

from steuerwerk import app, ctrl_funcs
from flask import render_template

functions = {
	"select pattern": None,
	"set color": None
}

ctrl_funcs["control Leuchtschild"] = "leuchtschild"
@app.route('/leuchtschild/')
def show_sign():
	return render_template("leuchtschild.html",functions=functions)
