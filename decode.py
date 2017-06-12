from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from train import get_config, create_model, _buckets
from prepare_helpers import initialize_vocabulary, EOS_ID, sentence_to_token_ids
import numpy as np
import tensorflow as tf
import math
import random
import time

from six.moves import xrange  # pylint: disable=redefined-builtin

import sys
import os


def decode(enc_path, dec_path):

  # Only allocate part of the gpu memory when predicting.
 # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
 # config = tf.ConfigProto(gpu_options=gpu_options)

  with tf.Session() as sess:
    # Create model and load parameters.
    model = create_model(sess, True)
    model.batch_size = 1  # We decode one sentence at a time.


    enc_vocab, _ = initialize_vocabulary(enc_path)
    _, rev_dec_vocab = initialize_vocabulary(dec_path)

    # Decode from standard input.
    sys.stdout.write("> ")
    sys.stdout.flush()
    sentence = sys.stdin.readline()
    while sentence:
      # Get token-ids for the input sentence.
      token_ids = sentence_to_token_ids(tf.compat.as_bytes(sentence), enc_vocab)
      # Which bucket does it belong to?
      bucket_id = min([b for b in xrange(len(_buckets))
          if _buckets[b][0] > len(token_ids)])
      # Get a 1-element batch to feed the sentence to the model.
      encoder_inputs, decoder_inputs, target_weights = model.get_batch(
          {bucket_id: [(token_ids, [])]}, bucket_id)
      # Get output logits for the sentence.
      _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                       target_weights, bucket_id, True)
      # This is a greedy decoder - outputs are just argmaxes of output_logits.
      outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
      # If there is an EOS symbol in outputs, cut them at that point.
      if EOS_ID in outputs:
        outputs = outputs[:outputs.index(EOS_ID)]
      # Print out French sentence corresponding to outputs.
      print(" ".join([tf.compat.as_str(rev_dec_vocab[output]) for output in outputs]))
      print("> ", end="")
      sys.stdout.flush()
      sentence = sys.stdin.readline()


