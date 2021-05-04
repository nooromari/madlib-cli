# import re
# print('Welcome to Madlib game, please input the blanks')

# def read_template(file_path):
#     with open(file_path, "r") as f:
#         return f.read().strip('\n')

# def parse_template(text):
#     # text = read_template("assets/dark_and_stormy_night_template.txt")
#     # s =  [e+'' for e in re.split('{|}',text)]
#     partsre = re.findall(r'\{.*?\}', text) 
#     print(partsre)
#     newtext = text.split(' ')
#     parts = []
#     for t in newtext:
#         if not t.find('{'):
#            parts.append(t)
#            text=text.replace(t,"{}")
#     parts = [ele.replace('{','') for ele in parts]
#     parts = [ele.replace('}','') for ele in parts]
#     parts_t = ()
#     for i in parts:
#         parts_t += (i,)
#     actual_stripped=text+'.'
#     actual_parts=parts_t
#     return actual_stripped, actual_parts

# parse_template(
#         "It was a {Adjective} and {Adjective} {Noun}."
#     )

import re
print('Welcome to Madlib game, please input the blanks')

def read_template(file_path):
    with open(file_path, "r") as f:
        return f.read().strip('\n')

def parse_template(text):
    parts=[]
    parts = re.findall(r'\{.*?\}', text) 
    for i in range(len(parts)):
        parts[i] = parts[i].replace("{", "")
        parts[i] = parts[i].replace("}", "")
        
    for i in range(text.count('{')):
           text=text.replace(parts[i],"")
    parts_t = ()
    for i in parts:
        parts_t = parts_t + (i,)
    print(text)
    print(parts_t)
    return text , parts_t

def merge(text,parts):
    return text.format(*parts)

print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))

