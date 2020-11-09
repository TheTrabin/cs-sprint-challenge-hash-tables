def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    negatives = {num: True for num in a if num < 0}
    return [num for num in a if num > 0 and -num in negatives]
    # return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
