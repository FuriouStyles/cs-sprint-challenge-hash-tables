def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weights_dict = {}
    for key, val in enumerate(weights):
        weights_dict[val] = key
    
    for idx, weight in enumerate(weights):
        if limit - weight in weights_dict:
            if weights_dict[limit-weight] > idx:
                return (weights_dict[limit-weight], idx)
            else:
                return (idx, weights_dict[idx, weights_dict])