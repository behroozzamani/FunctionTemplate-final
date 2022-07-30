def splited(string):
    return string.split()


def count_of_pattern(string_array, pattern):
    count = 0
    for a in string_array:
        if pattern == a:
            count = count + 1

    string_array.append(count)
    return string_array

def remove(string_array, pattern, m):
    count_of_removes = string_array[len(string_array) -1 ]
    string_array.pop()
    if count_of_removes<m:
        return string_array

    count_of_removes = count_of_removes - m
    new_str = ""
    count = 0
    for w in string_array:
        if (w != pattern): # or (count >= count_of_removes):
            new_str = new_str + w + " "
        else:
            if count < m:
                count = count + 1
                new_str = new_str + w + " "

    return new_str


