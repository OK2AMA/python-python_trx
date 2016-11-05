import serial
import struct
import time

# By David PD7L
# Example to control your Yaesu FT-897
ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate=9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.EIGHTBITS
)
print(ser.isOpen())
# Put the yaesu FT-897 on freq 439.700

print('70cm v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x44, 0x61, 0x87, 0x00, 0x01)
ser.write(data)
s = ser.read(1)


time.sleep(0.1)

print('2m v case je: %s\n' % time
	  .ctime())
data = struct.pack('BBBBB', 0x14, 0x55, 0x50, 0x00, 0x01)
ser.write(data)
s = ser.read(1)

#print('odezva je: %s\n' % ser.read(1))


time.sleep(0.1)

print('10m v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x02, 0x79, 0x65, 0x00, 0x01)
ser.write(data)
s = ser.read(1)


time.sleep(0.1)
print('RX status v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x00, 0x00, 0x00, 0x00, 0xE7)
ser.write(data)
rx_status = ser.read(1)

resp_byte = ord(rx_status[0])
squelch = True if (resp_byte & 0B10000000) else False
s_meter = resp_byte & 0x0F

# Read ack from the yaesu
print('Odezva od Yaesu je:\n' )

print(squelch)
print(s_meter)

ser.close()