from anyvalid.fields import Field
from anyvalid.exceptions import ValidationError


class ValidatorMetaclass(type):
    def __new__(cls, name, bases, clsdict):
        thing = super().__new__(cls, name, bases, clsdict)

        thing._validators = {
            fieldname: validator
            for fieldname, validator in vars(thing).items()
            if isinstance(validator, Field)
        }

        for fieldname in thing._validators:
            setattr(thing, fieldname, None)

        return thing


class BaseValidator(metaclass=ValidatorMetaclass):
    def __init__(self):
        self.errors = {}

    def is_valid(self, thing):
        raise NotImplemented()


class DictValidator(BaseValidator):

    def validate_field(self, field, thing):
        try:
            value = thing[field]
        except KeyError:
            raise ValidationError("{} not found".format(field))
        return self._validators[field].validate(value)


    def is_valid(self, thing):
        for field in self._validators:
            try:
                parsed = self.validate_field(field, thing)
            except ValidationError as e:
                self.errors[field] = e
            else:
                setattr(self, field, parsed)

        return not bool(self.errors)
