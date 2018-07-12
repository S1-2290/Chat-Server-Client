import os
import sys
import re
import socket
import cPickle as pickle
from modules.colors import *
from modules.utils import Utils
from modules.utils import Connect
from modules.config import MainConfigBinary

## Server script - Version: 1.0 ##

# ---------------------------------------------------------------------------------
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

# Classes
cnf_bin = MainConfigBinary()

# ---------------------------------------------------------------------------------
# Load the data

# ---------------------------------------------------------------------------------
"""
Init socket variable
- Apply AF_INET
- Apply SOCK_STREAM
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
Get input for:
- IP Address
- Port number
- Check inputs
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

try:
    noc = raw_input(ys + "Number of connections: " + ce)
    pass
except KeyboardInterrupt:
    Utils.print_exit_message_simple()
    sys.exit(1)
# ----------------------------------------------------------------------------------
# Bind the socket to the ip and port
connection = Connect(server, str(hostname), int(port_number))
connection.connect()
# ----------------------------------------------------------------------------------
# Set the number of connections to listen for
server.listen(int(noc))
s = None
# ----------------------------------------------------------------------------------
# Main command line
print astk + gs + "Enter command line..." + ce
# ----------------------------------------------------------------------------------
# Add data to the config list
print ys + ">>> " + ce + ys + "Updating information..." + ce
Utils.add_host_to_list(str(hostname))
Utils.add_port_to_list(int(port_number))
# ----------------------------------------------------------------------------------
while True:
    if s is None:
        # Waits for a connection
        print astk + gs + "Main loop entered..." + ce
        print astk + gs + "Waiting for connections..." + ce
        try:
            s, address = server.accept()
            pass
        except KeyboardInterrupt:
            print '\n'
            Utils.print_exit_message_simple()
            sys.exit(1)
        print astk + gs + "Connection established by client: " + ce + Colors.WHITE + address[0] + ce + "\n"
    else:
        """
        Print a message indicating that the server is waiting for the client to respond
        Print the clients response
        """
        print '\n' + ys + ">> " + ce + Colors.WHITE + "Waiting for client response..." + ce + '\n'
        print ys + "[ " + ce + Colors.WHITE + "MESSAGE:CLIENT" + ce + ys + " ]: " + ce + ys, s.recv(4080), ce
        try:
            cmd = raw_input(ys + "server" + ce + Colors.WHITE + ':' + ce + ys + hostname + '> ' + ce)
            s.send(cmd)
            # -------------------------------------------------------------------------------------------------
            # Regex string search
            cmd_exit = re.search("(exit|power off)", cmd, re.I | re.M)

            # -------------------------------------------------------------------------------------------------
            # Client sent commands

            # -------------------------------------------------------------------------------------------------
            if cmd_exit:
                """
                print '\n' + astk + gs + "Saving data..." + ce
                Utils.save_data()
                print '\n' + astk + gs + "Data saved..." + ce
                """
                # Send info to the client
                s.send(Colors.WHITE + " [ Server initialized termination command ]" + Colors.COLOR_END)
                connection.close_connections()
                Utils.print_exit_message_simple()
                sys.exit(1)
        except KeyboardInterrupt:
            print '\n'
            connection.close_connections()
            sys.exit(1)
