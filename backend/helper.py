from typing import List
import random

import pandas as pd

def shuffle(type: str) -> List[dict]:
    """
    :param type: lunch, breakfast, dinner
    :return: list
    """
    options = [
            {"id":1, "name":"红烧肉", "owner":"user@example.com.au","type":["Lunch"],"ingredients":[{"name":"五花肉","measurement":"500","units":"g"}]},
            {"id":2, "name":"肉末炖蛋", "owner":"user@example.com.au","type":["Dinner"],"ingredients":[{"name":"猪肉糜","measurement":"500","units":"g"}]},
            {"id":3, "name":"富贵虾", "owner":"user@example.com.au","type":["Dinner"],"ingredients":[{"name":"大虾","measurement":"500","units":"g"}]},
        ]
    choices = random.choices(options, k=2)
    return choices

def transform(file:str) -> List[dict]:
    df = pd.read_excel(file)



if __name__ == '__main__':
    choices = shuffle("lunch")
    print(choices)