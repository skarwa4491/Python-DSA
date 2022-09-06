
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

def vanity(codes, numbers):
    # Write your code here
    map ={
        2:"ABC",
        3:"DEF",
        4:"GHI",
        5:"JKL",
        6:"MNO",
        7:"PQRS",
        8:"TUV",
        9:"WXYZ"
    }
    number = ""
    results = []
    for code in codes:
        for ch in code:
            for key,value in map.items():
                if ch in value:
                    number+=str(key)
                    break
        results.append(number)
        number=''
        
    matched_numbers = []
    
    for number in numbers:
        for result in results:
            if result in number and number not in matched_numbers:
                matched_numbers.append(number)
                
    return matched_numbers






if __name__ == '__main__':
    codes_count = int(input().strip())
    codes = []
    for _ in range(codes_count):
        codes_item = input()
        codes.append(codes_item)

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = input()
        numbers.append(numbers_item)

    result = vanity(codes, numbers)
    print(result)
