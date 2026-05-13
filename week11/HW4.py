
def is_odd(word):
    return len(word) % 2 == 1


def transform_sentence(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if is_odd(word):
            print(f"Word's length is {len(word)}. Transform")
            result.append(word[::-1])
        else:
            print(f"Word's length is {len(word)}. Not transform")
            result.append(word)

    return " ".join(result)


sentence = "happy computer science programming class!!"

transformed = transform_sentence(sentence)
print()
print("Transformed Sentence:", transformed)