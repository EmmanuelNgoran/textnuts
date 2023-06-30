"""_summary_

Returns:
    _type_: _description_
"""

from abc import ABC,abstractmethod
from typing import List, Any, TypeVar 
from joblib import Parallel



class TextTransformer(ABC):
    """base class that contains an abstract method representing 
    all the different text transformers
    

    Args:
        ABC (_type_): _description_

    Returns:
        _type_: _description_
    """
    @abstractmethod
    def transform():
        return NotImplementedError
    

T = TypeVar('T',TextTransformer,str)

class Pipeline(TextTransformer):
    
    def __init__(self,transformers:List[T]) -> None:
        assert transformers!= None and len(transformers) > 0 ,"The transformer must be not be none or empty"
        
        self.__transformers = transformers
    
    def transform(self,texts, n_jobs=1, backend='multiprocessing') -> List[str]:
        """Apply the text transformers on the input text

        Args:
            texts (_type_): _description_
            n_jobs (int, optional): _description_. Defaults to 1.
            backend (str, optional): _description_. Defaults to 'multiprocessing'.

        Returns:
            List[str]: _description_
        """
        parralel = Parallel(n_jobs=n_jobs, return_generator=True)
        output_gen = parralel(self._pipe(text) for text in texts )
        
        return list(output_gen)
        
    def _pipe(self, text:str) -> List[str]:
        """_summary_

        Args:
            text (str): _description_

        Returns:
            List[str]: _description_
        """
        results = [ transformer.transform(str) for transformer in self.__transformers ]
        return results 
    
    
    
    
        
        
        
    
    
    
    
