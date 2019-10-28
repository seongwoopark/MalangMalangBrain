def solution(words):
    # create trie
    trie = {}
    for word in words:
        t = trie
        for char in word:
            # set trie by char
            if char not in t:
                t[char] = {}

            # count by char
            t[char]['count'] = t[char].get('count', 0) + 1

            # prepare next step
            t = t[char]

    # get answer
    answer = 0
    for word in words:
        i = 0
        for i, char in enumerate(word, start=1):
            # get trie node
            if i == 1:
                t = trie[char]
            else:
                t = t[char]

            # escape condition
            if t['count'] == 1:
                break

        # add typed chars
        answer += i
    return answer


if __name__ == '__main__':
    # ans = solution(words=["word", "war", "warrior", "world"]
    ans = solution(words=["go", "gone", "guild"])
