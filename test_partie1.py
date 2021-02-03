import partie1 as source

def printResult(testName,result,nTest,total):
    if result:
        color = "\033[32m Success \033[0m"
    else:
        color = "\033[31m Failure \033[0m"
    print(color+" "+testName+" test number:"+str(nTest)+"/"+str(total))


def test_rp():
    total = 3
    printResult("rp(pi,4)",source.rp(3.141592658,4)==3.142,1,total)
    printResult("rp(0.000650104200,5)",source.rp(0.000650104200,5)==0.00065010,2,total)
    printResult("rp(0,7)",source.rp(0,5)==0,3,total)
test_rp()