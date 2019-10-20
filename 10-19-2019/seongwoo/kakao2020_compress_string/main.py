def solution(s):
    answer = len(s)
    for unit_size in range(1, int(len(s) / 2) + 1):
        compressed = ''
        chunk = s[0:unit_size]
        repeat_count = 1
        for start in range(unit_size, len(s), unit_size):
            if chunk == s[start:start+unit_size]:
                repeat_count += 1
            else:
                if repeat_count == 1:
                    compressed = f'{compressed}{chunk}'
                else:
                    compressed = f'{compressed}{repeat_count}{chunk}'
                chunk = s[start:start+unit_size]
                repeat_count = 1
        else:
            if repeat_count == 1:
                compressed = f'{compressed}{chunk}'
            else:
                compressed = f'{compressed}{repeat_count}{chunk}'

        # compare compressed size
        if len(compressed) < answer:
            answer = len(compressed)
    return answer
