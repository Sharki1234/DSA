x = [1,2,3,4,5]
y = [8,13,20,29,40]
learningrate = 0.001
threshold = 0.00001
average_error = 1

m1 = 0
m2 = 0
c = 0

while average_error>threshold:
    total_error = 0
    dm1 = 0
    dm2 = 0
    dc = 0
    for i in  range(len(x)):
        prediction =( m1*(x[i]**2))+(m2*x[i]) + c
        error = (y[i] - prediction)
        dm1 += -2 * (x[i] **2) * error
        dm2 += -2 * (x[i]) * error
        dc += -2 * error
        total_error += (error**2)
    m1 -= learningrate*dm1/len(x)
    m2 -= learningrate*dm2/len(x)
    c-= learningrate*dc/len(x)
    average_error = total_error/len(x)

test = 6
test_y =( m1*(test**2))+(m2*test) + c
print(test_y)