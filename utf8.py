import binascii
import filecmp
global list


list = []
with open("C:\Python27\gujarati_in.txt","rb") as f:
    firstbyte = f.read(1)
    while firstbyte!="": 
        secondbyte = f.read(1)
        final = (ord(firstbyte)<<8) + (ord(secondbyte))
        if int('7F',16) >= final :
            list.append(final)
        if int('7FF',16) >= final and final>= int('80',16):
            byte1 = int((ord(firstbyte)<<2) | (ord(secondbyte)>>6) | 0xC0)
            list.append(byte1)
            byte2 = int((ord(secondbyte)>>2 )| 0x80)
            list.append(byte2)
        if int('FFFF',16) >= final and final>= int('800',16):    
            byte1 = int((ord(firstbyte)>>4) | 0xE0)
            list.append(byte1)
            byte2 = int(((ord(firstbyte)<<2)& 0x3C) |(ord(secondbyte)>>6)| 0xC0)
            list.append(byte2)
            byte3 = int(ord(secondbyte) & 0xBF)
            list.append(byte3)
        firstbyte = f.read(1)    
f.close()
values = bytearray(list)
g = open("C:\Python27\gujarati_out.txt","wb")
g.write(values)
g.close()
print filecmp.cmp("C:\Python27\gujarati_out.txt", "C:\Python27\out\gujarati_out.txt")