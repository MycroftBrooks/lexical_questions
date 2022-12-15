import re
from ..models import ChildQuestions

from better_profanity import profanity

def child_parser_db(word_input, title_list):
    words = {
        "nsfw",
        "sorry if",
        "reddit",
        "serious",
        "reddit",
        "redditor",
        "redditors",
        "reddit's",
        "onlyfans",
    }
    if profanity.contains_profanity(word_input):
        title = "YOUR SEARCH CONTAINS PROFANITY"
        data = {"question": title}
        title_list.append(data)
    else:
        ChildList = ChildQuestions.objects.filter(
            question__icontains=word_input
        )
        for sentence in ChildList:
            if profanity.contains_profanity(sentence.question) == 0:
                mut = words & set(re.findall(r"(\w+)", sentence.question.casefold()))
                if len(mut) == 0:
                    w = word_input[0].lower()
                    w1 = word_input[0].upper()
                    word = f"\\b[{w}{w1}]{word_input[1:]}\\w?\\b"
                    title = sentence.question
                    res = re.findall(word, title)
                    """ print(res) """
                    for e in res:
                        title = title.replace(
                            e, f"<mark><span style='color:green'>{e}</span></mark>"
                        )
                    data = {"title": title}
                    title_list.append(data)
            else:
                continue