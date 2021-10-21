from datetime import datetime
nemo_list = ['nemo']
large_nemo = []

for x in range(1000000):
    val = 'nemo'
    large_nemo.append(val)


def findnemo(inp):
    t0 = datetime.now()

    for i in inp:
        if i == 'nemo':
            print("Found NEMO")
        else:
            print("NEMO not found")

    t1 = datetime.now()
    diff = t1 - t0
    print('Small', diff)

def findlargenemo(large_inp):
    t0 = datetime.now()

    for i in large_inp:
        if i == 'nemo':
            print("Found NEMO")
        else:
            print("NEMO not found")

    t1 = datetime.now()
    diff = t1 - t0
    print('large', diff)


findnemo(nemo_list)
findlargenemo(large_nemo)
