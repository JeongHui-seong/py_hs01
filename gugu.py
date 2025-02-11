import sys
args = sys.argv[1:]

for j in range(int(args[0][:-1]),int(args[1]) + int(args[0][:-1])):
    print(f"=========={j}단==========")
    for i in range(1,10):
        print(f"{j} * {i} = {j * i}")
    