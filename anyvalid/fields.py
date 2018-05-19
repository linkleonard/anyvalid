from anyvalid.exceptions import ValidationError

class Field(object):
    def validate(self, thing):
        raise NotImplemented()


class TypedField(Field):
    _type = None

    def validate(self, thing):
        if not isinstance(thing, self._type):
            raise ValidationError(
                "{!r} is not instance of type {}".format(thing, self._type)
            )


class BooleanField(TypedField):
    _type = bool


class IntegerField(TypedField):
    _type = int


class CharField(TypedField):
    _type = str
