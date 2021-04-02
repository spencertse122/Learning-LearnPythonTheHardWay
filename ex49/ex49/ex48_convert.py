def convert_number(s):
    """
    Simple function to convert the input into an integer. If it fails, return None.
    """
    try:
        return int(s)
    except ValueError:
        return None
