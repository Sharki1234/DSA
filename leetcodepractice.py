num = 9

def power_of_3(value):
    if value == 1:
        return True
    if value%3 == 0 and value != 0:
        return(power_of_3(value/3))
    return False
print(power_of_3(num))

   

    