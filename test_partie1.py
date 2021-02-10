import partie1 as source
import numpy as np

def printResult(testName,result,nTest,total):
    if result:
        color = "\033[32m Success \033[0m"
    else:
        color = "\033[31m Failure \033[0m"
    print("         "+color+" "+testName+" test number:"+str(nTest)+"/"+str(total))
    return result

def test_rp():
    print("test rp(x,p)")
    total = 8
    printResult("rp(pi,4)",source.rp(3.141592658,4)==3.142,1,total)
    printResult("rp(0.000650104200,5)",source.rp(0.000650104200,5)==0.00065010,2,total)
    printResult("rp(2568415,3)",source.rp(2568415,3)==2570000,3,total)
    printResult("rp(-0.011,5)",source.rp(-0.011,5)==-0.011,4,total) #error
    printResult("rp(-0.0758998,5)",source.rp(-0.0758998,5)==-0.075900,5,total) #error
    printResult("rp(57,3)",source.rp(57,3)==57,6,total)
    printResult("rp(1,3)",source.rp(1,3)==1,7,total)
    printResult("rp(0,7)",source.rp(0,7)==0,8,total) #error
    print("\n")

def test_add():
    print("test add(a,b,p)")
    total = 7
    printResult("add(1/3,2/3,5)",source.prec_add(1/3,2/3,5)==1,1,total) 
    printResult("add(0.33333,0.66666,5)",source.prec_add(0.33333,0.66666,5)==0.99999,2,total)
    printResult("add(-1/3,0.33333,5)",source.prec_add(-1/3,0.33333,5)==0,3,total) #error
    printResult("add(-2/3,0.66666,5)",source.prec_add(-2/3,0.66666,5)==-0.00001,4,total) #error
    printResult("add(2/3,-0.66666,5)",source.prec_add(2/3,-0.66666,5)==0.00001,5,total) #error
    printResult("add(123.45,0.006789,4)",source.prec_add(123.45,0.006789,4)==123.5,6,total) #failure
    printResult("add(0,5/3,5)",source.prec_add(0,5/3,5)==1.6667,7,total) #error
    print("\n")

def test_prod():
    print("test prod(a,b,p)")
    total = 6
    printResult("prod(1/3,3,6)",source.prec_prod(1/3,3,6)==0.999999,1,total) #failure
    printResult("prod(2/3,3,6)",source.prec_prod(2/3,3,6)==2,2,total) #failure
    printResult("prod(0.66667,3,6)",source.prec_prod(0.66667,3,6)==2.00001,3,total)
    printResult("prod(5/9,0,5)",source.prec_prod(5/9,0,5)==0,4,total) #error
    printResult("prod(-0.2,0.999,3)",source.prec_prod(-0.2,0.999,3)==-0.2,5,total) #error
    printResult("prod(-0.2,0.999,4)",source.prec_prod(-0.2,0.999,4)==-0.1998,6,total) #error
    print("\n")

test_rp()
test_add()
test_prod()
test_log()