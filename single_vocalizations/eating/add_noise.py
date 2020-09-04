#!/usr/bin/env python
# Adds fs seconds of silence to all of the files in the current directory to make them T seconds long
# Usage: python3 add_noise.py 3

from __future__ import print_function, division
import scipy.io.wavfile as wavf
import numpy as np
from sys import argv
import os

def pad_audio(data, fs, T):
    # Calculate target number of samples
    N_tar = int(fs * T)
    # Calculate number of zero samples to append
    shape = data.shape
    # Create the target shape    
    N_pad = N_tar - shape[0]
    print("Padding with %s seconds of silence" % str(N_pad/fs) )
    shape = (N_pad,) + shape[1:]
    # Stack only if there is something to append    
    if shape[0] > 0:                
        if len(shape) > 1:
            return np.vstack((np.zeros(shape),
                              data))
        else:
            return np.hstack((np.zeros(shape),
                              data))
    else:
        return data

if __name__ == "__main__":
    if len(argv) != 2:
        print("Wrong arguments.")
        print("Use: %s target_time_s" % argv[0])
    else:
    	#directory = argv[1]
        #in_wav = argv[1]
        T = float(argv[1]) 
        for file_name in os.listdir(os.getcwd()):
        	out_wav = str(T) + "secs" + file_name 
        	if file_name.endswith(".wav"): 
		        # Read the wav file
		        fs, in_data = wavf.read(file_name)
		        # Prepend with zeros
		        out_data = pad_audio(in_data, fs, T)
		        # Save the output file
		        wavf.write(out_wav, fs, out_data)