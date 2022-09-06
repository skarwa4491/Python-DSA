# incomplete
def max_profit(arr):
    bsp = -arr[0]
    ssp = 0
    cool = 0

    for i in range(1, len(arr)):
        nssp, nbsp, = 0, 0
        if (bsp - arr[i] > bsp):
            nbsp = bsp - arr[i]
        else:
            nbsp = bsp
