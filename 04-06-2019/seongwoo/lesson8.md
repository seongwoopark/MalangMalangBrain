# Lesson 8: Leader

## 1. Dominator

- First try

    [https://app.codility.com/demo/results/trainingANCA7N-QC3/](https://app.codility.com/demo/results/trainingANCA7N-QC3/)

        def solution(A):
            counter = {}
            for i, value in enumerate(A):
                if value in counter:
                    counter[value].append((i, value))
                else:
                    counter[value] = [(i, value)]
            counter = sorted(counter.items(), key=lambda t : len(t[1]), reverse=True)
            answer = counter[0]
            return answer[1][0][0] if len(answer[1]) > len(A) / 2 else -1

- Second try, accepted

    [https://app.codility.com/demo/results/trainingAHRHDN-BAR/](https://app.codility.com/demo/results/trainingAHRHDN-BAR/)

        def solution(A):
            counter = {}
            for i, value in enumerate(A):
                if value in counter:
                    counter[value].append((i, value))
                else:
                    counter[value] = [(i, value)]
            counter = sorted(counter.items(), key=lambda t : len(t[1]), reverse=True)


            if not counter:
                return -1
            answer = counter[0]
            return answer[1][0][0] if len(answer[1]) > len(A) / 2 else -1