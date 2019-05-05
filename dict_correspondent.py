import numpy as np
file_name = 'part_names.txt'


def read_dict(filename):
    output_dict = {}
    keys = []
    values = []
    with open(filename, 'r') as readfile:
        for i,line in enumerate(readfile.readlines()):
            if i%2==0:
                keys.append(line.strip())
            else:
                values.append(line.strip())
    for key, value in zip(keys,values):
        output_dict[key] = value
    return output_dict


all_war_short = read_dict(file_name)
def replace_not_exist(all_war_freq):
    keys = []
    values = []
    for key, value in all_war_freq.items():
        if key in all_war_short:
            keys.append(all_war_short[key])
        else:
            keys.append(key)
        values.append(value)
    return keys, values


def get_percentage(all_war_freq):
    total = 0
    percent = []
    for val in all_war_freq.values():
        total+=val

    for value in all_war_freq.values():
        percent.append(np.divide(np.multiply(100,value),total))
    return percent


def print_out(all_month_dicts):
    for key in all_month_dicts:
        if key not in all_war_short:
            print(key)


def write_dict(dicts):
    with open(file_name,'a') as write_file:
        for key in dicts:
            write_file.write(key + '\n')



def write_list(input_list, file_name):
    with open(file_name,'a') as write_file:
        for value in input_list:
            write_file.write(value + '\n')


def read_list(file_name):
    output = []
    with open(file_name,'r') as read_file:
        for value in read_file.readlines():
            output.append(value.strip())

    return output