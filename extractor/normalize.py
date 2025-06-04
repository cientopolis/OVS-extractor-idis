import pandas as pd
import re 

def space_in_dimensions(text):
    return re.sub(r'(\d+)\s*[xX]\s*(\d+)', r'\1 x \2', text, flags=re.IGNORECASE)

def replace_mts(text):
    return re.sub(r'(\d+)(mts|m2|m)',r'\1 \2', text)
    
def replace_newlines(text):
    return re.sub(r'\n\s*\n+', '. ', text).replace('\n', ' ')

def replace_stars(text: str):
    return text.replace("*", " ")

def replace_numeric(text: str):
    return text.replace("º", "°")

def replace_dashes(text: str):
    return re.sub(r'[-_]', ' ', text)

def replace_multiple_spaces(text):
    return re.sub(r'\s+', ' ', text) 

def replace_number_commas_by_dots(text):
    return (re.compile(r'(\d+),(\d+)')).sub(r'\1.\2', text)

def replace_dots_by_spaces(text):
    return "" if text == "." else text

def replace_NA_by_spaces(text):
    return "" if text == "NA" else text

def normalize(data: str):
    return space_in_dimensions(replace_mts(replace_newlines(replace_multiple_spaces(replace_numeric(replace_stars(replace_dashes(replace_number_commas_by_dots(replace_dots_by_spaces(replace_NA_by_spaces(data))))))))))
