def solution(gst , pan):
    from_gst = gst[2:2+10]
    return from_gst.upper() == pan.upper()

print(solution('29AACCC6016B1Z4','AACCC6016B'))
