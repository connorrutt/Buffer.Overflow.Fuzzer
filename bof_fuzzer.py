#!/usr/bin/env python3
import pwntools pwn
from pwn import *

target_host = "example.com" ##target must have port adjusted, default set to 80
target_port = 80 

conn = pwntools.remote(target_host, target_port) 

payload_size = 100 ##default 100 but depending on potential time out, may lower or may higher 

while True:  
    payload = 'A' * payload_size  
    conn.send(payload)                                                            
   
   print("Sent %d bytes" % len(payload))                                       

while False:
    r = requests.post(url, data=payload, timeout=[])
   print("TimeOut: Lowering Payload size" % payload_size = (-1)   
