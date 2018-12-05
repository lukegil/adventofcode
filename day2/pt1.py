

def file_to_list(filepath):
    f = open(filepath, 'r')
    return [line.strip() for line in f]

def find_dupes(box_id):
    letters = {}
    for letter in box_id:
        if letters.get(letter):
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    found_two = False
    found_three = False
    for letter in letters:
        if letters[letter] == 2:
            found_two = True
        elif letters[letter] == 3:
            found_three = True
    return (found_two, found_three)

def calc_checksum(box_ids):
    twos = 0
    threes = 0
    for box_id in box_ids:
        a, b = find_dupes(box_id)
        twos += a
        threes += b
    return twos * threes


if __name__ == '__main__':
    arr = file_to_list('./data.txt')
    print calc_checksum(arr)
