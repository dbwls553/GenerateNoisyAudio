import os
import io_function as iof
import signal as sp

input_file_dir = './'
noise_file_dir = './'
output_file_dir = './'
snr_or_ssnr = 'snr'
target_snr = 10
target_ssnr = 10
frame_size = 1600


input_is_dir = os.path.isdir(input_file_dir)
noise_is_dir = os.path.isdir(noise_file_dir)

if input_is_dir:
    input_file_list = iof.read_dir_list(input_file_dir, extention='wav')
else:
    input_file_list = [input_file_dir]

if noise_is_dir:
    noise_file_list = iof.read_dir_list(noise_file_dir, extention='wav')
else:
    noise_file_list = [noise_file_dir]

old_sample_rate = 0
temp_sample_rate = 0
noise_sign al_train = []
for wav_file in noise_file_list:
    iof.read_wav(wav_file)