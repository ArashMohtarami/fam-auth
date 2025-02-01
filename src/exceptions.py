class PasswordMatchError(Exception):
    """Raised when the new password is the same as the old password."""


class PasswordConfirmationError(Exception):
    """Raised when the new password and confirmation password do not match."""


class UsernameAlreadyExistsError(Exception):
    """Raised when the chosen username is already taken."""


class ImageUploadError(Exception):
    """Raised when there is an error in uploading the image."""


class InvalidPhoneNumberError(Exception):
    """Raised when the phone number is invalid."""


class UserNotFoundError(Exception):
    """Raised when a user is not found in the database."""
