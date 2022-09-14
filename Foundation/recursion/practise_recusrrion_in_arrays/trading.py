import string


s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
map = {i: val for i, val in enumerate(s, start=1)}


def numbers_to_letters(s):
    if s is None:
        return s

    if len(s) == 1 and int(s) != 0 and int(s) <= 26:
        return map.get(s)

    s_arr = s.split(' ')
    ans = ''

    for ch in s_arr:
        if '+' in ch:
            ch_arr = ch.split('+')
            for c in ch_arr:
                if int(c) <= 26 and int(c) != 0:
                    ans = ans+map[int(c)]

        elif int(ch) <= 26 and int(ch) != 0:
            ans = ans+map[int(ch)]

    return ans


if __name__ == "__main__":
    print(numbers_to_letters('20 5 19 20+4 15 13 5'))
