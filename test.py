import io_function as iof
import os

# iof.createFolder('input/folder1')
# iof.createFolder('input/folder2')
# iof.createFolder('noise/noise1')
# iof.createFolder('noise/noise2')
# iof.write_wav([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0],'input/test_input_1.wav',1)
# iof.write_wav([0.1,0.2,0.3,0.4,0.5],'input/test_input_2.wav',1)
# iof.write_wav([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8],'input/test_input_3.wav',1)
# iof.write_wav([0.1,0.2,0.3,0.4,0.5,0.6],'input/folder1/test_input_1.wav',1)
# iof.write_wav([0.1,0.2],'input/folder1/test_input_2.wav',1)
# iof.write_wav([0.1,0.2,0.3,0.4],'input/folder2/test_input_1.wav',1)
# iof.write_wav([0.1,0.2,0.3],'input/folder2/test_input_2.wav',1)
#
# iof.write_wav([0.001, 0.002, 0.003, 0.004, 0.005, 0.006],'noise/noise1/test_noise_1.wav',1)
# iof.write_wav([0.07, 0.08, 0.09],'noise/noise1/test_noise_2.wav',1)
# iof.write_wav([0.09, 0.08, 0.07],'noise/noise2/test_noise_1.wav',1)
# iof.write_wav([0.006, 0.005, 0.004, 0.003, 0.002, 0.001],'noise/noise2/test_noise_2.wav',1)


output_file_dir = './input'
output_is_dir = os.path.isdir(output_file_dir)
if output_is_dir:
    output_file_list = iof.read_dir_list(output_file_dir, extention='wav')
else:
    output_file_list = [output_file_dir]

for wav_file in output_file_list:
    temp_data, temp_sample = iof.read_wav(wav_file)
    print("{} | {}".format(wav_file, [round(i,3) for i in temp_data]))

output_file_dir = './output'
output_is_dir = os.path.isdir(output_file_dir)
if output_is_dir:
    output_file_list = iof.read_dir_list(output_file_dir, extention='wav')
else:
    output_file_list = [output_file_dir]

for wav_file in output_file_list:
    temp_data, temp_sample = iof.read_wav(wav_file)
    print("{} | {}".format(wav_file, [round(i,3) for i in temp_data]))