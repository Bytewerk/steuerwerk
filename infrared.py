"""
The infrared module allows control of an infrared transmitter at the Bytewerk,
which in turn gives control over the amplifier, the video projector, etc…
"""

from flask import render_template, request
from steuerwerk import app, ctrl_funcs
import socket
import json
import collections

CMDS_FILE = "ircodes.json"
devices = None
with open(CMDS_FILE) as cmds_file:
    devices_raw = json.load(cmds_file, object_pairs_hook=collections.OrderedDict)

    # flatten the multiple command dictionaries for every device into one
    devices = {}
    for key in devices_raw.keys():
        devices[key] = {}
        devices[key]["commands"] = {}
        devices[key]["prot"] = devices_raw[key]["prot"]
        for cmds in devices_raw[key]["commands"]:
            devices[key]["commands"].update(cmds.items())

ctrl_funcs["send ir commands"] = "ir"
@app.route('/ir/', methods=['GET'])
@app.route('/ir/<device>', methods=['GET','POST'])
def show_ir(device=None):
    if request.form and device:
        name = request.form['cmd']
        cmd = devices[device]["commands"][name]
        prot = devices[device]["prot"]
        if name == "MAKE IT SO":
            make_it_so()
        send_cmd(prot,cmd)
    return render_template("ir.html", devices = devices_raw)

def make_it_so():
    dev = devices["Amplifier"]
    prot = dev["prot"]
    cmds = dev["commands"]
    send_cmd(prot, cmds["ON/OFF"])
    send_cmd(prot, cmds["DVD"])
    for i in range(15):
        send_cmd(prot, cmds["VOLUME UP"])

def send_cmd(prot,cmd):
    """ Send the specified infrared command. """
    with socket.create_connection(("ir.bingo",2701)) as sock:
        cmd_str = "irmp send {} {} 00\n".format(prot,cmd)
        sock.send(bytes(cmd_str,"utf-8"))
