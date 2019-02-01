# anyvalid

This project contains utilities to create validators to validate python objects.

## Usage

First, create a `BaseValidator` subclass. Add as many `Field` subclasses to this validator class
that are necessary. Finally, call the `is_valid()` method with a payload.

### Validators

#### DictValidator

A validator to validate `dict` objects.

Example usage:

```
class PersonValidator(DictValidator):
    name = CharField()
    age = IntegerField()


validator = PersonValidator()

validator.is_valid({
    "name": "My name",
    "age": 35,
})
```

### Fields

#### BooleanField

#### CharField

#### IntegerField
