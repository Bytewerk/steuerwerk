"""
The infrared module allows control of an infrared transmitter at the Bytewerk,
which in turn gives control over the amplifier, the video projector, etc…
"""

from flask import render_template, request
from bhbctrl import app, ctrl_funcs
import requests
import json

CMDS_FILE = "ircodes.json"
devices = None
with open(CMDS_FILE) as cmds_file:
    devices = json.load(cmds_file)

ctrl_funcs["send ir commands"] = "ir"
@app.route('/ir/', methods=['GET'])
@app.route('/ir/<device>', methods=['POST'])
def show_ir(device=None):
    if request.form and device:
        name = request.form['cmd']
        cmd = devices[device]["commands"][name]
        prot = devices[device]["prot"]
        send_cmd(prot,cmd)
    return render_template("ir.html", devices = devices)

def send_cmd(prot,cmd):
    """ Send the specified infrared command. """
    r = requests.get("http://ir.bingo/ecmd?irmp send {} {} 00".format(prot,cmd))
    #print(r.url)
    #print("\033[32m>>> DEBUG\033[39m: command {} requested to be sent".format(cmd))
