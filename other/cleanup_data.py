#!/usr/bin/env python3
import errno
import glob
import os

path = '/path/to/your/files/'
files = glob.glob(path + '/*.txt')
output_file_name = 'output_data.txt'
start_prefix = '<|startoftext|>'
end_prefix = '<|endoftext|>'


def remove_non_ascii(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])


if os.path.exists(output_file_name):
    os.remove(output_file_name)

for name in files:
    try:
        with open(name) as input_file:
            data = input_file.read()
            start_index = data.find(start_prefix) + len(start_prefix)
            end_index = data.find(end_prefix)

            while start_index != -1 & end_index != -1:
                single_story = remove_non_ascii(data[start_index:end_index])
                data = data[end_index + len(end_prefix):len(data)]

                output_file = open(output_file_name, "a")
                output_file.write("%s" % single_story)
                output_file.close()

                start_index = data.find(start_prefix) + len(start_prefix)
                end_index = data.find(end_prefix)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
