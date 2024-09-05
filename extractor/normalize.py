import pandas as pd
import re 

def normalize(data: str):
    for func_name in function_dict:
        data = function_dict[func_name](data)
    return data

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

def replace_n(text: str): # remplaza Ã± por ñ 
    return text.replace("Ã±", "ñ")

def replace_o(text : str):
    return text.replace("Ã³","ó")

def replace_a(text : str):
    return text.replace("Ã¡","á")

def replace_i(text : str):
    return text.replace("Ã-","í")

def replace_e(text : str):
    return text.replace("Ã©","é")

def replace_u(text : str):
    return text.replace("Ã° ","ú")

function_dict = {
    "space_in_dimensions": space_in_dimensions,
    "replace_mts": replace_mts,
    "replace_newlines": replace_newlines,
    "replace_stars": replace_stars,
    "replace_numeric": replace_numeric,
    "replace_dashes": replace_dashes,
    "replace_multiple_spaces": replace_multiple_spaces,
    "replace_number_commas_by_dots": replace_number_commas_by_dots,
    "replace_n": replace_n,
    "replace_o": replace_o,
    "replace_a": replace_a,
    "replace_i": replace_i,
    "replace_e": replace_e,
    "replace_u": replace_u
}
