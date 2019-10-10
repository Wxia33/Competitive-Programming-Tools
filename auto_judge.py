import os
import sys

file_name = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

file_result = "file_result.txt"


with open(input_file) as f_input:
    split_in_file = f_input.read().split("\n")
    print(split_in_file)

input_args = []
input_set = []
for i in split_in_file:
    if i == '':
        input_args.append(input_set)
        input_set = []
    else:
        input_set.append(i)
if input_set:
    input_args.append(input_set)

outputs = []
with open(output_file) as f_output:
    split_out_file = f_output.read().split("\n")
    print(split_out_file)

output_args = []
output_set = []
for i in split_out_file:
    if i == '':
        output_args.append(output_set)
        output_set = []
    else:
        output_set.append(i)
if output_set:
    output_args.append(output_set)

#os.system("cat input_file.txt | python script.py > file_result.txt")
try:
    os.system("mkdir test_cases")
except:
    pass

for case in range(len(input_args)):
    test_case = "test_case_" + str(case) + ".txt"
    test_file = open("./test_cases/" + test_case, "w")
    for inputs in input_args[case]:
        test_file.write(inputs)
    test_file.close()

try:
    os.system("mkdir results")
except:
    pass

for ind, test_cases in enumerate(os.listdir("./test_cases/")):
    cat_str = "cat " \
              + "./test_cases/" + test_cases + " | " + "python " \
              + file_name + " > ./results/result_" + str(ind) + ".txt"
    os.system(cat_str)
