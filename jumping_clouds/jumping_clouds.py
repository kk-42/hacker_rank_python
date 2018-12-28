
def calculate_finish_position(c):
    for i in range(len(c) - 1, 0, -1):
        if c[i] == 0:
            return i


def jump(current_position, current_jump_number, no_of_steps):
    current_position = current_position + no_of_steps
    current_jump_number = current_jump_number + 1

    return current_position, current_jump_number

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    no_of_jumps = 0
    current_position = 0
    finish_position = calculate_finish_position(c)

    while current_position < finish_position:
        if current_position + 2 < len(c) and c[current_position + 2] == 0:
            current_position, no_of_jumps = jump(current_position, no_of_jumps, 2)

        else:
            current_position, no_of_jumps = jump(current_position, no_of_jumps, 1)

    return no_of_jumps


if __name__ == '__main__':

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)
    print result
