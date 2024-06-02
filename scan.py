#usr/bin/python3

from argparse import ArgumentParser
import socket
from threading import Thread

def prepare_args():
    parser = ArgumentParser(description="PythonBased Fast Port Scanner", usage="%(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.1")        
    parser.add_argument(metavar="IPv4", dest="ip", help="host to scan")
    parser.add_argument("-s", "--start", dest="start", metavar="\b", type=int, help="starting port", default=1)
    parser.add_argument("-e", "--end", dest="end", metavar="\b", type=int, help="end port", default=65535)
    parser.add_argument("-t", "--threads", dest="threads", metavar="\b", type=int, help="number of threads", default=500)
    parser.add_argument("-V", "--verbose", dest="verbose", action="store_true", help="verbose")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    return args

def prepare_ports(start:int, end:int):
    for port in range(start, end+1):
        yield port

def scan_port(ip, port, open_ports):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        open_ports.append(port)
    except (ConnectionRefusedError, socket.timeout):
        pass

def prepare_threads(ip, ports, threads:int):
    open_ports = []
    thread_list = []
    for port in ports:
        thread = Thread(target=scan_port, args=(ip, port, open_ports))
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    return open_ports

def get_open_ports(ip, start, end, threads):
    ports = prepare_ports(start, end)
    open_ports = prepare_threads(ip, ports, threads)
    return open_ports

if _name_ == "_main_":
    arguments = prepare_args()
    open_ports = get_open_ports(arguments.ip, arguments.start, arguments.end, arguments.threads)
    print(f"Open Ports Found: {open_ports}")