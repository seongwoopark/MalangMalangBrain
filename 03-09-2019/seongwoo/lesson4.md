# Lesson 4: Counting Elements

1. MaxCounters → 왜 되는건지? is_changed_max_counter_value를 False로 하는 부분이 없는데?

    result report: [https://app.codility.com/demo/results/trainingRSWS9K-GFB/](https://app.codility.com/demo/results/trainingRSWS9K-GFB/)

    ```python
    def solution(N, A):
        answer = [0] * N
        max_counter_value = 0
        is_changed_max_counter_value = False

        for operation in A:
            if operation == N + 1:
                if is_changed_max_counter_value:
                    answer = [max_counter_value] * N
            else:
                answer[operation - 1] += 1
                if answer[operation - 1] > max_counter_value:
                    max_counter_value = answer[operation - 1]
                    is_changed_max_counter_value = True
        return answer
    ```

2. MissingInteger → 다 못품 숙제로 풀어오기
    ```python
    def solution(A):
        A = sorted(set(A))
        A.insert(0, -10000000)
        A.append(10000000)
        for v in A:
            if v:
                return
        return A[-1] + 1
    ```

    완료 답안,
    ```python
    def solution(A):
        A = sorted(set(A))
        A.insert(0, -1000001)
        A.append(1000001)
        for i in range(1, len(A)-1):
            if A[i-1] <= 0 and A[i] <= 0:
                continue

            asd = range(A[i-1] + 1, A[i])
            if asd:
                for j in asd:
                    if j > 0:
                        return j

        ans = 1000001
        asd = range(A[-2] + 1, A[-1])
        for j in asd:
            if j > 0:
                ans = j
                break
        return ans
    ```

3. PDF 파일 보고, Counter패턴(빵꾸 뚫어 놓는 패턴)으로도 풀어보고, 이 패턴 익히기

4. 다 하고, 오늘 부분 개인블로그에 올리기