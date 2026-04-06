



x = [1,2,3,4]
y = [2,4,6,8]
m = 0
c = 0


learning_rate = 0.01
total_error = 0
average_error= 1
while average_error>0.00000001:
    total_error = 0
    dm = 0
    dc = 0 
    for i in range(len(x)):
        num = m*x[i]+c
        error = (y[i]-num)
        total_error+=error**2
        dm +=  x[i] * error * -2
        dc +=   error * -2

    m = m- learning_rate*dm/len(x)
    c =c- learning_rate* dc/len(x)
    
    
    average_error = total_error/len(x)
   
    
print(m,c)

