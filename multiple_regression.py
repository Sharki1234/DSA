x1 = [1,2,3,4]
x2 = [2,4,6,8]
y = [5,9,13,17]

m1 = 0
m2 = 0
c = 0

learningrate = 0.0001
average_error = 1
threshold = 0.00001

while average_error>threshold:
    total_error = 0
    dm1 = 0
    dm2 = 0
    dc = 0
    for i in range(len(x1)):
        prediction = (m1*x1[i])+(m2*x2[i])+c
        error = y[i] - prediction
        total_error+=error**2
        dm1 += -2*error*x1[i]
        dm2 +=-2*error*x2[i]
        dc+=-2*error
    m1-=learningrate*dm1/len(x1)
    m2-=learningrate*dm2/len(x1)
    c-=learningrate*dc/len(x1)
    average_error = total_error/len(x1)
print(m1,m2,c)