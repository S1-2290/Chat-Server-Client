import os
import sys

# -- Module: Colors - colors.py - v1.0

# Normal colors
class Colors:

    GREEN = "\033[32m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    WHITE = "\033[37m"
    LIGHT_BLUE = "\033[36m"
    PURPLE = "\033[35m"
    COLOR_END = "\033[0m"

# Bold colors
class ColorsBold:

    GREEN_BOLD = "\033[01;32m"
    RED_BOLD = "\033[01;31m"
    YELLOW_BOLD = "\033[01;33m"
    BLUE_BOLD = "\033[01;34m"
    WHITE_BOLD = "\033[01;37m"
    LIGHT_BLUE_BOLD = "\033[01;36m"
    PURPLE_BOLD = "\033[01;35m"
    COLOR_END_BOLD = "\033[00m"

# Patterns
class Patterns:

    PLUS = Colors.GREEN + "[+] " + Colors.COLOR_END
    MINUS = Colors.RED + "[-] " + Colors.COLOR_END
    ASTK = Colors.BLUE + "[*] " + Colors.COLOR_END
