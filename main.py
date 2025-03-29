import re
import os


def add_text(id: str) -> str:
    with open(id) as subtitle:
        cleaned_text = ""
        for line in subtitle:
            if re.match(r"^\d+", line):
                continue
            if re.match("-->", line):
                continue
            cleaned_text += line
            cleaned_text += "\n"
        re.sub(r"\n+", "\n", cleaned_text)
        return cleaned_text


def add_start_balise(id: str) -> str:
    to_add = "<id = "
    to_add += id
    to_add += ">"
    return to_add


def add_end_balise() -> str:
    to_add = "</id>"
    return to_add


def generate_corpus(dir_path: str) -> str:
    corpus = ""
    dir_content = os.listdir(dir_path)
    for id in dir_content:
        id = dir_path + "/" + id
        corpus += add_start_balise(id)
        corpus += add_text(id)
        corpus += add_end_balise()
    return corpus


corpus = generate_corpus("corpus_srt")
print(corpus)
