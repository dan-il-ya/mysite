def get_problems_for_table():
    with open("./data/problems.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        problems = []
        for i in range(len(lines)):
            num, num_section, text = i+1, int(lines[i][0]), lines[i][2:]
            if text[-1]=='\n':
                text = text[:-1]
            problems.append([num, num_section, text])
    return problems

def get_sections_dict():
    with open("./data/sections.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        sections_dict = {}
        for i in range(len(lines)):
            num, text = i+1, lines[i]
            if text[-1] =='\n':
                text = text[:-1]
            sections_dict[num] = text
    return sections_dict

def get_sections():
    return (get_sections_dict().items)

def add_section(new_section):
    with open("./data/sections.txt", "a", encoding="utf-8") as f:
        f.write('\n'+new_section)

def write_problem(section_num, problem_text):
    with open("./data/problems.txt", "a", encoding="utf-8") as f:
        f.write('\n'+str(section_num)+' '+problem_text)

def get_references():
    refs = []
    with open('./data/references.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines()[1:]:
            refs.append(line.split(';'))
            if (refs[-1][-1] == '\n'):
                refs[-1][-1] = ''
    return refs

def add_ref(author, title, link):
    with open("./data/references.csv", "a", encoding="utf-8") as f:
        f.write('\n'+author+';'+title+';'+link)
