const menu = [
    {
        "id": 1,
        "name": "红烧肉",
        "owner": "user@example.com.au",
        "type": ["Lunch"],
        "ingredients": [{"name": "五花肉", "measurement": "500", "units": "g"}]
    },
    {
        "id": 2,
        "name": "肉末炖蛋",
        "owner": "user@example.com.au",
        "type": ["Dinner"],
        "ingredients": [{"name": "猪肉糜", "measurement": "500", "units": "g"}]
    },
    {
        "id": 3,
        "name": "富贵虾",
        "owner": "user@example.com.au",
        "type": ["Dinner"],
        "ingredients": [{"name": "大虾", "measurement": "500", "units": "g"}]
    }
]

const plans = [
    {
        "id": "b11b9e65-0e57-4c92-882f-616b584c835a",
        "owner": "username@example.com.au",
        "plan_type": "party",
        "numGuests": 4,
        "planStartDate": "2021-08-02",
        "occasion": "中秋节",
        "createAt": "2021-08-03 16:41:48.847402",
        "updateAt": "2021-08-03 16:41:48.847402",
        "plans": [
            {
                'type': '冷菜',
                'menu': [
                    {
                        "id": 3,
                        "name": "清蒸带鱼",
                        "owner": "user@example.com",
                        "type": ["dinner"],
                        "ingredients": [
                            {"name": "带鱼", "measurement": "500", "units": "g"},
                            {"name": "葱姜", "measurement": "20", "units": "g"},
                        ],
                        "createAt": "2021-08-03 16:41:48.847402",
                        "updateAt": "2021-08-03 16:41:48.847402",
                    }
                ]
            }
        ]
    },
    {
        "id": "b11b9e65-0e57-4c92-882f-616b584c835a",
        "owner": "username@example.com.au",
        "plan_type": "weekly",
        "numGuests": 3,
        "planStartDate": "2021-08-02",
        "planEndDate": "2021-08-08",
        "createAt": "2021-08-03 16:41:48.847402",
        "updateAt": "2021-08-03 16:41:48.847402",
        "plans": [
            {
                "day": "MON",
                "breakfast": [
                    {
                        "id": 1,
                        "name": "牛奶麦片",
                        "owner": "user@example.com",
                        "type": ["breakfast"],
                        "ingredients": [
                            {"name": "牛奶", "measurement": "200", "units": "ml"},
                            {"name": "燕麦片", "measurement": "50g", "units": "g"}
                        ],
                        "createAt": "2021-08-03 16:41:48.847402",
                        "updateAt": "2021-08-03 16:41:48.847402",
                    }
                ],
                "lunch": [
                    {
                        "id": 2,
                        "name": "鸡肉卷",
                        "owner": "user@example.com",
                        "type": ["lunch", "breakfast"],
                        "ingredients": [
                            {"name": "鸡肉", "measurement": "400", "units": "g"},
                            {"name": "生菜", "measurement": "30", "units": "g"},
                            {"name": "青椒", "measurement": "50", "units": "g"},
                            {"name": "卷饼", "measurement": "2", "units": "pieces"},
                        ],
                        "createAt": "2021-08-03 16:41:48.847402",
                        "updateAt": "2021-08-03 16:41:48.847402",
                    }
                ],
                "dinner": [
                    {
                        "id": 3,
                        "name": "清蒸带鱼",
                        "owner": "user@example.com",
                        "type": ["dinner"],
                        "ingredients": [
                            {"name": "带鱼", "measurement": "500", "units": "g"},
                            {"name": "葱姜", "measurement": "20", "units": "g"},
                        ],
                        "createAt": "2021-08-03 16:41:48.847402",
                        "updateAt": "2021-08-03 16:41:48.847402",
                    }
                ]
            }
        ]
    }
]

const user = {
    "id": "1",
    "username": "user@exampl.com",
    "password": "randomtexthere",
    "createAt": "2021-08-03",
    "createAt": "2021-08-11",
}

