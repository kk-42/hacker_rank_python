# Complete the countingValleys function below.
def countingValleys(n, s):
    current_altitude = 0
    no_of_visited_valleys = 0
    in_the_valley = False

    for step in s:
        if step == 'U':
            current_altitude = current_altitude + 1
            if current_altitude >= 0:
                in_the_valley = False

        else:
            current_altitude = current_altitude - 1
            if current_altitude < 0 and not in_the_valley:
                in_the_valley = True
                no_of_visited_valleys = no_of_visited_valleys + 1

    return no_of_visited_valleys


if __name__ == '__main__':
    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)
    print result
