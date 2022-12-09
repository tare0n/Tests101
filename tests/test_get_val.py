from get_val import get_val


def test_get_val():
    assert get_val({"key": "value"}, "key") == "value"


def test_get_val_for_empty_dict():
    assert get_val({}, "key") == "world"


def test_get_val_for_new_default():
    assert get_val("not dict", "key", "default") == "default"
