def sort_on(items):
    return items["num"]


def get_num_words(string):
    return len(string.split())


def get_char_count(string):
    chars = {}
    for c in string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_sorted_dictionary_list(dictionary):
    dictionary_list = []
    for i in dictionary:
        single_dict = dict()
        lowered = i.lower()
        single_dict["char"] = lowered
        single_dict["num"] = dictionary[i]
        dictionary_list.append(single_dict)
        dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list
