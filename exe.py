from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os 
import sys
import tensorflow as tf
from decode import decode
from train import get_config

# 0 is spanish 1 is english
mode = 0

if __name__ == '__main__':
    
    enc_vocab_path_Eng = '/Users/smokey/LIGN165_finalproject/final/enc_vocab_English.txt'
    dec_vocab_path_Eng = '/Users/smokey/LIGN165_finalproject/final/dec_vocab_English.txt'
   
    enc_vocab_path_Sp = '/Users/smokey/LIGN165_finalproject/final/enc_vocab_Spanish.txt'
    dec_vocab_path_Sp = '/Users/smokey/LIGN165_finalproject/final/dec_vocab_Spanish.txt'
    

    if mode == 0:
        gConfig = get_config('seq2seq_sp.ini')
        decode(enc_vocab_path_Sp, dec_vocab_path_Sp)
    elif mode:
        gConfig = get_config('seq2seq.ini')
        decode(enc_vocab_path_Eng, dec_vocab_path_Eng)
    else:
        # wrong way to execute "serve"
        #   Use : >> python ui/app.py
        #           uses seq2seq_serve.ini as conf file
        print('Serve Usage : >> python ui/app.py')
        print('# uses seq2seq_serve.ini as conf file')
