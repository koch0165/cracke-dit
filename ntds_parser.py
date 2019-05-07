import re

from impacket.examples.secretsdump import NTDSHashes

def process_local(ntds, historic):
    hashes = list()
    ntdshashes = NTDSHashes(ntds)
    while True:
        if ntdshashes is None:
            break  
        record, hasNextRecord = ntdshashes.getNextRecord()
        if hasNextRecord == False:
            break
        if record is None: 
            continue
        hashes.append(__process_hash(record))
    ntdshashes.finish()
    return None, hashes

def __process_hash(hash):
    print("processing hash")
    displayname, user, objectguid  = re.findall("(?P<displayname>.*):(?P<user>.*):(?P<objectguid>.*)", hash)[0]
    return {"displayname": displayname.strip(), "username": user.strip(), "objectguid": objectguid.strip()}
