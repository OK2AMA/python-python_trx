import serial
import struct
import time


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

for x in range (200000, 1000000,100):
    h_d = int(x/10) % 100
    h_c = int(x/1000) % 100
    h_b = int(x/100000) % 100
    h_a = int(x/10000000) % 100

    data = struct.pack('BBBBB', h_a, h_b, h_c, h_d, 0x01)
    ser.write(data)
    s = ser.read(1)
    time.sleep(0.1)
    data = struct.pack('BBBBB', 0x00, 0x00, 0x00, 0x00, 0xE7)
    ser.write(data)
    rx_status = ser.read(1)
    resp_byte = ord(rx_status[0])
    s_meter = resp_byte & 0x0F
    print(x)
    print(s_meter)
    print("")
	

