{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from __future__ import absolute_import\n",
    "from __future__ import division\n",
    "from __future__ import print_function\n",
    "\n",
    "import os\n",
    "\n",
    "from prepare_helpers import create_vocabulary, data_to_token_ids\n",
    "\n",
    "flag = 0 # 1 for english, 0 for spanish"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "directory = '/Users/smokey/LIGN165_finalproject/final/'\n",
    "if flag:\n",
    "    enc_rawPath = os.path.join(directory, 'enc_dataRaw_English.txt')\n",
    "    dec_rawPath = os.path.join(directory, 'dec_dataRaw_English.txt')\n",
    "    enc_vocabPath = os.path.join(directory, 'enc_vocab_English.txt')\n",
    "    dec_vocabPath = os.path.join(directory, 'dec_vocab_English.txt')\n",
    "    enc_trainPath = os.path.join(directory, 'enc_train_English.txt')\n",
    "    dec_trainPath = os.path.join(directory, 'dec_train_English.txt')\n",
    "    \n",
    "else:\n",
    "    enc_rawPath = os.path.join(directory, 'enc_dataRaw_Spanish.txt')\n",
    "    dec_rawPath = os.path.join(directory, 'dec_dataRaw_Spanish.txt')\n",
    "    enc_vocabPath = os.path.join(directory, 'enc_vocab_Spanish.txt')\n",
    "    dec_vocabPath = os.path.join(directory, 'dec_vocab_Spanish.txt')\n",
    "    enc_trainPath = os.path.join(directory, 'enc_test_Spanish.txt')\n",
    "    dec_trainPath = os.path.join(directory, 'dec_test_Spanish.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Creating vocabulary /Users/smokey/LIGN165_finalproject/final/enc_vocab_Spanish.txt from /Users/smokey/LIGN165_finalproject/final/enc_dataRaw_Spanish.txt\n",
      "  processing line 1000\n",
      "  processing line 2000\n",
      ">> Dataset number of samples : 2427\n",
      ">> Full Vocabulary Size : 4235\n",
      "Tokenizing data in /Users/smokey/LIGN165_finalproject/final/enc_dataRaw_Spanish.txt\n",
      "    Tokenizing line 1000\n",
      "    Tokenizing line 2000\n"
     ]
    }
   ],
   "source": [
    "# for encoder \n",
    "\n",
    "# create vocab\n",
    "create_vocabulary(enc_vocabPath, enc_rawPath, 10000000)\n",
    "# create training set\n",
    "data_to_token_ids(enc_rawPath, enc_trainPath, enc_vocabPath)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Creating vocabulary /Users/smokey/LIGN165_finalproject/final/dec_vocab_Spanish.txt from /Users/smokey/LIGN165_finalproject/final/dec_dataRaw_Spanish.txt\n",
      "  processing line 1000\n",
      "  processing line 2000\n",
      ">> Dataset number of samples : 2427\n",
      ">> Full Vocabulary Size : 4183\n",
      "Tokenizing data in /Users/smokey/LIGN165_finalproject/final/dec_dataRaw_Spanish.txt\n",
      "    Tokenizing line 1000\n",
      "    Tokenizing line 2000\n"
     ]
    }
   ],
   "source": [
    "# for decoder\n",
    "\n",
    "create_vocabulary(dec_vocabPath, dec_rawPath, 10000000)\n",
    "# create vocab\n",
    "data_to_token_ids(dec_rawPath, dec_trainPath, dec_vocabPath)\n",
    "# create training set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
