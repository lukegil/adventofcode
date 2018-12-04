import requests

class ForeverIter(object):
    def __init__(self, els):
        self.els = els
        self.index = -1
        self.length = len(els)

    def __iter__(self):
        return self

    def next(self):
        self.index += 1
        if self.index < self.length:
            return self.els[self.index]
        self.index = -1
        return self.next()

class ForeverList(list):
    def __init__(self, *args):
        super(ForeverList, self).__init__(*args)

    def __iter__(self):
        return ForeverIter(self)


def file_to_array(f):
    resp = open(f, 'r')
    return [line.strip() for line in resp]

def process(arr):
    seen = set([])
    cur_val = 0
    found_dupe = False
    for num in ForeverList(arr):
        cur_val += int(num)
        if cur_val in seen:
            break
        seen.add(cur_val)
    return cur_val

if __name__ == '__main__':
    arr = file_to_array('./data.txt')
    print process(arr)
