# 1 main_str = input()
# 2 count = 0
# 3 sum = 0
# 4 lenght_of_sequence = 0
# 5 while count < len(num):
    if main_str[count] == '0':
        sum += 1
        if sum > lenght_of_sequence:
            lenght_of_sequence = sum
    if main_str[count] == '1':
        sum = 0
    count += 1
# 6 print(lenght_of_sequence)
