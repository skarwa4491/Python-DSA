from collections import defaultdict
import sys


def smallestNegativeBalance(debts):

    # Write your code here
    borrower_map = {}
    lender_map = {}
    for txn in debts:
        if(borrower_map.get(txn[0])):
            borrower_map.update(
                {txn[0]: int(borrower_map.get(txn[0]))+int(txn[2])})
        else:
            borrower_map.update({txn[0]: int(txn[2])})
        if(lender_map.get(txn[1])):
            lender_map.update(
                {txn[1]: int(lender_map.get(txn[1]))+int(txn[2])})
        else:
            lender_map.update({txn[1]: int(txn[2])})

    result = []
    for person, value in borrower_map.items():
        if person in lender_map.keys() and person in borrower_map.keys():
            value = lender_map[person]-borrower_map[person]
        elif person in lender_map.keys():
            value = lender_map[person]
        elif person in borrower_map.keys():
            value = borrower_map[person]*-1
        
        if value < 0:
            result.append(person)
    return result


if __name__ == '__main__':
    debts_rows = int(input().strip())

    debts_columns = int(input().strip())

    debts = []

    for _ in range(debts_rows):
        debts.append(input().rstrip().split())

    result = smallestNegativeBalance(debts)
    print(result)
