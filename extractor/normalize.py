import pandas as pd
import re 


def replace_mts(text):
    return re.sub(r'(\d+)(mts|m2|m)',r'\1 \2', text)
    
def replace_newlines(text):
    return re.sub(r'\n\s*\n+', '. ', text).replace('\n', ' ')

def replace_stars(text: str):
    return text.replace("*", " ")

def replace_dashes(text: str):
    return re.sub(r'[-_]', ' ', text)

def replace_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text) 

def normalize(data: pd.DataFrame):
    return replace_mts(replace_newlines(replace_multiple_spaces(replace_stars(replace_dashes(data)))))
