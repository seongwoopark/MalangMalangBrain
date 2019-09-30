# Lesson 12: Euclidean algorithm

reading material: [https://codility.com/media/train/10-Gcd.pdf](https://codility.com/media/train/10-Gcd.pdf)

## 1. ChocolatesByNumbers

first try, brute force, O(N + M)

[https://app.codility.com/demo/results/training2QUYJV-6KG/](https://app.codility.com/demo/results/training2QUYJV-6KG/)

    def solution(N, M):
        answer = 0
        chocloates = [True] * N
        cursor = 0
        while chocloates[cursor]:
            # eat chocolate
            answer += 1
            chocloates[cursor] = False
            # update cursor
            cursor = (cursor + M) % N
        return answer

2nd try, improve special cases, O(N + M)

[https://app.codility.com/demo/results/trainingS75A5W-G3B/](https://app.codility.com/demo/results/trainingS75A5W-G3B/)

    def solution(N, M):
        # handle special case
        if M == N:
            return 1
        elif M > N:
            M = M - N

        answer = 0
        chocloates = [True] * N
        cursor = 0
        while chocloates[cursor]:
            # eat chocolate
            answer += 1
            chocloates[cursor] = False
            # update cursor
            cursor = (cursor + M) % N
        return answer

3rd try, use gcd and lcm, O(log(N + M))

[https://app.codility.com/demo/results/trainingKW8W34-H45/](https://app.codility.com/demo/results/trainingKW8W34-H45/)

    def gcd_dividing(a, b):
        if a % b == 0:
            return b
        else:
            return gcd_dividing(b, a % b)

    def lcm(a,b):
        gcd = gcd_dividing(a, b)
        return (a * b) / gcd

    def solution(N, M):
        # handle special case
        if M == N:
            return 1
        elif M > N:
            M = M - N
        return int(lcm(N, M) / M)

## 2. CommonPrimeDivisors

first try, wrong

[https://app.codility.com/demo/results/training67F889-93M/](https://app.codility.com/demo/results/training67F889-93M/)

    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        i=2
        while (i * i <= n):
            if (sieve[i]):
                k=i * i
                while (k <= n):
                    sieve[k] = False
                    k += i
            i += 1
        return sieve

    def gcd_binary(a, b, res):
        if a == b:
            return res * a
        elif (a % 2 == 0) and (b % 2 == 0):
            return gcd_binary(a // 2, b // 2, 2 * res)
        elif (a % 2 == 0):
            return gcd_binary(a // 2, b, res)
        elif (b % 2 == 0):
            return gcd_binary(a, b // 2, res)
        elif a > b:
            return gcd_binary(a - b, b, res)
        else:
            return gcd_binary(a, b - a, res)

    def get_prime_divisors(n, _sieve):
        prime_divisors = set()
        for i in range(2, n):
            quotient = n / i
            if quotient < i:
                break
            quotient = int(quotient)
            if n % i == 0:
                if _sieve[i]:
                    prime_divisors.add(i)
                if _sieve[quotient]:
                    prime_divisors.add(quotient)
        return prime_divisors

    def solution(A, B):
        answer = 0
        max_element = max([max(A), max(B)])
        _sieve = sieve(max_element)
        for a, b in zip(A, B):
            # special case
            if a == b:
                answer += 1
                continue

            # get common prime divisiors
            gcd = int(gcd_binary(a, b, 1))
            common_prime_divisors = get_prime_divisors(gcd, _sieve)

            # check
            a_quotient = int(a / gcd)
            b_quotient = int(b / gcd)
            if a_quotient in common_prime_divisors and b_quotient not in common_prime_divisors:
                answer += 1
            elif a_quotient not in common_prime_divisors and b_quotient in common_prime_divisors:
                answer += 1
        return answer

2nd try, wrong

[https://app.codility.com/demo/results/trainingA352S8-VH5/](https://app.codility.com/demo/results/trainingA352S8-VH5/)

    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        i=2
        while (i * i <= n):
            if (sieve[i]):
                k=i * i
                while (k <= n):
                    sieve[k] = False
                    k += i
            i += 1
        return sieve

    def gcd_binary(a, b, res):
        if a == b:
            return res * a
        elif (a % 2 == 0) and (b % 2 == 0):
            return gcd_binary(a // 2, b // 2, 2 * res)
        elif (a % 2 == 0):
            return gcd_binary(a // 2, b, res)
        elif (b % 2 == 0):
            return gcd_binary(a, b // 2, res)
        elif a > b:
            return gcd_binary(a - b, b, res)
        else:
            return gcd_binary(a, b - a, res)

    def get_prime_divisors(n, _sieve):
        prime_divisors = set()
        for i in range(2, n):
            quotient = n / i
            if quotient < i:
                break
            quotient = int(quotient)
            if n % i == 0:
                if _sieve[i]:
                    prime_divisors.add(i)
                if _sieve[quotient]:
                    prime_divisors.add(quotient)
        return prime_divisors

    def solution(A, B):
        # get gcd list
        gcd_list = []
        for a, b in zip(A, B):
            gcd_list.append(int(gcd_binary(a, b, 1)))

        # get _sieve from max gcd
        _sieve = sieve(max(gcd_list))

        # get answer
        answer = 0
        for a, b, gcd in zip(A, B, gcd_list):
            # special case
            if a == b:
                answer += 1
                continue

            # get common prime divisiors
            common_prime_divisors = get_prime_divisors(gcd, _sieve)

            # check
            a_quotient = int(a / gcd)
            b_quotient = int(b / gcd)
            if a_quotient in common_prime_divisors and b_quotient not in common_prime_divisors:
                answer += 1
            elif a_quotient not in common_prime_divisors and b_quotient in common_prime_divisors:
                answer += 1
        return answer

3rd try, wrong

[https://app.codility.com/demo/results/trainingYKFF76-NFY/](https://app.codility.com/demo/results/trainingYKFF76-NFY/)

    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        i=2
        while (i * i <= n):
            if (sieve[i]):
                k=i * i
                while (k <= n):
                    sieve[k] = False
                    k += i
            i += 1
        return sieve

    def gcd_binary(a, b, res):
        if a == b:
            return res * a
        elif (a % 2 == 0) and (b % 2 == 0):
            return gcd_binary(a // 2, b // 2, 2 * res)
        elif (a % 2 == 0):
            return gcd_binary(a // 2, b, res)
        elif (b % 2 == 0):
            return gcd_binary(a, b // 2, res)
        elif a > b:
            return gcd_binary(a - b, b, res)
        else:
            return gcd_binary(a, b - a, res)

    def get_prime_divisors(n, _sieve):
        prime_divisors = set()
        for i in range(2, n):
            quotient = n / i
            if quotient < i:
                break
            quotient = int(quotient)
            if n % i == 0:
                if _sieve[i]:
                    prime_divisors.add(i)
                if _sieve[quotient]:
                    prime_divisors.add(quotient)
        prime_divisors.discard(1)
        return prime_divisors

    def solution(A, B):
        # get gcd list
        gcd_list = []
        for a, b in zip(A, B):
            gcd_list.append(int(gcd_binary(a, b, 1)))
        # get _sieve from max gcd
        _sieve = sieve(max(gcd_list))

        # get answer
        answer = 0
        for a, b, gcd in zip(A, B, gcd_list):
            # special case
            if a == b:
                answer += 1
                continue

            # get common prime divisiors
            common_prime_divisors = get_prime_divisors(gcd, _sieve)

            # check
            a_quotient = int(a / gcd)
            b_quotient = int(b / gcd)
            if a_quotient in common_prime_divisors and b_quotient not in common_prime_divisors:
                answer += 1
            elif a_quotient not in common_prime_divisors and b_quotient in common_prime_divisors:
                answer += 1
            elif a_quotient == b:
                answer += 1
            elif b_quotient == a:
                answer += 1
        return answer

4th try, wrong

[https://app.codility.com/demo/results/trainingHDW6NT-F6R/](https://app.codility.com/demo/results/trainingHDW6NT-F6R/)

    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        i=2
        while (i * i <= n):
            if (sieve[i]):
                k=i * i
                while (k <= n):
                    sieve[k] = False
                    k += i
            i += 1
        return sieve

    def gcd_binary(a, b, res):
        if a == b:
            return res * a
        elif (a % 2 == 0) and (b % 2 == 0):
            return gcd_binary(a // 2, b // 2, 2 * res)
        elif (a % 2 == 0):
            return gcd_binary(a // 2, b, res)
        elif (b % 2 == 0):
            return gcd_binary(a, b // 2, res)
        elif a > b:
            return gcd_binary(a - b, b, res)
        else:
            return gcd_binary(a, b - a, res)

    def get_prime_divisors(n, _sieve):
        prime_divisors = set()
        for i in range(1, n+1):
            quotient = n / i
            if quotient < i:
                break
            quotient = int(quotient)
            if n % i == 0:
                if _sieve[i]:
                    prime_divisors.add(i)
                if _sieve[quotient]:
                    prime_divisors.add(quotient)
        prime_divisors.discard(1)
        return prime_divisors

    def solution(A, B):
        # get gcd list
        gcd_list = []
        for a, b in zip(A, B):
            gcd_list.append(int(gcd_binary(a, b, 1)))
        # get _sieve from max gcd
        _sieve = sieve(max(gcd_list))

        # get answer
        answer = 0
        for a, b, gcd in zip(A, B, gcd_list):
            # special case
            if a == b:
                answer += 1
                continue

            # get common prime divisiors
            common_prime_divisors = get_prime_divisors(gcd, _sieve)

            # check
            a_set = get_prime_divisors(int(a / gcd), _sieve)
            b_set = get_prime_divisors(int(b / gcd), _sieve)
            if a_set | common_prime_divisors == b_set | common_prime_divisors:
                answer += 1
        return answer