 # question : How many sentences
def countSentences(wordSet, sentences):
    # Write your code here
    word_map = {}
    for word in wordSet:
        temp = tuple(sorted(word))
        word_map[temp] = word_map.get(temp,0)+1
    ans = [1] * len(sentences)
    for i in range(len(sentences)):
        for word in sentences[i].split():
            key = tuple(sorted(word))
            if key in word_map:
                ans[i]*=word_map[key]
    return ans

if __name__ == '__main__':
    wordSet_count = int(input().strip())

    wordSet = []

    for _ in range(wordSet_count):
        wordSet_item = input()
        wordSet.append(wordSet_item)

    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    result = countSentences(wordSet, sentences)