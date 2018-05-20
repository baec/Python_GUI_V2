#!/usr/bin/python3
# Filename :rect.py
# Contains the Rectangle class
# Author   : Christian Baeza
# Note: Hello World!
#-----------------------------

class Rectangle():
   
   def __init__(self, stat, value, width, code, quant, switch):

      self.stat= stat
      self.value=value
      self.width=width
      self.code= code
      self.quant=quant
      self.switch=switch
      
      

   def getStat(self):return self.stat
   def getValue(self):return self.value
   def getWidth(self):return self.width
   def getCode(self):return self.code
   def getQuant(self):return self.quant
   def getSwitch(self):return self.switch
 
