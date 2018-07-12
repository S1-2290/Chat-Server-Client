import os
import sys
import re
import socket
from modules.colors import *
from modules.utils import Utils

# -- Client - v1.0

# --------------------------------------------------------------------
# Variables - Colors
gs = Colors.GREEN
rs = Colors.RED
ys = Colors.YELLOW
blue = Colors.BLUE
ce = Colors.COLOR_END
# -> Patterns
plus = Patterns.PLUS
minus = Patterns.MINUS
astk = Patterns.ASTK


# --------------------------------------------------------------------
"""
Get input for:
- IP Address
- Port number
"""
try:
    hostname = raw_input(ys + "Enter IP Address: " + ce)
    # Check input
    Utils.check_ip_address_input(str(hostname))
    pass
except KeyboardInterrupt:
    Utils.print_exit_message_simple()
    sys.exit(1)

try:
    port_number = raw_input(ys + "Enter port number (1-65,535): " + ce)
    # Check input
    Utils.check_port_number_input(int(port_number))
    pass
except KeyboardInterrupt:
    Utils.print_exit_message_simple()
    sys.exit(1)
# ---------------------------------------------------------------------
"""
Init the socket variable
- Apply AF_INET
- Apply SOCK_STREAM
"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ---------------------------------------------------------------------
# Connect client to server
print astk + gs + "Attempting to connect to the server..." + ce
try:
    client.connect((str(hostname), int(port_number)))
    print astk + gs + "Connection successful..." + ce
    print astk + gs + "Connected to: " + ce + Colors.WHITE + hostname + ce
    pass
except socket.error as e:
    print rs + "Error: " + ce + Colors.WHITE + str(e) + ce
    Utils.print_exit_message_simple()
    sys.exit(1)
# ---------------------------------------------------------------------
# Enter main command line
print astk + gs + "Entering main client command line..." + ce + '\n'
while True:
    try:
        cmd = raw_input(ys + "client" + ce + Colors.WHITE + ':' + ce + ys + hostname + '> ' + ce)
        client.send(cmd)
        # ------------------------------------------------------------------
        # Client commands

        # ------------------------------------------------------------------
    except KeyboardInterrupt:
        print '\n'
        Utils.print_exit_message_simple()
        sys.exit(1)
    # Wait for the server to respond
    print '\n' + ys + ">> " + ce + Colors.WHITE + "Waiting for the server to respond..." + ce + '\n'
    print ys + "[ " + ce + Colors.WHITE + "SERVER" + ce + ys + " ]: " + ce + Colors.WHITE, client.recv(4080), ce
