I2Cexample.py Kodları

import smbus
import time
Bus = smbus.SMBus(1)
"""I2C1 kanali secildi 
# mpu6050'nin I2C adresi 0x68'dir
"""
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_XOUT_L = 0x3C
ACCEL_YOUT_H = 0x3D
ACCEL_YOUT_L = 0x3E
ACCEL_ZOUT_H = 0x3F
ACCEL_ZOUT_L = 0x40
GYRO_XOUT_H  = 0x43
GYRO_XOUT_L  = 0x44
GYRO_YOUT_H  = 0x45
GYRO_YOUT_L  = 0x46
GYRO_ZOUT_H  = 0x47
GYRO_ZOUT_L  = 0x48

def mpu_init():
    #sample rate diveder register  
    Bus.write_byte_data(0x68,SMPLRT_DIV,0x07)
    #power management register
    Bus.write_byte_data(0x68,PWR_MGMT_1,0x01)
	#Gyro configuration register
    Bus.write_byte_data(0x68, GYRO_CONFIG, 24)    

def ivmeX_oku():
    value1=Bus.read_byte_data(0x68,ACCEL_XOUT_H)
    value2=Bus.read_byte_data(0x68,ACCEL_XOUT_L)
    value=(value1<<8)|value2 #xxxxxxxx00000000|
    if value>32768:
        value=value-65536
    return value/16384.0

def ivmeY_oku():
    value1=Bus.read_byte_data(0x68,ACCEL_YOUT_H)
    value2=Bus.read_byte_data(0x68,ACCEL_YOUT_L)
    value=(value1<<8)|value2
    if value>32768:
        value=value-65536
    return value/16384.0

def ivmeZ_oku():
    value1=Bus.read_byte_data(0x68,ACCEL_ZOUT_H)
    value2=Bus.read_byte_data(0x68,ACCEL_ZOUT_L)
    value=(value1<<8)|value2
    if value>32768:
        value=value-65536
    return value/16384.0

def GyroX():
    value1=Bus.read_byte_data(0x68,GYRO_XOUT_H)
    value2=Bus.read_byte_data(0x68,GYRO_XOUT_L)
    value=(value1<<8)|value2
    if value>32768:
        value=value-65536
    return value/16.4    

def GyroY():
    value1=Bus.read_byte_data(0x68,GYRO_YOUT_H)
    value2=Bus.read_byte_data(0x68,GYRO_YOUT_L)
    value=(value1<<8)|value2
    if value>32768:
        value=value-65536
    return value/16.4 

def GyroZ():
    value1=Bus.read_byte_data(0x68,GYRO_ZOUT_H)
    value2=Bus.read_byte_data(0x68,GYRO_ZOUT_L)
    value=(value1<<8)|value2
    if value>32768:
        value=value-65536
    return value/16.4 
    
mpu_init()

time.sleep(0.5)
while 1:
    
    print("AX: %.2f"%ivmeX_oku() ,"AY: %.2f"%ivmeY_oku() ,"AZ: %.2f"%ivmeZ_oku() ,"GX: %.2f"%GyroX() 
    ,"GY: %.2f"%GyroY(),"GZ: %.2f"%GyroZ())
    time.sleep(0.1)
