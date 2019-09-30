import os


def solution(pattern, string):
    if '*' not in pattern:
        if '?' not in pattern:
            # exact match
            return pattern == string
        else:
            # only ? exists
            if len(pattern) != len(string):
                return False
            while
            pattern.index('?')
            pass
    else:
        ans = False
    return ans


class ReadContext(object):
    def __init__(self, file_name=None):
        if not file_name:
            file_name = 'input.txt'
        dir_name = os.path.dirname(os.path.abspath(__file__))
        if os.path.exists('{0}/{1}'.format(dir_name, file_name)):
            self._file_obj = open('{0}/{1}'.format(dir_name, file_name), 'r')
        else:
            self._file_obj = None

    def __enter__(self):
        return self

    def input(self):
        return self._file_obj.readline() if self._file_obj else input()

    def __exit__(self, _type, _value, _trace_back):
        if self._file_obj:
            self._file_obj.close()


if __name__ == '__main__':
    with ReadContext() as r:
        C = int(r.input().strip())
        for _ in range(C):
            W = r.input().strip()
            N = int(r.input().strip())
            answers = []
            for _ in range(N):
                file_name = r.input().strip()
                result = solution(pattern=W, string=file_name)
                if result is True:
                    answers.append(file_name)
            for answer in sorted(answers):
                print(answer)
