import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from boyer_moore import boyer_moore_search

def run_tests():
    print("==================================================")
    print("RUNNING BOYER-MOORE ALGORITHM TESTING")
    print("==================================================\n")
    
    # sample text and pattern to search for
    sample_text = "HERE IS A SIMPLE EXAMPLE OF MATCHING A SIMPLE PATTERN"
    sample_pattern = "SIMPLE"
    
    print(f"Test Text: '{sample_text}'")
    print(f"Target Pattern: '{sample_pattern}'\n")
    
    results = boyer_moore_search(sample_text, sample_pattern)
    
    # display results
    print("--------------------------------------------------")
    print("ALGORITHM OUTPUT:")
    print("--------------------------------------------------")
    if results:
        # pattern found
        # print the starting indices and the matched context
        print(f"Pattern found at starting indices: {results}")
        for idx in results:
            print(f"Match context: {sample_text[idx:idx+len(sample_pattern)]} at index {idx}")
    else:
        # pattern not found
        print("Pattern not found in the provided text.")
    print("==================================================")

if __name__ == "__main__":
    run_tests()