import string
exclude = set(string.punctuation)

def handle_strings(x):
    """
    Helper function to make string all caps and remove punctuation.
    
    x: any string
    """
    x = x.upper()
    x = ''.join(ch for ch in x if ch not in exclude)
    return x
    