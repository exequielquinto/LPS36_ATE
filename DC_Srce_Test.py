#import pandas as pd         
import visa, time    

#Connect to Instruments
rm = visa.ResourceManager()
DC_Srce = rm.open_resource('USB0::0x0A69::0x084B::S50000000068::0::INSTR')


#Read Instrument IDs
print DC_Srce.query('*IDN?')

DC_Srce.write('SOUR:VOLT 10.0005')
DC_Srce.write('SOUR:CURR 2.05')
DC_Srce.write('CONF:OUTP ON')
time.sleep(2)

V1 = (DC_Srce.query('MEASure:VOLTage?'))
time.sleep(0.5)
I1 = (DC_Srce.query('MEASure:CURRent?'))
time.sleep(0.5)

DC_Srce.write('CONF:OUTP OFF')

print float(V1)
print float(I1)
