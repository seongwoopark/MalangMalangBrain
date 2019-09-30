# Lesson 13: Fibonacci numbers

reading material: [https://codility.com/media/train/11-Fibonacci.pdf](https://codility.com/media/train/11-Fibonacci.pdf)

## 1. Ladder

first try, backtracking alogorithm, O(L**2), runtime error: maximum recursion depth

[https://app.codility.com/demo/results/training9MG4C7-5BW/](https://app.codility.com/demo/results/training9MG4C7-5BW/)

    cache = {}

    def climbing_ways(rungs):
        # cache hit
        ways = cache.get(rungs)
        if ways:
            return ways
        # escapce conditions
        elif rungs < 0:
            ways = 0
        elif rungs == 0:
            ways = 1
        else:
            # like fibonacci
            ways = climbing_ways(rungs-2) + climbing_ways(rungs-1)
        # cache set
        cache[rungs] = ways
        return ways


    def solution(A, B):
        answers = []
        for rungs, m in zip(A, B):
            answers.append(climbing_ways(rungs) % 2**m)
        return answers

2nd try, O(L**2), add setrecursionlimit, timeout error

[https://app.codility.com/demo/results/trainingEC3HAW-ZZT/](https://app.codility.com/demo/results/trainingEC3HAW-ZZT/)

    import sys
    sys.setrecursionlimit(100000)


    cache = {}

    def climbing_ways(rungs):
        # cache hit
        ways = cache.get(rungs)
        if ways:
            return ways
        # escapce conditions
        elif rungs < 0:
            ways = 0
        elif rungs == 0:
            ways = 1
        else:
            # like fibonacci
            ways = climbing_ways(rungs-2) + climbing_ways(rungs-1)
        # cache set
        cache[rungs] = ways
        return ways


    def solution(A, B):
        answers = []
        for rungs, m in zip(A, B):
            answers.append(climbing_ways(rungs) % 2**m)
        return answers

3rd try, O(L), applied 2nd cache

[https://app.codility.com/demo/results/training67ZNNF-H3G/](https://app.codility.com/demo/results/training67ZNNF-H3G/)

    import sys
    sys.setrecursionlimit(100000)


    climbing_cache = {}

    def climbing_ways(rungs):
        # cache hit
        ways = climbing_cache.get(rungs)
        if ways:
            return ways
        # escapce conditions
        elif rungs < 0:
            ways = 0
        elif rungs == 0:
            ways = 1
        else:
            # like fibonacci
            ways = climbing_ways(rungs-2) + climbing_ways(rungs-1)
        # cache set
        climbing_cache[rungs] = ways
        return ways


    def solution(A, B):
        answers = []
        answer_cache = {}
        for rungs, m in zip(A, B):
            answer = answer_cache.get((rungs, m))
            if not answer:
                answer = climbing_ways(rungs) % 2**m
                answer_cache[(rungs, m)] = answer
            answers.append(answer)
        return answers

## 2. FibFrog

first try, wrong answer

[https://app.codility.com/demo/results/training5C27T3-MD2/](https://app.codility.com/demo/results/training5C27T3-MD2/)

    def fib(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)


    min_jumps = 100002


    def jumping(cursor, jumps, leaves, jump_types):
        # escapce conditions
        global min_jumps
        if cursor == -1:
            if jumps < min_jumps:
                min_jumps = jumps
            return

        for jump_type in jump_types:
            next_cursor = cursor - jump_type
            if next_cursor < -1:
                break
            if next_cursor == -1 or leaves[next_cursor] == 1:
                jumping(cursor=next_cursor, jumps=jumps + 1, leaves=leaves, jump_types=jump_types)
        return


    def solution(A):
        # get jump types
        goal = len(A)
        n = 0
        result = 0
        jump_types = set()
        while result < goal:
            result = fib(n)
            if result <= goal:
                jump_types.add(result)
            n += 1
        jump_types.discard(0)
        jump_types = sorted(list(jump_types))

        # get min jumps
        jumping(cursor=goal, jumps=0, leaves=A, jump_types=jump_types)
        global min_jumps
        return -1 if min_jumps == 100002 else min_jumps