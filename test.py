#import pandas as pd         
import visa, time    

#Connect to Instruments
rm = visa.ResourceManager()
DC_Srce = rm.open_resource('USB0::0x0A69::0x084B::S50000000068::0::INSTR')
daq = rm.open_resource('ASRL1::INSTR')
eload1 = rm.open_resource('USB0::0x0A69::0x083E::636002000532::0::INSTR')  #Ch2, Ch1
eload2 = rm.open_resource('USB0::0x0A69::0x083E::636002000381::0::INSTR')  #Ch4, Ch3

#Read Instrument IDs
print DC_Srce.query('*IDN?')
print daq.query('*IDN?')
print eload1.query('*IDN?')
print eload2.query('*IDN?')

DC_Srce.write('SOUR:VOLT 10.00')
DC_Srce.write('SOUR:CURR 5.00')
DC_Srce.write('CONF:OUTP ON')
time.sleep(2)
DC_Srce.write('CONF:OUTP OFF')