from typing import Collection, runtime_checkable
from Typing import SupportsAverage

def avg(collection: Collection[SupportsAverage]) -> SupportsAverage:
    """Get the average of a collection of addable values.

    Args:
        collection (Collection[SupportsAverage]): The collection to get the average of.

    Returns:
        SupportsAverage: The average of the collection.
    """
    
    return sum(collection) / len(collection)
