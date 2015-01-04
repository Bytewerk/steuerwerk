"""
The infrared module allows control of an infrared transmitter at the Bytewerk,
which in turn gives control over the amplifier, the video projector, etc…
"""

from bhbctrl import app, ctrl_funcs

ctrl_funcs["send ir commands"] = "ir"
@app.route('/ir')
def show_ir():
    return "hello IR"
