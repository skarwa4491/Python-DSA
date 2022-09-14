from curses import start_color
from xml.etree.ElementInclude import include


start_time = [1,1,2]
end_time = [3,2,4]

inc = [0]*len(start_time)
exc = [0]*len(end_time)

inc[0] = 1

for i in range(1, len(start_time)):
    if end_time[i-1] <= start_time[i]:
        inc[i] = inc[i-1]+1
    else:
        inc[i] = exc[i-1]+1
    exc[i] = max(inc[i-1], exc[i-1])
    
print(max(inc[-1],exc[-1]))
    