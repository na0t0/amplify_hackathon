from blockext import run, reporter, command
import combinatorialOptimization4

global Res0
global Res1
Res0=""
Res1=""
A=""

@command("set list %s")
def set_list(m):
    global A
    A = m.split(" ")
    print(A)

    global Res0
    global Res1
    
    Res0 = ""
    Res1 = ""
    
    Res0, Res1 = combinatorialOptimization4.comb1_main(A)

@reporter("get list1")
def get_list1():
    return ((Res0.replace("'","")).replace("[","")).replace("]","")

@reporter("get list2")
def get_list2():
    return ((Res1.replace("'","")).replace("[","")).replace("]","")

if __name__ == "__main__":
    run("CombinationOptimization", "CombinationOptimization", 1234)