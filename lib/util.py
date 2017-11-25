import operator

def key_with_max_value(item):
    """Get the key with maximum value in a dict."""
    return max(item.iteritems(), key=operator.itemgetter(1))[0]




