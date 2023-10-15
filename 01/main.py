# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = open("/Users/mavger22/PycharmProjects/Advent_of_Code_2022/01/data.txt")
    calories = []
    carried = 0
    while True:
        read = data.readline()
        if read == "\n":
            calories.append(carried)
            carried = 0
            continue

        elif read == "":
            break

        else:
            read = int(read)
            carried += read

    calories.sort(reverse=True)
    print(calories)

    print(f'Elve #{calories.index(max(calories)) + 1} carries the most ({max(calories)}) calories')

# part two
    topThree = 0
    for i in range(3):
        topThree += max(calories)
        print(max(calories))
        calories.remove(max(calories))


    print(f'The top three elves carry {topThree} calories')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
