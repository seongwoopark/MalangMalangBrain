# Lesson 10: Prime and composite numbers

- Go language를 이용해서 코딩: Go lang 스터디를 병행한다 [http://golang.site/](http://golang.site/)

## 1. CountFactors

[https://app.codility.com/demo/results/trainingF9QS6U-5W9/](https://app.codility.com/demo/results/trainingF9QS6U-5W9/)

    package solution

    func Solution(N int) int {
        var factors int = 0
        for i := 1; i <= N; i++ {
            if i > N / i {
                break
            }

            if N % i == 0 {
                if N / i == i {
                    factors++
                } else {
                    factors += 2
                }
            }
        }
        return factors
    }

## 2. MinPerimeterRectangle

[https://app.codility.com/demo/results/trainingKTQQZX-RG4/](https://app.codility.com/demo/results/trainingKTQQZX-RG4/)

    package solution

    func Solution(N int) int {
        var answer int = (N + 1) * 2
        for a := 1; a <= N; a++ {
            b := N / a
            if a > b {
                break
            }
            if N % a != 0 {
                continue
            }

            if (a + b) * 2 < answer {
                answer = (a + b) * 2
            }
        }
        return answer
    }

## 3. Peaks

First try, O(N^2)

[https://app.codility.com/demo/results/trainingQB8RRH-E8G/](https://app.codility.com/demo/results/trainingQB8RRH-E8G/)

    package solution

    func find_peaks(A []int) []int {
        var peaks []int = []int{}
        for i := 1 ; i < len(A) - 1 ; i++ {
            if (A[i-1] < A[i]) && (A[i] > A[i+1]) {
                peaks = append(peaks, i)
            }
        }
        return peaks
    }

    func can_be_divided(peaks []int, K int, blocks int) bool {
        var start, end int
        var block_has_peak bool
        for i := 0 ; i < blocks; i++ {
            start = i * K
            end = (i + 1) * K
            // println(start, end)
            block_has_peak = false
            for j := 0 ; j < len(peaks); j++ {
                if (start <= peaks[j]) && (peaks[j] < end) {
                    block_has_peak = true
                    break
                }
            }
            if block_has_peak == false {
                return false
            }
        }
        return true
    }

    func Solution(A []int) int {
        // find peaks
        var peaks []int
        peaks = find_peaks(A)

        // divide array
        var i, K int
        for i = len(A) ; i > 0 ; i-- {
            if len(A) % i != 0 {
                continue
            }
            K = len(A) / i
            if can_be_divided(peaks, K, i) {
                return i
            }
        }
        return 0
    }