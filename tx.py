import serial
import struct
import time




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

cw_base = 0.5
cw_long  = cw_base
cw_short = cw_base / 3

ser.setDTR(False)
time.sleep(cw_short)
ser.setDTR(True)
time.sleep(cw_long)
ser.setDTR(False)
time.sleep(cw_short)

ser.setDTR(False)
time.sleep(cw_short)
ser.setDTR(True)
time.sleep(0.3)
ser.setDTR(False)
time.sleep(cw_short)

ser.setDTR(False)
time.sleep(cw_short)
ser.setDTR(True)
time.sleep(cw_long)
ser.setDTR(False)
time.sleep(cw_short)

ser.setDTR(False)
time.sleep(cw_short)
ser.setDTR(True)
time.sleep(cw_short)
ser.setDTR(False)
time.sleep(cw_short)

'''
print('70cm v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x44, 0x61, 0x87, 0x00, 0x01)  
                              MM    Mk    kk    hh
ser.write(data)
s = ser.read(1)
'''
x = 2700
time.sleep(1)


