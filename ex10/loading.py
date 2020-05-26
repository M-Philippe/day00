import time


def ft_progress(listy):
    start = time.process_time()
    line = None
    for a in listy:
        line = "[" + str(int(((a+1)/len(listy))*100)) + "%]"\
                + " [" + str(a+1) + "/" + str(len(listy)) + "]  "\
                + "elapsed time : " + str(time.process_time())
        print(line)
        yield a


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print(ret)
