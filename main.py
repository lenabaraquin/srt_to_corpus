import re

with open("test.srt", encoding="iso-8859-15") as subtitle:
    cleaned_text = ""
    for line in subtitle:
        line = line.replace("\n", "")
        if "" == line:
            continue
        if re.match(r"^\d+", line):
            continue
        if "-->" in line:
            continue
        line = re.sub(r"</?\w+>", "", line)
        cleaned_text += line
        cleaned_text += "\n"
    print(cleaned_text)
