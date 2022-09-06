mappings = {
    0: ".;",
    1: "abc",
    2: "def",
    3: "ghi",
    4: "jkl",
    5: "mno",
    6: "pqrs",
    7: "tu",
    8: "vwx",
    9: "yz"
}


def solution(s,ans):

    if len(s) == 0:
        print(ans)
        return
    
    ch = s[0]
    ros = s[1:]
    cr_map = mappings.get(int(ch))
    for cr in cr_map:
        solution(ros,ans+cr)

solution('786','')
