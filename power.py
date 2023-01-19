def pow(num, topower):
    if topower == 0:
        return 1
    else:
        return num * pow(num , topower - 1)


print(pow(5,1))