from .metaclass import ValidatorMetaclass
from anyvalid.exceptions import ValidationError


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
