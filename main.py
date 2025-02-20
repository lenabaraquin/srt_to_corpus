import re


def add_text(id: str) -> str:
    with open(id, encoding="iso-8859-15") as subtitle:
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
        return cleaned_text


def add_start_balise(id: str) -> str:
    to_add = "<id = "
    to_add += id
    to_add += ">"
    return to_add


def add_end_balise() -> str:
    to_add = "</id>"
    return to_add


def generate_corpus() -> str:
    id = "test.srt"
    corpus = ""
    corpus += add_start_balise(id)
    corpus += add_text(id)
    corpus += add_end_balise()
    return corpus


corpus = generate_corpus()
print(corpus)
