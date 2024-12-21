import os

def parse_and_sort_input() -> tuple:
    list1 = []
    list2 = []
    with open('input.txt', 'r') as f:
        for line in f:
            line_splits = line.strip().split('   ')
            list1.append(int(line_splits[0]))
            list2.append(int(line_splits[1]))

    return list1, list2

def calculate_distance(list1, list2) -> int: # Part 1
    list1.sort()
    list2.sort()

    distance = 0
    for key, _ in enumerate(list1):
        distance += abs(list1[key] - list2[key])

    return distance

def calculate_similarity_score(list1, list2) -> int: # Part 2
    similarity_score = 0

    for id in list1:
        similarity_score += id * list2.count(id)

    return similarity_score

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))

    list1, list2 = parse_and_sort_input()
    
    print(f'Total distance: {calculate_distance(list1, list2)}')

    print(f'Similarity score: {calculate_similarity_score(list1, list2)}')

    print('end')
