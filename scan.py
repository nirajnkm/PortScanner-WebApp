#usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread
from time import time
import subprocess


open_ports = []


def prepare_args():

	parser = ArgumentParser(description="PythonBased Fast Port Scanner",usage="%(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.1")       	
	parser.add_argument(metavar="IPv4",dest="ip",help="host to scan")
	parser.add_argument("-s","--start",dest="start",metavar="\b",type=int,help="starting port",default=1)

	parser.add_argument("-e","--end",dest="end",metavar="\b",type=int,help="end port",default=65535)

	parser.add_argument("-t","--threads",dest="threads",metavar="\b",type=int,help="number of threads",default=500)

	parser.add_argument("-V","--verbose",dest="verbose",action="store_true",help="vervose")
	parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0")
	args = parser.parse_args()
	return args

def prepare_ports(start:int,end:int):
	for port in range(start,end+1):
                yield port
				
def scan_port():
        
        while True:
                
                try:
                        s=socket.socket()
                        s.settimeout(1)
                        port = next(ports)
                        s.connect((arguments.ip,port))
                        open_ports.append(port)
                        if arguments.verbose:
                                print(f"\r{open_ports}",end="")
                except (ConnectionRefusedError,socket.timeout):
                        continue
                except StopIteration:
                        break                


def prepare_threads(threads:int):
        thread_list = []
        for _ in range(threads):
                thread_list.append(Thread(target=scan_port))    
        for thread in thread_list:
                thread.start()  
        for thread in thread_list:
                thread.join()
		  			

if __name__ == "__main__":
        arguments = prepare_args()
        ports = prepare_ports(arguments.start,arguments.end)
        #start_time = time()
        prepare_threads(arguments.threads)
        #end_time = time()
        #if arguments.verbose:
        #       print()
        #print(f"Open Ports Found - {open_ports}")
        #print(f"Time taken {round(end_time - start_time)}")
        with open('openports.txt', 'w') as file:
        # Write Python code to the file
                file.write(str(open_ports))

