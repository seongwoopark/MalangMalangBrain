max_len = 100000


def solution(words, queries):
    # create trie and reverse trie by length
    trie_by_length = [{} for _ in range(max_len + 1)]
    rtrie_by_length = [{} for _ in range(max_len + 1)]
    for word in words:
        # len of words
        word_len = len(word)

        # get trie by length
        # it is root trie, root trie counts the length of word
        trie = trie_by_length[word_len]
        rtrie = rtrie_by_length[word_len]

        # insert word into trie
        for char, rchar in zip(word, word[::-1]):
            # set count
            trie['count'] = trie.get('count', 0) + 1
            rtrie['count'] = rtrie.get('count', 0) + 1

            # set trie by char
            # it is trie that the words that begin with char
            if char not in trie:
                trie[char] = {}
            if rchar not in rtrie:
                rtrie[rchar] = {}

            # prepare next step
            trie = trie[char]
            # prepare next step
            rtrie = rtrie[rchar]

    # search
    answer = []
    for query in queries:
        # decide query
        if query[0] == '?':
            query = query[::-1]
        else:
            pass
    return answer
