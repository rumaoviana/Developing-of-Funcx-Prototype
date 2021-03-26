import xlwt
import time
import numpy as np
#from PIL import Image
start3 = time.time()
from funcx.sdk.client import FuncXClient
fxc = FuncXClient()
end3 = time.time()
exec_time3 = ((end3 - start3) * 1000)
print(exec_time3)
fxc.throttling_enabled = False
high = 10
low = 5
m,n = 100,100
a = (high - low)*np.random.rand(m,n) + low
def complex(a):
    return a
n = 2000
estimate = []
start1 = time.time()
hello_function = fxc.register_function(complex)
end1 = time.time()
registertime = ((end1 - start1) * 1000)
print("The register time is:", registertime)
index = 1
book = xlwt.Workbook()
sheet = book.add_sheet('data', cell_overwrite_ok=True)
sheet.write(0,0,'exec_time3')
sheet.write(0,1,'registertime')
sheet.write(0,2,'runtime')
sheet.write(0,3,'exec_time')
for i in range (0, n):
    #start1 = time.time()
    #hello_function = fxc.register_function(matrix)
    #end1 = time.time()
    #registertime = ((end1 - start1) * 1000)
    #print("The register time is:", registertime)
    #high = 10
    #low = 5
    #m,n = 2,2
    #a = (high - low)*np.random.rand(m,n) + low
    start2 = time.time()
    #a = (high - low)*np.random.rand(m,n) + low
    # res = fxc.run(items, endpoint_id='7601789e-8569-413f-be3e-e573d04c5799', function_id=sum_function)
    res = fxc.run(a, endpoint_id='d25d7886-6112-4f05-b3bd-0625cc61e6e8', function_id=hello_function)
    end2 = time.time()
    runtime = ((end2 - start2) * 1000)
    print("The runtime is:", runtime)
    # get the raw json response
    start = time.time()
    result = fxc.get(f"tasks/{res}") 
    while result['status'] != 'success':
        time.sleep(1)
        result = fxc.get(f"tasks/{res}")
    completion_time = result['completion_t']
    exec_time = (float(completion_time) - start) * 1000
    print("The function execution time is:", exec_time)
    # add the result to the list
    estimate.append(a)    #overhead.append(Overheadtime)
    sheet.write(index,0,exec_time3)
    sheet.write(index,1,registertime)
    sheet.write(index,2,runtime)
    sheet.write(index,3,exec_time)
    index +=1
book.save('Latencyreadingsforcomplexmatrix.csv')
#a = sum(overhead)
#avg1 = a / n 
#print("The Overhead average is:", avg1)
#b = sum(estimate)
#print ("the sum is:", b)
#avg = b / n
#print("The average is:", avg)
#print(estimate)



