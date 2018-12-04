import requests

def file_to_array(f):
    resp = open(f, 'r')
    return [line.strip() for line in resp]

def process(arr):
    return sum([int(k) for k in arr])

if __name__ == '__main__':
    arr = file_to_array('./data.txt')
    print process(arr)
