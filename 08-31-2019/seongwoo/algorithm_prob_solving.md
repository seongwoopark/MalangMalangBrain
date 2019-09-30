## 1. MinMaxDivision

I couldn't submit T^T

## 2. NailingPlanks

first try, O((N + M) * N)

    def solution(A, B, C):
        nailed_planks = {}
        for start, end in zip(A, B):
            nailed_planks[(start, end)] = False

        for i, nail in enumerate(C):
            # nail
            for key in nailed_planks.keys():
                start, end = key
                if start <= nail <= end:
                    nailed_planks[key] = True
            # check nailed result
            if all(nailed_planks.values()):
                return i + 1
        return -1

2nd try, O((N + M) * N)

    def can_be_nailed_planks(nails_number, A, B, C):
        nailed_planks = {}
        for start, end in zip(A, B):
            nailed_planks[(start, end)] = False

        for i in range(nails_number):
            # nail
            for key in nailed_planks.keys():
                start, end = key
                if start <= C[i] <= end:
                    nailed_planks[key] = True

            # check nailed result
            if all(nailed_planks.values()):
                return True
        return False

    def solution(A, B, C):
        answer = -1
        min_nails = 1
        max_nails = len(C)
        while min_nails <= max_nails:
            mid_nails = int((min_nails + max_nails) / 2)
            if can_be_nailed_planks(mid_nails, A, B, C):
                answer = mid_nails
                max_nails = mid_nails - 1
            else:
                min_nails = mid_nails + 1
        return answer