README.txt
Mary Perkins and Stefanie Reed

Description:

This is the code for the paper "Assessing the Linguistic Features of
Neural Conversational Models" by Mary Perkins and Stefanie Reed. It utilizes
Tensorflow's seq2seq model. The seq2seq model is not ours and belongs to
Tensorflow, the copyright statement can be viewed in the file seq2seq_model.py.
This code includes the saved parameters for the best models we found for
English and for Spanish. The parameters can be loaded and utilized for
prediction purposes. The file exe.py is capable of running these trained
models in prediction mode-- which is further discussed in the Operating
Instructions section. Although this program is meant to run on the models
that we have already trained-- all preprocessing and training files are 
included as well.




File Descriptions:

final
	Directory- contains all preprocessing data files some are necessary 
	for training and testing. Also saved best Spanish model and best 
	English model are within this direction.

badword_list.py 
	Used for preprocessing - contains words that needed to be filtered out

decode.py
	Used to run the trained models. Predicts the response

exe.py
	The driver file.

logs.py
	Used for preprocessing - logs

prepare_exe.py
	Used to execute preprocessing step.

prepare_helpers.py
	Used for preprocessing and decode. Contains helper functions.

preprocess_exe.py
	Used to execute another preprocessing step

preprocess_helpers.py
	Used for preprocessing only. Contains helper functions.

seq2seq.ini
	Configuration file for English chatbot

seq2seq_model.py
	Contains the Tensorflow seq2seq model

seq2seq_sp.ini
	Configuration file for Spanish chatbot

train.py
	Used for training. 




System Requirements:

Python 2.7
Tensorflow 0.12



Operating Instructions:

1. File paths in exe.py, seq2seq.ini, and seq2seq_sp.ini need to be changed.
2. To use the Spanish chatbot change the mode flag inside of train.py 
AND exe.py (located near top of file) to 0.
To use the English chatbot change the mode flag inside of train.py AND
exe.py to 1.
3. ONLY after all system requirements have been met, and step 1 + 2 have been
carried out, the program can be run in prediction mode. Run the 
prediction mode by typing "python exe.py" at the command line. 
A Command Line prompt will appear. All input will be treated as a query
into the model, and the model will give a predicted response to your
query. 

