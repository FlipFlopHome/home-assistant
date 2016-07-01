#!/usr/bin/env python

import http.client
import time

BUFFER_SIZE = 1024
Success = True
Fail = False

 
SWITCH_ON_REQUEST = '/relay/1'
SWITCH_OFF_REQUEST = '/relay/0'
SWITCH_GET_STATE_REQUEST = '/relay'


class WiFly():

     def __init__(self, IpAddress, Port):
         self.IpAddress = IpAddress
         self.Port = Port

     def OpenConnection(self):
         try:
             self.s = http.client.HTTPConnection(self.IpAddress, self.Port)
         except:
             self.s = None
             return Fail

         return Success


     def getSwitchState(self):
         
         if self.s == None:
             print('None')
         else:
             self.s.request("GET", SWITCH_GET_STATE_REQUEST)
             data = self.s.getresponse()
             
             if data.read() == b'{"relay": 1}':
                 return True
             else:
                 return False  

     def setOn(self):
         #bArrayRequest = SWITCH_ON_REQUEST.encode()
         if self.s == None:
             print('None')
         else:
             self.s.request("GET", SWITCH_ON_REQUEST)
             data = self.s.getresponse()
             
             if data.read() == b'{"relay": 1}':
                 return Success
             else:
                 return Fail     

     def setOff(self):
         if self.s == None:
             print('None')
         else:
             self.s.request("GET", SWITCH_OFF_REQUEST)
             data = self.s.getresponse()
             
             if data.read() == b'{"relay": 0}':
                 return Success
             else:
                 return Fail
             
         

 

