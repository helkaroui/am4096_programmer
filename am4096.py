#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
import smbus
import time

class AM4096:
    """
    Class of the AM4096
    """

    def __init__(self , bus , address):
        """ init the am4096 class"""
        self.bus = smbus.SMBus(bus)
        self.address = address
        self.busaddr= bus
        self.devices=[]
    def get_settings(self):
        pass
    def check_default_settings(self):
        pass
    def write_default_settings(self):
        pass
    def get_status(self):
        pass
    def scan_all(self):
        pass
    def get_device_list(self):
        pass
    def connect_to(self,device):
        pass
    def connect_to_first(self):
        pass
    def read_memory(self, reg):
        return self.bus.read_i2c_block_data(self.address, reg)
        pass
    def write_memory(self, reg , data):
        if (len(data)>2) return False
        res = self.bus.write_i2c_block_data(self.address, reg, data)
        return res
    def write_memory_with_check(self,addr , reg , data):
        pass
