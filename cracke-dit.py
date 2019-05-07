import sys, glob, os, argparse, itertools, time
from threading import Thread, Event

import json

from impacket.examples.secretsdump import NTDSHashes
import re
import codecs
import locale

BANNER = """\033[91m
                        __                  ___ __ 
  ______________ ______/ /_____        ____/ (_) /_
 / ___/ ___/ __ `/ ___/ //_/ _ \______/ __  / / __/
/ /__/ /  / /_/ / /__/ ,< /  __/_____/ /_/ / / /_  
\___/_/   \__,_/\___/_/|_|\___/ \033[90mv1.0\033[0m\033[91m \__,_/_/\__/  
        \033[0m@darkp0rt\n"""


if __name__ == "__main__":
    #print(BANNER)
    #available_outputs = ", ".join(outputs.discover_outputs().keys())

    parser = argparse.ArgumentParser(add_help=False, description="crack-dit makes it easier to perform password "
                                                                "audits against Windows-based corporate environments.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--database-name", default="db.json", action="store", help="Name of the database file to store")
    parser.add_argument("--help", action="store_true", help="show this help message and exit", required=False)

    group = parser.add_argument_group("1. Cracking", "cracke-dit can take your raw ntds.dit and SYSTEM hive "
                                                              "and turn them in to a user:hash file for cracking "
                                                              "within your favourite password cracker")
    group.add_argument("--ntds", action="store", help="(local) ntds.dit file to parse")
    group.add_argument("--out", action="store", help="File to write user:hash to")
    args, unknown_args = parser.parse_known_args()
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout) 

    validFile = False
    try:
        ntdshashes = NTDSHashes(args.ntds)
        validFile = True
        print('FileOpenSucceded')
        sys.stdout.flush();
    except Exception as e:
        print('InvalidFile')
        sys.stdout.flush();
    wait = True

    try:
        while validFile and True:
            #if wait == True:
            #    line = sys.stdin.readline()
            if ntdshashes is None:
                print('Finished')
                sys.stdout.flush()
                break
            record, hasNextRecord = ntdshashes.getNextRecord()
            if hasNextRecord == False:
                print('Finished')
                sys.stdout.flush()
                break
            if record is None:
                wait =  False
                continue
            displayname, user, objectguid  = re.findall("(?P<displayname>.*):(?P<user>.*):(?P<objectguid>.*)", record)[0]
            userrecord = displayname.strip() +","+ user.strip()+","+objectguid.strip()+"\n"
            print(userrecord)
            sys.stdout.flush()
            wait = True
    except Exception as e:
        print('Error'+str(e))
