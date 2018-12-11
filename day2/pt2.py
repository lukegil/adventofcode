

def file_to_list(filepath):
    f = open(filepath, 'r')
    return [line.strip() for line in f]

def get_variations(box_id):
    variations = set([])
    for i in range(len(box_id)):
        variations.add(box_id[:i] + '?' + box_id[i+1:])
    
    return variations

def process(arr):
    seen_ids = set([])
    for box_id in arr:
        variations = get_variations(box_id)
        for var in variations:
            if var in seen_ids:
                return var
        seen_ids |= variations
    return ''


if __name__ == '__main__':
    arr = file_to_list('./data.txt')
    print process(arr).replace('?', '')
