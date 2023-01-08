# -*- coding: utf-8 -*-
"""cryptoXORandOneTimePad.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IIJz0U6-pS90yD0O2xMRPdWbVkTHkYY6
"""

def xor(x,s):
  print(bin(x), 'xor',s,'=',x^s)

xor(4,8)
xor(4,12)
xor(3,6)
xor(1,2)

import random
def generate_key_stream(n):
  
 def xor_bytes(key_stream,message):
  length = min(len(key_stream), len(message))
  return bytes([key_stream[i]^message[i] for i in range(length)])

  message = "YOU ARE AWESOME"
  message = message.encode()
  key_stream = generate_key_stream(len(message))
  cipher = xor_bytes(key_stream, message)
  print(key_stream)
  print(cipher)
  print(xor_bytes(key_stream,cipher))