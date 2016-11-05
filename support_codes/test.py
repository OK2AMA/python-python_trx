import serial
import struct
import time
import timeit

pravda = True

# By Kuba OK2AMA
# control your Yaesu FT-857
ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate=9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.EIGHTBITS
)

print(ser.isOpen())




'''
print('70cm v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x44, 0x61, 0x87, 0x00, 0x01)  
                              MM    Mk    kk    hh
ser.write(data)
s = ser.read(1)
'''
time.sleep(1)
print( time.time() )
time.sleep(1)
print( time.time() )
time.sleep(1)
print( time.time() )
time.sleep(1)
print( time.time() )

    
   


    

