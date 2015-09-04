"""
The infrared module allows control of an infrared transmitter at the Bytewerk,
which in turn gives control over the amplifier, the video projector, etc…
"""

from flask import render_template, request
from steuerwerk import app, ctrl_funcs
import socket
import json
import collections
import time
import traceback
import sys

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
        else:
            send_cmds(prot,cmd)
    return render_template("ir.html", devices = devices_raw)

def make_it_so():
    dev = devices["Amplifier"]
    prot = dev["prot"]
    cmds = dev["commands"]
    send_cmds(prot, cmds["ON/OFF"], *[cmds["VOLUME UP"]]*15)
    send_cmds(prot, cmds["DVD"])


COMMAND_TIMEOUT = 0.1 #timeout between actual sent IR commands
RECONNECTION_TIMEOUT = 1 #timeout between reconnections of the socket to the IR interface
RECONNECTION_ATTEMPTS = 3 #how many times to attempt connection to infrared board before giving up and clearing the queue
socket.setdefaulttimeout(RECONNECTION_TIMEOUT) # set timeout for new socket objects
ECMD_HOST = "ir.bingo"
ECMD_PORT = 2701

def send_cmds(prot,*cmds):
    """ Send the specified infrared commands. """
    sock = None
    for i in range(RECONNECTION_ATTEMPTS):
        try:
            sock = socket.create_connection((ECMD_HOST,ECMD_PORT),RECONNECTION_TIMEOUT)
        except:
            traceback.print_exc(file=sys.stderr)
            time.sleep(RECONNECTION_TIMEOUT)
    for cmd in cmds:
        cmd_str = "irmp send {} {} 00\n".format(prot,cmd)
        sock.send(bytes(cmd_str,"utf-8"))
        time.sleep(COMMAND_TIMEOUT)
