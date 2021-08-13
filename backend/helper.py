from typing import List
import random
import json

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
    drop_cols = ['序号']
    reduce_key = ['菜名']
    owner = "user@example.com.au"
    df = (pd.read_excel(file)
          .drop(drop_cols, axis=1)
          .dropna(how="all")
          .ffill()
          )

    df['ingredients'] = df.apply(lambda x:{'name':x['配料'],'measurement':x['用量'],'unit':x['单位']}, axis=1)
    reduce = df.groupby(reduce_key)['ingredients'].apply(list)

    data = json.loads(reduce.to_frame().reset_index().assign(owner=owner).to_json(orient="records"))
    return data


if __name__ == '__main__':
    from pprint import pprint
    pprint(transform('../../炒菜谱.xlsx'))