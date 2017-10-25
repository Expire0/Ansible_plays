#convert a mac address without the colon to the proper format. 

conv=':'.join(format(s, '02x') for s in bytes.fromhex(mas))
