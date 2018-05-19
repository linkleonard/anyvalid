from anyvalid.fields import CharField, IntegerField
from anyvalid.validators import DictValidator


class PersonDictValidator(DictValidator):
    name = CharField()
    age = IntegerField()


def test_validator():
    validator = DictValidator()
    assert validator.is_valid({})


def test_person_validator():
    validator = PersonDictValidator()
    assert validator.is_valid({"name": "hi", "age": 1})


def test_person_validator_missing():
    validator = PersonDictValidator()
    assert not validator.is_valid({})


def test_person_validator_wrong_type():
    validator = PersonDictValidator()
    assert not validator.is_valid({"name": 1})


def test_person_validator_missing_age():
    validator = PersonDictValidator()
    assert not validator.is_valid({"name": "john"})
