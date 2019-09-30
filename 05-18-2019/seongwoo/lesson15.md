# Lesson 15: Caterpillar method

## 1. CountTriangles

[https://app.codility.com/demo/results/trainingQ6KACS-59S/](https://app.codility.com/demo/results/trainingQ6KACS-59S/)

First try, wrong answer

    from operator import itemgetter

    def solution(A):
        # index and sort array A
        indexed_A = []
        for i, side in enumerate(A):
            indexed_A.append((i, side))
        sorted_indexed_A = sorted(indexed_A, key=itemgetter(1))

        # get number of triplet cases
        largest_side_item = sorted_indexed_A[-1]
        second_largest_side_item = sorted_indexed_A[-2]
        for i, side in sorted_indexed_A:
            if second_largest_side_item[0] == i:
                return 0
            if second_largest_side_item[1] + side > largest_side_item[1]:
                break
        len_can_be_triplet_items = len(sorted_indexed_A[i:])
        # return nC3 = len(can_be_triplet_items)! / (3! * (len(can_be_triplet_items) - 3)!)
        return int(len_can_be_triplet_items * (len_can_be_triplet_items - 1) * (len_can_be_triplet_items - 2) / (3 * 2 * 1))