#!/usr/bin/env python3
import sys

def get_input(filepath):
    counter = 0
    file = open(filepath, 'r')
    content = file.readlines()
    new = []
    for lines in content:
        new.append(lines.split(" "))
        new[counter] = lines.rstrip()
        counter += 1
    firstline = []
    streets = []
    cars = []

    firstline.append(new[0].split(" "))

    stop = 0
    counter_for_cars = 0
    for x in new:
        if stop == 0:
            stop +=1
            continue
        tmp = x[::-1][0]
        if tmp.isnumeric() == True:
            streets.append(x.split(" "))
            counter_for_cars += 1
    stop = 0
    for x in new:
        if stop <= counter_for_cars:
            stop +=1
            continue
        cars.append(x.split(" "))

    file.close()
    return firstline, streets, cars


def check_if_exist(ind, schedule):
    for i in range(len(schedule)):
        if (ind == schedule[i][0]):
            return (True, i)
    return (False, 0)

def loop(coll):
    schedule = []

    for i in range(int(coll[0][0][2])):
        if (len(schedule) == 0):
            schedule.append([coll[1][i][y + 1] for y in range(3)])
        else:
            check = check_if_exist(coll[1][i][1], schedule)
            if (check[0] == True):
                for x in range(2):
                    schedule[check[1]].append(coll[1][i][x + 2])
            else:
                schedule.append([coll[1][i][y + 1] for y in range(3)])
    
    print(len(schedule))
    for i in range(len(schedule)):
        lol = 1
        print(int(schedule[i][0]))
        print(int((len(schedule[i]) - 1) / 2))
        for x in range(int((len(schedule[i]) - 1) / 2)):
            print(str(schedule[i][lol]) + " " + str(schedule[i][lol + 1]))
            lol += 2

def main(argv):
    coll = get_input(argv[1])
    loop(coll)





if __name__ == '__main__':
    main(sys.argv)
