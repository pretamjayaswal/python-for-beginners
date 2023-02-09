# input a binanry number and check divisibility with 5
num = input("Binary Number: ")

int_num = int(str(num),2)

if int_num % 5 == 0:
    print(f'{num} or {int_num}(decimal) is divisible by 5')
else:
    print(f'{num} or {int_num}(decimal) is NOT divisible by 5')