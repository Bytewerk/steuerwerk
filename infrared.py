"""
The infrared module allows control of an infrared transmitter at the Bytewerk,
which in turn gives control over the amplifier, the video projector, etc…
"""

from flask import render_template, request
from steuerwerk import app, ctrl_funcs
#import requests
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
@app.route('/ir/<device>', methods=['POST'])
def show_ir(device=None):
    if request.form and device:
        name = request.form['cmd']
        cmd = devices[device]["commands"][name]
        prot = devices[device]["prot"]
        send_cmd(prot,cmd)
    return render_template("ir.html", devices = devices_raw)

def send_cmd(prot,cmd):
    """ Send the specified infrared command. """
    with socket.create_connection(("ir.bingo",2701)) as sock:
        cmd_str = "irmp send {} {} 00\n".format(prot,cmd)
        sock.send(bytes(cmd_str,"utf-8"))
    #r = requests.get("http://ir.bingo/ecmd?irmp send {} {} 00".format(prot,cmd))
    #print(r.url)
    #print("\033[32m>>> DEBUG\033[39m: command {} requested to be sent".format(cmd))
