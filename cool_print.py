import time

def cool_print(target, length):

    step = length / len(target)
    
    for i in target:
        print(i, end="")
        time.sleep(step)
