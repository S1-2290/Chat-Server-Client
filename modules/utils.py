import os
import sys
import socket
import pickle
from colors import *
from config import MainConfigBinary

# -- Module: Utility - utils.py - v1.0

# Classes
cnf_bin = MainConfigBinary()

class Utils:

    def __init__(self, exit_on_error=True, new_line_char='\n'):
        self.EX = exit_on_error
        self.NL = new_line_char


    @staticmethod
    def print_error_msg(message, exit_on_error):
        if len(message) == 0:
            print "Please enter a(n) error message..."
            sys.exit(1)
        else:
            print Colors.RED + "Error: " + Colors.COLOR_END + Colors.WHITE + message + Colors.COLOR_END
            if exit_on_error:
                sys.exit(1)
            else:
                pass

    @staticmethod
    def check_ip_address_input(address):
        addr = address

        if len(addr) == 0:
            Utils.print_error_msg("Please fill in the IP Address field...", False)
            pass
        else:
            pass

    @staticmethod
    def check_port_number_input(port):
        if port <= 0:
            if port > 65535:
                Utils.print_error_msg("Port non-existent, please enter a port in between 1 - 65,535...", False)
                pass
            else:
                pass
            Utils.print_error_msg("Port cannot be less than 1...", False)
            pass
        else:
            pass

    @staticmethod
    def print_exit_message_simple():
        print Colors.WHITE + "Exiting..." + Colors.COLOR_END
        pass

    @staticmethod
    def add_port_to_list(port):
        Utils.check_port_number_input(int(port))

        if port not in cnf_bin.LIST_OF_PORTS:
            # Add the port
            print Colors.WHITE + "|_" + Colors.COLOR_END + "Adding port: " + Colors.YELLOW, port, Colors.COLOR_END + "to the list..."
            cnf_bin.LIST_OF_PORTS.append(port)
            pass
        else:
            pass

    @staticmethod
    def add_host_to_list(hostname):
        Utils.check_ip_address_input(str(hostname))

        if hostname not in cnf_bin.LIST_OF_HOSTS:
            # Add the hostname to the list
            print Colors.WHITE + "|_" + Colors.COLOR_END + "Adding hostname: " + Colors.YELLOW + hostname + Colors.COLOR_END + " to the list..."
            cnf_bin.LIST_OF_HOSTS.append(hostname)
            pass
        else:
            pass

    @staticmethod
    def save_data():
        # Use pickle to serialize the class data from the __init__()
        save_file = open(".save.dat", "wb")
        with open(save_file) as data:
            pickle.dump(cnf_bin, data)
            pass
        save_file.close()

class Connect:

    def __init__(self, sock_stream, hostname, port_number):
        self.sock = sock_stream
        self.host = hostname
        self.port = port_number

    def connect(self):
        print Patterns.ASTK + Colors.GREEN + "Connecting..." + Colors.COLOR_END
        try:
            # Bind the connection
            self.sock.bind((self.host, self.port))
            print Patterns.ASTK + Colors.GREEN + "Connection successful..." + Colors.COLOR_END
            print Patterns.ASTK + Colors.GREEN + "Connected to port: ", self.port, Colors.COLOR_END
            pass
        except socket.error as e:
            print Colors.RED + "Error: " + Colors.COLOR_END + Colors.WHITE + str(e) + Colors.COLOR_END
            sys.exit(1)

    def close_connections(self):
        print Colors.WHITE + "[I] " + Colors.COLOR_END + Colors.YELLOW + "Closing connection..." + Colors.COLOR_END
        try:
            self.sock.close()
            sys.exit(1)
        except Exception as e:
            print Colors.RED + "Error: " + Colors.COLOR_END + Colors.WHITE + "Could not normally close connection, forcing connection termination..." + Colors.COLOR_END
            sys.exit(1)
