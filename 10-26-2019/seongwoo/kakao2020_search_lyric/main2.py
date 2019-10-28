import re


def match_words(words_chunk, query):
    query = query.replace("?", ".")
    return len(re.findall(fr"\b{query}\b", words_chunk))


def solution(words, queries):
    answer = []
    cache = {}
    words_chunk = '\n'.join(words)
    for query in queries:
        match_count = cache.get(query, None)
        if match_count is None:
            match_count = match_words(words_chunk, query)
            cache[query] = match_count
        answer.append(match_count)
    return answer
