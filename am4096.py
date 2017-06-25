#!/usr/bin/python2.7
#-*- coding: utf-8 -*-
from smbus import SMBus
import time

class AM4096:
    """
    Class of the AM4096
    """
    #self.configuration = {'Pdint','AGCdis','Slowint','Pdtr','Pdie','Reg35','Adr','Abridis','Bufsel','Monsel','Sign','Zin','Nfil','Daa','Hist','Dact','Dac','SSIcfg','Sth','UVW','Res','SRCH','Rpos','Apos','Weh','Wel','Thof','Tho'}

    def __init__(self , bus , address):
        """ init the am4096 class"""
        self.bus = SMBus(bus)
        self.address = address
        self.busaddr= bus
        self.configuration = {}
        self.devices=[]
        self.i2c_repeated_start_condition = self.check_start_condition()
    def get_stored_settings(self):
        row = self.read_memory(0)
        self.configuration['Pdint']= int((row[0] >> 7) & 0x01)
        self.configuration['AGCdis']= int((row[0] >> 6) & 0x01)
        self.configuration['Slowint']= int((row[0] >> 4) & 0x01)
        self.configuration['Pdtr']= int((row[0] >> 2) & 0x03)
        self.configuration['Pdie']= int((row[0] >> 1) & 0x01)
        self.configuration['Reg35']= int(row[0] & 0x01)
        self.configuration['Addr']= int(row[1] & 0x7F)

        row = self.read_memory(1)
        self.configuration['Abridis']= int((row[0] >> 7) & 0x01)
        self.configuration['Bufsel']= int((row[0] >> 6) & 0x01)
        self.configuration['Monsel']= int((row[0] >> 5) & 0x01)
        self.configuration['Sign']= int((row[0] >> 4) & 0x01)
        self.configuration['Zin']= int((row[0] & 0x0F) + row[1])

        row = self.read_memory(2)
        self.configuration['Nfil']= int(row[0])
        self.configuration['Daa']= int((row[1] >> 7) & 0x01)
        self.configuration['Hist']= int(row[1] & 0x7F)

        row = self.read_memory(3)
        self.configuration['Nfil']= int(row[0])
        self.configuration['Daa']= int((row[1] >> 7) & 0x01)
        self.configuration['Hist']= int(row[1] & 0x7F)

        
        #self.configuration = {Dact','Dac','SSIcfg','Sth','UVW','Res','SRCH','Rpos','Apos','Weh','Wel','Thof','Tho'}
        return self.configuration
    def get_address(self):
        return 
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
        

am = AM4096(1,55)
am.get_stored_settings()
"""
while(1):
    try:
        res = am.read_memory(32)
    except IOError:
        print "am4096 disconnected"
    print((res[0] << 8)+ res[1])

"""
