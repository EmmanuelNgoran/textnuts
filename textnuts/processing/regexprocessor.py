from .. import base
from typing import List, Dict
from .matches import MatchesType
from ..config import regex_pattern
import re

class RegexRuler(base.TextTransformer):
    
    def __init__(self,name,matches_types=List[MatchesType]) -> None:
        self.name = name
        self.matches_type = matches_types
        
    
    def transform(self,text:str) -> str:
        SPACE_REG = r"\s{2,}"
        result_text = text
        for matches_type in self.matches_type:
            pattern = regex_pattern[matches_type.value]
            result_text = re.sub(pattern," ",result_text)
        
        return re.sub(SPACE_REG," ",result_text)
            
            
            
        
        


