import re
import os


def clean_text(text: str) -> str:
    time_stamp = re.compile(r".*-->.*")
    cleaned_text = time_stamp.sub("", text)
    subtitle_n = re.compile(r"\d")
    cleaned_text = subtitle_n.sub("", cleaned_text)
    new_line = re.compile(r"\n+")
    cleaned_text = new_line.sub("\n", cleaned_text)
    return cleaned_text


def add_text(id: str) -> str:
    with open(id) as subtitle:
        text = subtitle.read()
        return clean_text(text)


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
