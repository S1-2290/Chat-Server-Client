import os
import sys

# -- Module: Config - config.py - v1.0

"""
Main config class: MainConfigBinary
- @Contains:
  -> LIST_OF_PORTS => $list{<@?>}
  -> LIST_OF_HOSTS => $list{<@?>}
"""
class MainConfigBinary:

    def __init__(self):
        self.LIST_OF_PORTS = []
        self.LIST_OF_HOSTS = []
