from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys, os


final_directory = '/Users/smokey/LIGN165_finalproject/final/'

english_file = 'preprocess_logs_English.txt'
spanish_file = 'preprocess_logs_Spanish.txt'

def log(sample_num, msg, showID, mode):

  if (showID.find('English') != -1):
    preprocess_file = english_file
  else:
    preprocess_file = spanish_file

  if mode == 'preprocess':
    path = os.path.join(final_directory, preprocess_file)

  f = open(path, 'a+')
  
  f.write((str(sample_num) + ' ' + showID + ' ---> ' + msg))

  f.close()

      
