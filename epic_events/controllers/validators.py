from validate_email import validate_email
from password_validator import PasswordValidator


def validate_password(password):

    schema = PasswordValidator()

    schema \
        .min(8) \
        .max(100) \
        .has().uppercase() \
        .has().lowercase() \
        .has().digits() \
        .has().no().spaces() \
        .has().symbols()

    return schema.validate(password)


def validate_email_adress(email):

    return validate_email(email)
