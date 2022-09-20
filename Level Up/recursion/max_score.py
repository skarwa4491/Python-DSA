import sys
sys.setrecursionlimit(10**6)

# incorrect solution
def solution(words , letters , score , idx):
    '''
        leet code 1255
    '''
    if len(words) == idx:
        return 0
    score_no = solution(words , letters , score , idx+1)
    word = words[idx]
    is_included = True
    word_score = 0
    score_yes = 0
    word_index = 0
    for i,ch in enumerate(word,start=0):
        word_index = i
        try:
            index_pop = letters.index(ch)    
        except ValueError:
            is_included = False
            word_score = 0
            break
        popped_char = letters.pop(index_pop)
        word_score += score[ord(popped_char)-ord('a')]
        
    if is_included:
        score_yes = word_score + solution(words, letters, score , idx+1)
    
    for ch in range(word_index+1):
        letters.append(word[ch])
        
    return max(score_no , score_yes)
        

    
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(solution(words , letters , score , 0))