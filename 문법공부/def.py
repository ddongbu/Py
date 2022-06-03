def add_mul(choise,*args):
    if choise == "add":
        result = 0
        for i in args:
            result += i
    elif choise == "mul":
        result = 1
        for i in args:
            result*=i
    else:
        result = None

    return result

a = add_mul("add",1,2,3)
b= add_mul("mul",1,2,3,4,5,6)
print(a, "/",b)