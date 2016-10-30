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
ser.setDTR(False)
time.sleep(2)



'''
print('70cm v case je: %s\n' % time.ctime())
data = struct.pack('BBBBB', 0x44, 0x61, 0x87, 0x00, 0x01)  
                              MM    Mk    kk    hh
ser.write(data)
s = ser.read(1)
'''
start = 0
end = 0
start_tx = 0
while(pravda):
    data = struct.pack('BBBBB', 0x00, 0x00, 0x00, 0x00, 0xE7)
    ser.write(data)
    rx_status = ser.read(1)
    
    resp_byte = (rx_status[0])
    squelch = True if (resp_byte & 0B10000000) else False
    s_meter = resp_byte & 0x0F
    
    time.sleep(0.2)
    
    if( (squelch == False ) and (start == 0 ) ):
        print("Zacinam nahravat")
        start = time.time()
    
    if( (squelch == True ) and (start != 0 ) and end == 0 ):
        print("Konec nahravky")
        end = time.time() - start
        
    if( ( end != 0 ) and (start_tx == 0) ):
        print("Zacinam vysilat")
        ser.setDTR(True)
        start_tx = time.time()

    if((end < (time.time() - start_tx ) ) and ( start_tx != 0 ) ) : 
        print("Konec TX")
        ser.setDTR(False)
        start = 0
        end = 0
        start_tx = 0
    
   


    

