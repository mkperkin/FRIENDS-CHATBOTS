from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys, os
import re
from collections import Counter
import logs
import codecs
from unidecode import unidecode



def stripNonConversation(rawInputPath, rawOutputPath, badWords):
  rawData = open(rawInputPath, 'r')
  processedData = open(rawOutputPath,'w+')
  
  rawData.seek(0)

  regex1 = re.compile("\[(.*?)\]")
  regex2 = re.compile("\((.*?)\)")
  for line in rawData:
      line = re.sub(regex1, '', line)           # remove []
      line2 = re.sub(regex2, '', line)          # remove ()
      line3 = re.sub(r'[^\x00-\x7f]',r'', line2) # keep ascii chars only
      line3 = removeBadWords(line3, badWords)              # remove non-conversation lines 
      line3 = re.sub('^\s*\n$', '', line3)
      if(line3):  
          processedData.write(line3)
 
  processedData.close()
  rawData.close() 


def spanish_prep(rawInputPath, tmp_asciiPath, badWords):

  rawData = codecs.open(rawInputPath, 'r', encoding='utf-8')
  asciiData = open(tmp_asciiPath, 'w+', encoding='ascii')

  rawData.seek(0)
  
  for line in rawData:
      line = unidecode(line)
      asciiData.write(line)
  
  rawData.close()
  asciiData.close()


# private
def removeBadWords(line, badWords):
  for i in range(len(badWords)):
      line = re.sub(badWords[i], '', line)
  return line



# input must be striped for NonConversation
def findMostFreqSpeaker(rawProcessedPath):

  rawData = open(rawProcessedPath, 'r')

  rawData.seek(0)
  names = []
  for line in rawData:
      end = line.find(':')
      if (end != -1):
          x = line[0:end]
          names.append(x)

  mostFreqActor = Counter(names).most_common(1)
  mostFreqActor= [name[0] for name in mostFreqActor]
  mostFreqActor = ''.join(mostFreqActor)

  rawData.close()
  
  return mostFreqActor



def separateData(rawProcessedPath, mostFreqActor, enc_dataPath, dec_dataPath, showID):
  
  rawData = open(rawProcessedPath,'r')
  enc_data = open(enc_dataPath, 'a+')
  dec_data = open(dec_dataPath,'a+')
  
  name = mostFreqActor + ':'   # mostFreqActor is name of speaker for decoder
  rawData.seek(0)       
  prev = rawData.readline()

  sample_num = 0;
  for line in rawData:
    start = line.find(name)

    if (start != -1):
        #make sure there is a matching response
        prev_idx = prev.find(":")
        if(prev_idx == -1):
            prev = line
            continue
        #if there is a matching response, write to files
        start = start + (len(name))
        target = line[start:]  # actual text for decoder
        removeActorNames(target)
        dec_data.write(target)


        name_speaker = prev[0:prev_idx] # name of speaker for encoder
        speaker = prev[prev_idx+1:]     # actual text for encoder
        removeActorNames(speaker)
        enc_data.write(speaker)
       
        # create seperate file to log actor id's
        msg = 'ENC_ACTORID = ' + mostFreqActor + '   DEC_ACTORID = ' + name_speaker + '\n'
        logs.log(sample_num, msg, showID, 'preprocess')
        sample_num = sample_num + 1
    
    prev = line


  dec_data.close() 
  enc_data.close()
  rawData.close()


#private
# last NonConversation text to be removed
def removeActorNames(line):
  end = line.find(':')
  if (end != -1):
      x = line[0:end+1]
            
      regex = "^(\s)*" + re.escape(x) + "(\s)*(\.)?(\s)*(\:)?"
      regex = re.compile(regex)
      re.sub(regex,'',line)
  return line 
