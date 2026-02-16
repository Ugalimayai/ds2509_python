def count_elements(s):
    counts = {}
    for char in s:
        #loops over each element of s and returns how many times it appears
        counts[char] = counts.get(char, 0) + 1
    return counts


def calculate_similarity_score(list1, list2):
    """
    Calculate similarity score between two frequency dictionaries.

    Returns a float rounded to 2 decimal places.
    """

    freq_dict1 = count_elements(list1) #get a dictionary of element and count
    freq_dict2 = count_elements(list2)

    # Get all unique elements from both dictionaries
    all_keys = set(freq_dict1.keys()) | set(freq_dict2.keys())


    # Calculate delta (absolute difference) and sigma (sum) for each element
    total_delta = 0
    total_sigma = 0

    for key in all_keys:
        #loop over the unique set union values
        count1 = freq_dict1.get(key, 0) #for every element key, it counts the number of times it appeared in freq_dict1. if not, it returns 0
        count2 = freq_dict2.get(key, 0)


        total_delta += abs(count1 - count2) #update the total delta variable on each iteration
        total_sigma += count1 + count2


    # Calculate similarity score
    similarity = 1 - (total_delta / total_sigma)

    # Round to 2 decimal places
    return round(similarity, 2)

L1 = "hello"
L2 = "jello"
print(calculate_similarity_score(L1, L2))

# Alternatively we can import the Counter frequency dictionary which does what the count_elements functions tries to achieve
