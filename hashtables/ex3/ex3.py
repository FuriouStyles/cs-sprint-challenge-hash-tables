def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # 1. Loop through each list and count the unique 
    # instance of each number found
    #
    # 2. Find the numbers that have a count equal to
    # the number of arrays
    counter = {}
    for lst in arrays:
        for item in lst:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1

    result = []
    for item in counter:
        if counter[item] == len(arrays):
            result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
