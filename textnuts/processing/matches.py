from enum import Enum

class MatchesType(Enum):
    
    EMAIL = "email_reg"
    PHONE_NUMBER = "phone_number_reg"
    DIGIT = "digit_reg"
    SPECIAL_CHARACTERS = "special_char_reg"
    HTML_TAGS=""
    URL = "url_reg"
    
    
    