def bad_character_table(pattern):
    """
    Preprocesses the pattern to create the Bad Character Table.
    Stores the last occurrence index of each character in the pattern.
    """
    bad_char = {}
    pattern_length = len(pattern)
    
    # fill the dictionary with the last seen index of each character
    for i in range(pattern_length):
        character = pattern[i]
        bad_char[character] = i
        
    return bad_char


def good_suffix_table(pattern):
    """
    Preprocesses the pattern to create the Good Suffix Table.
    Determines shifts based on matching suffixes when a mismatch occurs.
    """
    m = len(pattern)
    good_suffix = [0] * (m + 1)
    suff = [0] * (m + 1)
    
    # base case setup
    suff[m] = m
    g = m - 1
    for i in range(m - 2, -1, -1):
        if i > g and suff[i + m - 1 - f] < i - g:
            suff[i] = suff[i + m - 1 - f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                g -= 1
            suff[i] = f - g

    for i in range(m + 1):
        good_suffix[i] = m

    j = 0
    for i in range(m - 1, -1, -1):
        if suff[i] == i + 1:
            while j < m - 1 - i:
                if good_suffix[j] == m:
                    good_suffix[j] = m - 1 - i
                j += 1
                
    for i in range(m - 1):
        good_suffix[m - 1 - suff[i]] = m - 1 - i

    return good_suffix

def boyer_moore_search(text, pattern):
    """
    Executes the Boyer-Moore string matching algorithm.
    Returns a list of starting indices where the pattern is found in the text.
    """
    n = len(text)
    m = len(pattern)
    matches = []
    
    # if the pattern is empty, return no matches
    if m == 0 or n == 0 or m > n:
        return matches

    # generate shift tables
    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)
    
    shift = 0
    while shift <= (n - m):
        j = m - 1  # start matching from the right end of the pattern
        
        # keep moving left as long as characters match
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
            
        if j < 0:
            # match found
            # record the starting index of the match
            matches.append(shift)
            # shift the pattern past this match using the good suffix rule
            shift += good_suffix[0]
        else:
            # mismatch found at pattern index j
            mismatched_char = text[shift + j]
            
            # calculate bad character shift
            if mismatched_char in bad_char:
                bad_char_shift = j - bad_char[mismatched_char]
            else:
                bad_char_shift = j + 1
                
            # calculate good suffix shift
            good_suffix_shift = good_suffix[j]
            
            # take the maximum of both rules to skip as much text as safely possible
            shift += max(1, max(bad_char_shift, good_suffix_shift))
            
    return matches