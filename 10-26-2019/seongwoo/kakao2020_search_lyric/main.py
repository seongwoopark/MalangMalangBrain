import re


def match_words(words, query):
    pattern = re.compile('^' + query.replace("?", ".") + '$')
    match_count = 0
    for word in words:
        if re.match(pattern, word):
            match_count += 1
    return match_count


def solution(words, queries):
    answer = []
    cache = {}
    for query in queries:
        match_count = cache.get(query, None)
        if match_count is None:
            match_count = match_words(words, query)
            cache[query] = match_count
        answer.append(match_count)
    return answer
