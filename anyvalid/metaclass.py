from anyvalid.fields import Field


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
