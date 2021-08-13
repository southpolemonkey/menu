from backend.helper import transform

def test_transform():
    test_file = '../../炒菜谱.xlsx'
    data = transform(test_file)
    assert isinstance(data, list) == True


