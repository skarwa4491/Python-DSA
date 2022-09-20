
def process_text(pid):
    with open('/Users/laptop-on-rent-011/Documents/DSA_Pyhton/palo alto networks/process.txt' , 'r') as f:
        for line in f.readlines():
            content = line.split('\t')
            if len(content) > 0:
                if content[0] == pid:
                    return content[1]
        return 'Top'

print(process_text('654768676'))
            
        