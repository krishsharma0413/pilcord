class PilcordError(Exception):
    """Base exception for :class:`Pilcord`"""
    def __init__(self, message: str):
        super().__init__(message)

class InvalidImageType(PilcordError):
    """Raised when the image type is not supported"""
    def __init__(self, message: str):
        super().__init__(message)

class InvalidImageUrl(PilcordError):
    """Raised when the image URL is invalid"""
    def __init__(self, message: str):
        super().__init__(message)    