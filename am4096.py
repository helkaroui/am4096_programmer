#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
from smbus import SMBus
import time

class AM4096:
    """
    Class of the AM4096
    """
    #self.configuration = {'Pdint','AGCdis','Slowint','Pdtr','Pdie','Reg35','Adr','Abridis','Bufsel','Monsel','Sign','Zin','Nfil','Daa','Hist','Dact','Dac','SSIcfg','Sth','UVW','Res','SRCH','Rpos','Apos','Weh','Wel','Thof','Tho'}

    def __init__(self , bus , Name = None , address = None):
        """ init the am4096 class"""
        self.bus = SMBus(bus)
        self.address = address
        self.busaddr= bus
        self.configuration = {}
        self.devices=[]
        self.i2c_repeated_start_condition = self.check_start_condition()
    def get_settings(self, stored = True):
        configuration = {}
        reg_addr= 0 if stored else 48
        row = self.read_memory(reg_addr)
        configuration['Pdint']= int((row[0] >> 7) & 0x01)
        configuration['AGCdis']= int((row[0] >> 6) & 0x01)
        configuration['Slowint']= int((row[0] >> 4) & 0x01)
        configuration['Pdtr']= int((row[0] >> 2) & 0x03)
        configuration['Pdie']= int((row[0] >> 1) & 0x01)
        configuration['Reg35']= int(row[0] & 0x01)
        configuration['Addr']= int(row[1] & 0x7F)

        row = self.read_memory(reg_addr+1)
        configuration['Abridis']= int((row[0] >> 7) & 0x01)
        configuration['Bufsel']= int((row[0] >> 6) & 0x01)
        configuration['Monsel']= int((row[0] >> 5) & 0x01)
        configuration['Sign']= int((row[0] >> 4) & 0x01)
        configuration['Zin']= int(((row[0] & 0x0F) << 8) + row[1])

        row = self.read_memory(reg_addr+2)
        configuration['Nfil']= int(row[0])
        configuration['Daa']= int((row[1] >> 7) & 0x01)
        configuration['Hist']= int(row[1] & 0x7F)

        row = self.read_memory(reg_addr+3)
        configuration['Dact']= int((row[0] >> 7) & 0x01)
        configuration['Dac']= int((row[0] >> 5) & 0x03)
        configuration['SSIcfg']= int((row[0] >> 3) & 0x03)
        configuration['Sth']= int(((row[0] & 0x01) << 8)  + ((row[1] >> 6) & 0x03))
        configuration['UVW']= int((row[1] >> 3) & 0x07)
        configuration['Res']= int((row[1] >> 3) & 0x07)

        row = self.read_memory(32)
        configuration['Rpos']= {'valid': int((row[0] >> 7) & 0x01) , 'value':int(((row[0] & 0x0F) << 8) + row[1])}

        row = self.read_memory(33)
        configuration['Apos']= {'valid': int((row[0] >> 7) & 0x01) , 'value':int(((row[0] & 0x0F) << 8) + row[1])}

        row = self.read_memory(34)
        configuration['Weh']= int((row[0] >> 6) & 0x01)
        configuration['Wel']= int((row[0] >> 5) & 0x01)

        row = self.read_memory(35)
        configuration['AGCgain']= int((row[0] >> 4) & 0x0F)
        configuration['Thof']= int((row[0] >> 2) & 0x01)
        configuration['Tho']= int(((row[0] & 0x03) << 8) + row[1])
        
        if stored :
            self.configuration = configuration
        return configuration 
        
    def set_address(self):
        return
    def get_Absolute_position(self):
        row = self.read_memory(33)
        return int(((row[0] & 0x0F) << 8) + row[1])
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
        if (len(data)>2):
            return False
        res = self.bus.write_i2c_block_data(self.address, reg, data)
        return res
    def write_memory_with_check(self,addr , reg , data):
        pass
    def check_start_condition(self):
        """ Init repeated start mode"""
        try:
            f = open('/sys/module/i2c_bcm2708/parameters/combined','w+r')
            if(str(f.read(1)).lower() != 'y'):
                f.write('Y')
            f.close()
        except IOError:
            print "Don't have write permission"
    def __str__(self):
        print(self.configuration)
        pass
        

am = AM4096(1,address = 55)
am.get_settings()
while(1):
    print(am.get_Absolute_position())

