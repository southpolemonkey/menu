# Menu Saver

## 功能

- 自动生产每周菜单和购物清单
- 支持根据人数自动生成家庭聚餐的菜单和购物清单
- 支持手动导入菜单
- 支持历史数据查看
- 支持菜单和购物清单的导出
- 支持搜索：配料，种类(点心，荤素菜，汤类等) 
- 支持查看单一菜品以及更新数据
- (Optional) 根据菜单生成预算
- (Optional) 购物清单按类别排列，提供购物路线
- (Optional) 支持菜式风格，比如西式，中式，荤菜还是素菜等
- (Optional) 宴会菜单根据更新宾客数自己调整


## System Design

### Technology

- Backend: FastAPI
- Frontend: React
- Storage: MongoDB



### Sample data

```json
# meals
[
    {
      'name': 'fried eggs'
      'owner': <username>
      'type': ['breakfast', 'lunch']
      'ingredients': [
        {'name': 'egg', 'mesaure': '2', 'units': ''},
        {'name': 'spring onion', 'measure': '50', 'units': 'g'
      ],
    },
    {
      'name': '土豆牛腩煲'
      'owner': <username>
      'type': ['dinner']
      'ingredients': [
        {'name': 'potato', 'mesaure': '200', 'units': 'g'},
        {'name': 'beef flank', 'measure': '500', 'units': 'g'
      ],
      'duration': '120 mins'
    }

]

# weekly plan
{
  'date': '2021-07-25'
  'owner': <user_id>
  'type': 'weekly'
  'plans': [
    {'day': 'monday', 
     'breakfast': ['milk', 'sandwich', 'boilded eggs'],
     'lunch': ['steak sandwich'],
     'dinner': ['chicken', 'fried vegetables']
    },
    {'day': 'tuesday', 
     'breakfast': ['orange juice', 'bread'],
     'lunch': ['beef soup noodle'],
     'dinner': ['fish', 'salad']
    },
    ...
  ]
}


# party plan
{
 'date': '2021-07-05',
 'title': 'birthday party'
 'type': 'party',
 'number_guests': '8',
 'plans': ['steak', 'fish', 'lamb', 'salad']
}



# shopping list
{
  'date': '2021-07-25'
  ingredients: [
    {'name': 'egg', 'measurements': '1 box'},
    {'name': 'pork belly', 'measurements': '1 kg'},
    {'name': 'iceberg', 'measurements': '2 heads'},
    {'name': 'salmon fillets', 'measurements': '3 pieces'},
    {'name': 'tiger prawn', 'measurements': '500 gram'},
  ]
}

```

### Project Structure

```
backend
    - main.py
    - routers
        - menu.py
        - users.py
        - plan.py
    - models
        - menu.py
        - users.py
        - plan.py
    - internals
        - admin.py
```

### Class

```
/MenuGenerator
 - weekly_menu(num_guest, ) 
 - party_menu(num_guest, )
/IngredientAggregator 
/IO
 - Input meals data
 - Export   
```

```python
def pick(type: str):
    '''pick a random meal from database for the given type'''
    meal = "select * from db.meals where type = lunch order by random()" 
```
 
### API endpoints

**Menu**

```
/menu                   GET     Retrieve all menus
/menu                   POST    Create a new menu
/menu/{menuId}          PUT     Update a menu
/menu/{menuId}          DELETE     Delete a menu
/menu/createWithList    POST    Create menus in batch
```

**Plan**

```
/plan           GET     Retrieve all plans
/plan/          POST    Generate a plan
/plan/{planId}  GET     Find generated plan by ID
/plan/{planId}  DELETE  Delete generated plan by ID

```

**User**

```
/user           POST    Create an User
/user/login     GET     Login in user
/user/logout    GET     Logout user
/user/{username} GET
/user/{username} PUT
/user/{username} DELETE 
```

### Data Model

```
Menu {
    id          integer
    name        string
    owner       string
    followers   Array[User]
    type        string Enum
    ingredients Array[{
        id          integer
        name        string
        measurement integer
        units       string
    }]
    createAt     string($date-time)
    updateAt         string($date-time)
}
```

```
WeeklyMenu {
    id      integer
    owner   integer
    num_guests      integer
    planStartDate   string($date)
    planEndDate     string($date)
    createAt        string($datetime)
    updateAt        string($datetime)
    plans           Array[
        {
            day ENUM Array [MON,TUE,WED,THU,FRI,SAT,SUN ]
            breakfast Array [Menu]
            lunch     Array [Menu] 
            dinner    Array [Menu]   
        }
    ]
}
```

```
GroupMenu {
    id      integer
    owner   integer
    num_guests      integer
    plans Array[ Menu ]
    planStartDate   string($date)
    purpose     string
    createAt    string($datetime)
    updateAt    string($datetime)
}

```

```
ShoppingList {
    id integer
    plan_id     integer
    ingredients Array[
      {
        name        string
        measurement integer
        units       string
      }
    ]
    planDate    string($date)
    createAt    string($datetime)
    updateAt    string($datetime)
}
```

## Useful tools

https://transform.tools/json-to-proptypes