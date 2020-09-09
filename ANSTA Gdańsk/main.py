import time
import sys
from itertools import chain


"""
    TASK 1:
    GENERATOR KODÓW POCZTOWYCH
    przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""
def generate_postals(start, end):
    pre_start, post_start = list(map(lambda x:int(x), start.split('-')))
    pre_end, post_end = list(map(lambda x:int(x), end.split('-')))
    prefixes = [i for i in range(pre_start, pre_end + 1)]
    postals = {pre_start: [post_start, 999]}  # First postal

    # Catching postal codes between 'start' and 'end' postals
    mid_prefixes = prefixes[1:-1]
    for prefix in mid_prefixes:
        postals[prefix] = [0, 999]
        
    postals[pre_end] = [0, post_end]  # Last postal
    for prefix, scope in postals.items():
       yield (str(prefix) + '-' + str(i) 
                    if i > 99  else (str(prefix) + '-0' + str(i)
                        if i > 9 else str(prefix) + '-00' + str(i))
                            for i in range(scope[0], scope[1] + 1))

def task_1():
    print("\nTASK 1\n")
    start = '79-900'
    end = '80-155'
    start_time = time.time()
    memory = []
    for g in generate_postals(start, end):
        print(*g, sep=' | ', end=' | ')
        memory.append(sys.getsizeof(g))
    
    durration = time.time() - start_time
    print("\n\nFrom {} to {} in {:.10f} seconds with only {} bytes.".format(start, end, durration, sum(memory)))



"""
    TASK 2:
    PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
"""
def lacking_elements(array, n):
    return [i for i in range(1, n + 1) if i not in array]

def task_2():
    input_list = [2,3,7,4,9]
    n = 10
    print("\nTASK 2:\n")
    print("Input data:\nList: {}\nN = {}".format(input_list, n))
    print("Missing elements:", lacking_elements(input_list, n))


"""
    TASK 3:
    NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
"""
def generate_list(start, end, step):
    return [i / 10 for i in range(int(start*10), int(end*10) + 1, int(step*10))]

def task_3():
    start = 2
    end = 5.5
    step = .5
    print("\nTASK 3:")
    print("\nFrom {} to {} with step of {}".format(start, end, step))
    result = generate_list(start, end, step)
    print("Result =", result)
    print("\nDetails:")
    [print("Item  {}  is type of  {}".format(i, type(i))) for i in result]


def main():
    task_1()
    task_2()
    task_3()
    print("")

if __name__ == '__main__':
    main()

# Author: Marcin Hebdzyński
# Email: hebdzynski.m@gmail.com