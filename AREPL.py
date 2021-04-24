def test_doc_str(number, kwargs=3):
    """This is a test function

    Args:
        number (integer): This is a integer
        kwargs (integer, optional): This is a test. Defaults to 3.

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if number < 2:
        raise TypeError
    return kwargs


data = {"a": 1, "b": [[1, 2], [3, 4]], "c": 5}
