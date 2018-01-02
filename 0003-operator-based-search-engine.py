all_elements = [
    ["rap", "us", "english", "eminem", "movie_related"], # Eminem - Lose Yourself
    ["rap", "us", "english", "tupac", "diss_song"], # Tupac - Hit 'Em Up
    ["rap", "france", "french", "nekfeu"], # Nekfeu - On Verra
    ["rap", "us", "english", "eminem", "ed_sheeran", "feat"], # Eminem - River ft. Ed Sheeran
    ["france", "french", "edith_piaf", "old"], # Edith Piaf - Non, je ne regrette rien
    ["england", "english", "ed_sheeran"] # Ed Sheeran - Shape of You
]

def elements_are_identical(elements_ids_1, elements_ids_2):
    if len(elements_ids_1) != len(elements_ids_2):
        return False
    i = 0
    while i < len(elements_ids_1):
        if (elements_ids_1[i] != elements_ids_2[i]):
            return False
        i += 1
    return True

def element_contains_label(element, label):
    for element_label in element:
        if element_label == label:
            return True
    return False

def get_all_elements_ids():
    matching_elements_ids = []
    i = 0
    while i < len(all_elements):
        matching_elements_ids.append(i)
        i += 1
    return matching_elements_ids

def get_all_elements_ids_except_label(exception_label):
    matching_elements_ids = []
    i = 0
    while i < len(all_elements):
        if not element_contains_label(all_elements[i], exception_label):
            matching_elements_ids.append(i)
        i += 1
    return matching_elements_ids

def get_elements_ids_based_on_label(label):
    matching_elements_ids = []
    i = 0
    while i < len(all_elements):
        if element_contains_label(all_elements[i], label):
            matching_elements_ids.append(i)
        i += 1
    return matching_elements_ids

def get_union_ids(elements_ids_1, elements_ids_2):
    return list(set(elements_ids_1 + elements_ids_2))

def get_intersection_ids(elements_ids_1, elements_ids_2):
    return list(set(elements_ids_1).intersection(elements_ids_2))

def get_symmetric_difference_ids(elements_ids_1, elements_ids_2):
    if len(elements_ids_1) < len(elements_ids_2):
        return list(set(elements_ids_1).symmetric_difference(elements_ids_2))
    return list(set(elements_ids_2).symmetric_difference(elements_ids_1))

def get_elements(search_query):
    if (search_query == "ALL"):
        return get_all_elements_ids()
    # Binary operators
    if ("OR" in search_query or "AND" in search_query or "XOR" in search_query or "AND_NOT" in search_query or "OR_NOT" in search_query or "XOR_NOT" in search_query):
        decomposed_search_query = search_query.split(' ')
        matching_elements_ids_1 = get_elements_ids_based_on_label(decomposed_search_query[0])

        if ("AND_NOT" in search_query or "OR_NOT" in search_query or "XOR_NOT" in search_query):
            matching_elements_ids_2 = get_all_elements_ids_except_label(decomposed_search_query[2])
        else:
            matching_elements_ids_2 = get_elements_ids_based_on_label(decomposed_search_query[2])

        if ("XOR_NOT" in search_query or "XOR" in search_query):
            return get_symmetric_difference_ids(matching_elements_ids_1, matching_elements_ids_2)
        if ("OR_NOT" in search_query or "OR" in search_query):
            return get_union_ids(matching_elements_ids_1, matching_elements_ids_2)
        if ("AND_NOT" in search_query or "AND" in search_query):
            return get_intersection_ids(matching_elements_ids_1, matching_elements_ids_2)
    # Unary operator
    if ("NOT" in search_query):
        decomposed_search_query = search_query.split(' ')
        return get_all_elements_ids_except_label(decomposed_search_query[1])
    return get_elements_ids_based_on_label(search_query)

# Tests

results = get_elements("ALL")
print(elements_are_identical(results, [0, 1, 2, 3, 4, 5]))

results = get_elements("france")
print(elements_are_identical(results, [2, 4]))

results = get_elements("germany")
print(elements_are_identical(results, []))

results = get_elements("eminem")
print(elements_are_identical(results, [0, 3]))

results = get_elements("NOT us")
print(elements_are_identical(results, [2, 4, 5]))

results = get_elements("NOT germany")
print(elements_are_identical(results, [0, 1, 2, 3, 4, 5]))

results = get_elements("eminem OR tupac")
print(elements_are_identical(results, [0, 1, 3]))

results = get_elements("macklemore OR snoop_dogg")
print(elements_are_identical(results, []))

results = get_elements("eminem OR eminem")
print(elements_are_identical(results, [0, 3]))

results = get_elements("eminem AND ed_sheeran")
print(elements_are_identical(results, [3]))

results = get_elements("eminem AND tupac")
print(elements_are_identical(results, []))

results = get_elements("eminem AND eminem")
print(elements_are_identical(results, [0, 3]))

results = get_elements("eminem XOR ed_sheeran")
print(elements_are_identical(results, [0, 5]))

results = get_elements("rap XOR us")
print(elements_are_identical(results, [2]))

results = get_elements("macklemore XOR snoop_dogg")
print(elements_are_identical(results, []))

results = get_elements("eminem XOR eminem")
print(elements_are_identical(results, []))

results = get_elements("eminem AND_NOT ed_sheeran")
print(elements_are_identical(results, [0]))

results = get_elements("eminem AND_NOT eminem")
print(elements_are_identical(results, []))

results = get_elements("eminem OR_NOT ed_sheeran")
print(elements_are_identical(results, [0, 1, 2, 3, 4]))

results = get_elements("eminem OR_NOT eminem")
print(elements_are_identical(results, [0, 1, 2, 3, 4, 5]))

results = get_elements("eminem XOR_NOT ed_sheeran")
print(elements_are_identical(results, [1, 2, 3, 4]))

results = get_elements("eminem XOR_NOT eminem")
print(elements_are_identical(results, [0, 1, 2, 3, 4, 5]))
