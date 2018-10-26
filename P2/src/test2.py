#!/usr/local/bin/python
# coding: latin-1

import io


file = io.open('../datasets/training_data.csv', 'r', encoding='latin-1')
training_data = file.readlines()

print training_data[3]

c = training_data[3][9]
print c

