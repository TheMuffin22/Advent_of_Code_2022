def find_common_item(string):
    for i in range(len(string)):
        if string[i] in string[int(len(string)/2):]:
            return string[i]


def find_group_label(group):
    group.sort(key=len, reverse=True)
    for i in range(len(group[0])):
        if group[0][i] in group[1] and group[0][i] in group[2]:
            return group[0][i]


def evaluate_priority(character):
    if 96 < ord(character) < 123:
        return ord(character) - 96
    elif 64 < ord(character) < 91:
        return ord(character) - 38
    else:
        Exception("Wrong character input")


if __name__ == '__main__':
    data = open("/Users/mavger22/PycharmProjects/Advent_of_Code_2022/03/data.txt")
    sum_prio = 0
    lines = 0
    while True:
        read = data.readline()
        if read == "":
            break
        lines += 1
        read = read[:len(read)-1]
        char = find_common_item(read)
        prio = evaluate_priority(char)
        print(char)
        print(prio)
        sum_prio += prio
    print(f'Your priority sum is {sum_prio} ({lines} bags evaluated)')

    # second half

    data = open("/Users/mavger22/PycharmProjects/Advent_of_Code_2022/03/data.txt")
    sum_prio = 0
    groups = 0
    while True:
        group = []
        for i in range(3):
            group.append(data.readline())

        if group[0] == "":
            break

        label = find_group_label(group)
        prio = evaluate_priority(label)

        sum_prio += prio
        groups += 1

    print(f'Your group label sum is {sum_prio} ({groups} groups evaluated)')


