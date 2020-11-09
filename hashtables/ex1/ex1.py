def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    lookup = {weight: i for (i, weight) in enumerate(weights)}
    for (i, weight) in enumerate(weights):
        needed_weight = limit - weight
        if needed_weight in lookup:
            return (max(i, lookup[needed_weight]), min(i, lookup[needed_weight]))
            
    return None
