import re
print('Welcome to Madlib game, please input the blanks')

def read_template(file_path):
    with open(file_path, "r") as f:
        return f.read().strip('\n')

def parse_template():
    text = read_template("assets/dark_and_stormy_night_template.txt")
    # s =  [e+'' for e in re.split('{|}',text)]
    newtext = text.split(' ')
    parts = []
    for t in newtext:
        if not t.find('{'):
           parts.append(t)
           rep_txt=text.replace(t,"{}")

    # for i in range(text.count('{')):
    #    parts.append(text[text.index('{')+1: text.index('}')])
    print(parts,rep_txt)
       
parse_template()