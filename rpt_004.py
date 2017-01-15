#!/usr/bin/env python3
#
# By Kuba OK2AMA
# control your Yaesu FT-857

import pyaudio
import wave
import sys
import serial
import struct
import time


never_end_loop = True
prubeh_rec = False
prubeh_play = False


ser = serial.Serial(
  port='/dev/ttyUSB0',
  baudrate=9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_TWO,
  bytesize=serial.EIGHTBITS
)

print(ser.isOpen())
ser.setDTR(False)
time.sleep(1)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")
frames = []

"""PyAudio Example: Play a WAVE file.
*********************************************************************
"""

wf = wave.open("output.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

p.terminate()

# ***********************************

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
while(never_end_loop):
    data = struct.pack('BBBBB', 0x00, 0x00, 0x00, 0x00, 0xE7)
    ser.write(data)
    rx_status = ser.read(1)
    
    resp_byte = (rx_status[0])
    squelch = True if (resp_byte & 0B10000000) else False
    s_meter = resp_byte & 0x0F
    
    # time.sleep(0.2)
    
    if( (squelch == False ) and (start == 0 ) ): 
        print("Zacinam nahravat")
        start = time.time()
        prubeh_rec = True
        
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        frames = []

        
        
    if( prubeh_rec == True ):  
        print("* recording")
        data = stream.read(CHUNK)
        frames.append(data)

    
    if( (squelch == True ) and (start != 0 ) and end == 0 ):
        print("Konec nahravky")
        end = time.time() - start
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        prubeh_rec = False    
        
        
    if( ( end != 0 ) and (start_tx == 0) ):
        print("Zacinam vysilat")
        ser.setDTR(True)
        start_tx = time.time()
        wf = wave.open("output.wav", 'rb'
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        prubeh_play = True

		
    if( prubeh_play == True ):    
        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

    if((end < (time.time() - start_tx ) ) and ( start_tx != 0 ) ) : 
        print("Konec TX")
        ser.setDTR(False)
        start = 0
        end = 0
        start_tx = 0
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        prubeh_play = False
