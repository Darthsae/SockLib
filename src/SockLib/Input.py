def floatput(prompt: str = "") -> float:
    """Get a float as input

    Args:
        prompt (str): the prompt to display

    Returns:
        float: value of input as float
    """
    return float(input(prompt))

def intput(prompt: str = "") -> int:
    """Get an int as input
    
    Args:
        prompt (str): the prompt to display

    Returns:
        int: value of input as int
    """
    return int(input(prompt))

def boolput(prompt: str = "", case_sensitive: bool = False, true_values: set[str] = {"y", "yes"}) -> bool:
    """Get a bool as input
    
    Args:
        prompt (str): the prompt to display
        case_sensitive (bool): whether to be case sensitive with the input
        true_values (set[str]): the values to consider true

    Returns:
        bool: value of input as bool
    """
    answer: str = input(prompt)
    return answer.lower() if case_sensitive else answer in true_values