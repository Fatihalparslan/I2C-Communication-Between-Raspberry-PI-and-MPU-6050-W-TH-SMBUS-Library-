# I2C-Communication-Between-Raspberry-PI-and-MPU-6050-W-TH-SMBUS-Library-
### Functions 

 write_quick(int addr) tek bir bit yazmaya yarar.
 
read_byte(int addr) 1 byte okur 

write_byte(int addr,char val) 1 byte yazar 

read_byte_data(int addr,char cmd)-1 byte okumayi saglar,cmd register adresi,addr slave cihaz I2C adresi

write_byte_data(int addr,char cmd,char val)-1 byte veriyi registera atama addr cihaz adresi,cmd register
adresi ,val yazilmak istenen deger

read_i2c_block_data(int addr,char cmd)

write_i2c_block_data(int addr,char cmd,long vals[])

proje videosu:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/5_tBxGctzWc/0.jpg)](https://www.youtube.com/watch?v=5_tBxGctzWc)
