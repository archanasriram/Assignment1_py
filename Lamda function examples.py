#lambda<arguments>:<expression>
import math # Assigning Lambda to a variable
sqrt_lambda=lambda x:math.sqrt(x)
result= sqrt_lambda(25)
print(result)
#Passing multiple values
get_sum=lambda x,y:x+y
print(get_sum(4,7))
#Comprehensions replace map,filter and reduce
##map
random_list=[2345,678,256,987,9874]
map(lambda x:x**2,random_list)
for i in map(lambda x:x**2,random_list):
    print(i)

    