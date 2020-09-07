import time
import sys
from itertools import chain

"""
    TASK 1:
    GENERATOR KODÓW POCZTOWYCH
    przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
"""
def postal_codes(start, end):
    prefix_start, postfix_start = start.split("-")
    prefix_end, postfix_end = end.split("-")
    postal_codes_list_1 = (prefix_start + "-" + str(i)
                            for i in range(int(postfix_start), 1000, 1))

    postal_codes_list_2 = (prefix_end + "-" + str(i)
                            if len(str(i)) == 3
                                else (prefix_end + "-0" + str(i)
                                    if len(str(i)) == 2
                                        else prefix_end + "-00" + str(i))
                                            for i in range(0, int(postfix_end) + 1, 1))
    
    return chain(postal_codes_list_1, postal_codes_list_2)

def task_1():
    start = "79-990"
    end = "80-155"
    start_time = time.time()
    result = postal_codes(start, end)
    print("\nTASK 1:\n")
    print("Input data:", "\nFirst postal code =", start, "\nLast postal code =", end, "\n\nResults:")
    pricessing_time = time.time() - start_time
    print("Processing time (in seconds) =", pricessing_time)
    print("Memory =", sys.getsizeof(result))
    print("\nNumber of postal codes =", len(result))
    print(*result, sep=' | ')
    print(type(result))


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
    print("Input data:", "\nList =", input_list, "\nN =", n)
    print("\nResult =", lacking_elements(input_list, n))


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
    print("\nTASK 3:\n")
    print("Input data:", "\nStart =", start, "\nEnd =", end, "\nStep =", step)
    result = generate_list(start, end, step)
    print("\nResult =", result, "\nDetails:")
    [print("Item =", i, "| Type:", type(i)) for i in result]


def main():
    task_1()
    task_2()
    task_3()
    print("")

if __name__ == '__main__':
    main()