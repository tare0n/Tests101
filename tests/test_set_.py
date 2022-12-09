from set_ import set_
from flatten import flatten
import random as rd


test_coll = {"a": {"b": {"c": 11}}}
letters = list('abcdefghijklmnopqrstuvwxyz')
test_path = []
for i in range(rd.randint(1, 5)):
    test_path.append(rd.choice(letters))
test_value = rd.randint(1, 10)


def test_set_update():
    set_(test_coll, test_path, test_value)
    assert test_value in flatten(test_coll).values()


test_path = []
for i in range(rd.randint(1, 5)):
    test_path.append(rd.choice(letters))
test_value = rd.randint(1, 10)


def test_set_len():
    start_len = len(flatten(test_coll))
    set_(test_coll, test_path, test_value)
    difference = len(flatten(test_coll)) - start_len
    assert abs(difference) <= 1
