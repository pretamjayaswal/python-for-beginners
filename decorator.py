def mylog(x):
    def outer(func):
        def wrapper():
            print(x)
            for _ in range(x):
                print("--Logged--"+ str(_))
                func()
        return wrapper
    return outer

@mylog(10)
def main():
    print('MAIN CODE EXECUTED')

#  main = mylog(2)(main)



main()