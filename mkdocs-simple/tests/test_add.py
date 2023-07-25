from mkdocs_simple.add import add, add_np

def test_add():
    assert add(1,2) == 3

def test_add_np():
    assert add_np(1,2) == 3

def test_adds():
    assert add(1,2) == add_np(1,2)