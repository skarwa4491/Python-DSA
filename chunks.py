# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



#
# Complete the 'minimumChunksRequired' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER totalPackets
#  2. 2D_LONG_INTEGER_ARRAY uploadedChunks
#

def minimumChunksRequired(totalPackets, uploadedChunks):
    

    def count_min_cunks_for_range(range_chunks):
        
        # count = 1
        # if range_chunks == 1:
        #     return 1
        # elif range_chunks > 2:
        #     uploaded_chunk = 2
        #     while range_chunks > 1:
        #         range_chunks -= uploaded_chunk
        #         uploaded_chunk *=2
        # if uploaded_chunk == 1:
        #     count+=1
        flag = True
        if range_chunks == 1:
            return 1
        else:
            while range_chunks != 1:
                if range_chunks % 2 != 0:
                    flag = False
                range_chunks=range_chunks//2
        if flag:
            return 1
        else:
            if range_chunks == 1:
                return 2
            else:
                return 0
        
    # Write your code here
    is_uploaded = [False]*(totalPackets+1)
    total_chunks = 0
    for uploaded in uploadedChunks:
        for i in range(uploaded[0],uploaded[1]+1):
            is_uploaded[i] = True
    
    i = 1
    while i < len(is_uploaded):
        if is_uploaded[i] == True:
            i+=1
            continue
        else:
            start = i
            range_chunks = 0
            while start < len(is_uploaded) and is_uploaded[start]==False:
                start+=1
                range_chunks+=1
            chunk = count_min_cunks_for_range(range_chunks)
            total_chunks+=chunk
            i += start
            
    return total_chunks

if __name__ == '__main__':

    totalPackets = int(input().strip())

    uploadedChunks_rows = int(input().strip())
    uploadedChunks_columns = int(input().strip())

    uploadedChunks = []

    for _ in range(uploadedChunks_rows):
        uploadedChunks.append(list(map(int, input().rstrip().split())))

    result = minimumChunksRequired(totalPackets, uploadedChunks)
    print(result)