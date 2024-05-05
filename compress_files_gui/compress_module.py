import zlib , base64 #-> compress , decode 

def compress(inputfile,outputfile , comp_level) : 
    data = open(inputfile,'r').read() #-> read the file 
    data_bytes= bytes(data,'utf-8')#-> convert the str to bytes 
    comp_data= base64.b64encode(zlib.compress(data_bytes,comp_level)) #-> encode data to 64 and compress it 
    decoded_data=comp_data.decode('utf-8') #-> convert the bytes to str 
    comp_file = open(outputfile,'w') # -> open file to read data 
    comp_file.write(decoded_data)#-> write the data 
    comp_file.close() 



def decompress(inputfile,outputfile) : 
    data =open(inputfile,'r').read()
    decomp_data =zlib.decompress (base64.b64decode(data)).decode('utf-8')
    decomp_file =open(outputfile , 'w')
    decomp_file.write(decomp_data)
    decomp_file.close()


