def find_value(given_dict, search_phrase):
    success = search_function(given_dict, search_phrase)
    if success:
        print(success)
    else:
        print(f"No {search_phrase} found")


def search_function(given_dict, search_phrase):
    found = ""
    for key in given_dict.keys():
        if type(given_dict[key]) == dict:
            found = search_function(given_dict[key], search_phrase)
            if found:
                return found
        if type(given_dict[key]) == list:
            for list_entry in given_dict[key]:
                found = search_function(list_entry, search_phrase)
                if found:
                    return found
        if given_dict[key] == search_phrase:
            found = search_phrase + f" found with key - {key}"
            return found
    return found


if __name__ == "__main__":
    default_dict = {
        "book": "151012",
        "identifier": [
            {"type": "ABC", "value": "3806768526"},
            {"type": "DEF", "value": "97789689"},
        ],
    }

    first_custom_dict = {
        "book": {"type": "DEF", "value": "3806768526"},
        "identifier": "ABC"
    }

    second_custom_dict = {
        "owner": "John",
        "collection": [
            {"book": "151012",
             "identifier": [
                 {"type": "CBD", "value": "3806768526"},
                 {"type": "DEF", "value": "97789689"},
             ], },
            {"book": "1770012",
             "identifier": [
                 {"type": "XYZ", "value": "3806768526"},
                 {"type": "DEF", "value": "97789689"},
                 {"type": "ABC", "value": "97789689"},
             ], }
        ]

    }

    first_search = "ABC"

    second_search = "GHI"

    find_value(default_dict, first_search)
    find_value(default_dict, second_search)
    find_value(first_custom_dict, first_search)
    find_value(second_custom_dict, first_search)
