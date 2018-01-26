def count_words(typed,words):
    return len([x for x in words if x.lower() in typed.lower()])
