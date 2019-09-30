# Lesson 6: Sorting

## 1. Distinct

- First try, accepted

    [https://app.codility.com/demo/results/trainingTJXMMT-WTM/](https://app.codility.com/demo/results/trainingTJXMMT-WTM/)

        def solution(A):
            return len(set(A))

## 2. MaxProductOfThree

- First try, wrong answer

    [https://app.codility.com/demo/results/trainingBKB2WE-CPY/](https://app.codility.com/demo/results/trainingBKB2WE-CPY/)

        def solution(A):
            A.sort()
            return A[-1] * A[-2] * A[-3]

- Second try, wrong answer

    [https://app.codility.com/demo/results/training7FR77J-7T6/](https://app.codility.com/demo/results/training7FR77J-7T6/)

        def solution(A):
            # sort given array
            A.sort()

            # product of triplet will be positive case #1
            if A[-3] > 0:
                return A[-1] * A[-2] * A[-3]

            # product of triplet will be positive case #2
            if A[1] < 0 and A[-1] > 0:
                return A[0] * A[1] * A[-1]

            # product of triplet will be negative or 0
            A = [item for item in A if item <= 0]
            if A[-1] == 0:
                return 0
            return A[0] * A[1] * A[2]

- Third try, wrong answer

    [https://app.codility.com/demo/results/trainingFRVY9H-X3Y/](https://app.codility.com/demo/results/trainingFRVY9H-X3Y/)

        def solution(A):
            # sort given array
            A.sort()

            # product of triplet will be positive case #1
            if A[-3] > 0:
                return A[-1] * A[-2] * A[-3]

            # product of triplet will be positive case #2
            if A[1] < 0 and A[-1] > 0:
                return A[0] * A[1] * A[-1]

            # product of triplet will be negative or 0
            A = [item for item in A if item <= 0]
            if A[-1] == 0:
                return 0
            return A[-1] * A[-2] * A[-3]

- Fourth try, wrong answer

    [https://app.codility.com/demo/results/training2TFCTN-2AY/](https://app.codility.com/demo/results/training2TFCTN-2AY/)

        def solution(A):
            # sort given array
            A.sort()

            max_cases = []
            # product of triplet will be positive case #1
            if A[-3] > 0:
                max_cases.append(A[-1] * A[-2] * A[-3])

            # product of triplet will be positive case #2
            if A[1] < 0 and A[-1] > 0:
                max_cases.append(A[0] * A[1] * A[-1])

            # product of triplet will be negative or 0
            A = [item for item in A if item <= 0]
            if A[-1] == 0:
                max_cases.append(0)
            return max(max_cases)

- Fifth try, accepted

    [https://app.codility.com/demo/results/training2TFCTN-2AY/](https://app.codility.com/demo/results/training2TFCTN-2AY/)

        def solution(A):
            # sort given array
            A.sort()

            max_cases = []
            # product of triplet will be positive case #1
            if A[-3] > 0:
                max_cases.append(A[-1] * A[-2] * A[-3])

            # product of triplet will be positive case #2
            if A[1] < 0 and A[-1] > 0:
                max_cases.append(A[0] * A[1] * A[-1])

            # product of triplet will be negative or 0
            A = [item for item in A if item <= 0]
            if len(A) >= 1 and A[-1] == 0:
                max_cases.append(0)
            if len(A) >= 3:
                max_cases.append(A[-1] * A[-2] * A[-3])
            return max(max_cases)

## 3. NumberOfDiscIntersections

- First try, brute force O(N^2)

    [https://app.codility.com/demo/results/trainingWPBB94-WGV/](https://app.codility.com/demo/results/trainingWPBB94-WGV/)

        def solution(A):
            A = [(c-r, c+r) for c, r in enumerate(A)]

            count_pairs = 0
            for i, (a1, a2) in enumerate(A):
                for b1, b2 in A[i+1:]:
                    if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
                        count_pairs += 1
            return count_pairs

- Second try, brute force O(N^2) with constraints escape

    [https://app.codility.com/demo/results/trainingGR52EZ-AUM/](https://app.codility.com/demo/results/trainingGR52EZ-AUM/)

        def solution(A):
            A = [(c-r, c+r) for c, r in enumerate(A)]

            count_pairs = 0
            for i, (a1, a2) in enumerate(A):
                for b1, b2 in A[i+1:]:
                    # check if b circle includes a circle
                    if b1 <= a1 <= b2 or b1 <= a2 <= b2:
                        count_pairs += 1
                    # check if a circle includes b circle
                    elif a1 <= b1 <= a2 or a1 <= b2 <= a2:
                        count_pairs += 1
                    if count_pairs > 10000000:
                        return -1
            return count_pairs