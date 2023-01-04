file = open(r'dataset/rosalind_ini3.txt')

input_string = file.read()
output_string = input_string[24: 36 + 1] + ' ' + input_string[105: 111 + 1]

print(output_string)
