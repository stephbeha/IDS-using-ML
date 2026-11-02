from scapy.all import *
from sys import argv
import logging
import datetime
from datetime import datetime

import RuleFileReader
from Sniffer import *

RED = '\033[91m'
BLUE = '\033[34m'
GREEN = '\033[32m'
ENDC = '\033[0m'
#C:\Users\stephane\OneDrive\Documents\final year project\ML-IDS-ICT
#usage python -B src/ML-IDS.py rules/ML-RULES.txt
def main(filename):
    """Read the rule file and start listening."""
    from datetime import datetime
    
    now = datetime.now()
 # Format the datetime string to not include invalid characters
    formatted_now = now.strftime("%Y-%m-%d %H-%M-%S")
    
    logging.basicConfig(filename= "Simple-NIDS " + formatted_now + '.log', level=logging.INFO)

    print ("ML-IDS started.")
    # Read the rule file
    print ("Reading rule file...")
    global ruleList
    ruleList, errorCount = RuleFileReader.read(filename);
    print ("Finished reading rule file.")

    if (errorCount == 0):
        print ("All (" + str(len(ruleList)) + ") rules have been correctly read.")
    else:
        print (str(len(ruleList)) + " rules have been correctly read.")
        print (str(errorCount) + " rules have errors and could not be read.")

    # Begin sniffing
    sniffer = Sniffer(ruleList)
    sniffer.start()
    
    #sniffer.stop()
    #print "Simple-NIDS stopped."

ruleList = list()
script, filename = argv
main(filename)
