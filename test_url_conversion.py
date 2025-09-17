#!/usr/bin/env python3

import sys
import os

# Add the current directory to path to import from faq_processor
sys.path.insert(0, os.getcwd())
from faq_processor import convert_plain_urls_to_markdown

def test_url_conversion():
    print("Testing URL conversion function...")
    
    test_cases = [
        # Plain URLs
        "Check this Video: https://www.loom.com/share/710e3297487b409d94df0e8da1c984ce",
        "2025: https://courses.datatalks.club/de-zoomcamp-2025/enrollment",
        "Yes to both! check out this document: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/awesome-data-engineering.md",
        
        # Already formatted markdown links (should be preserved)
        "brew install conflict with docker desktop and command line tools. You need to install docker desktop first and then the command line tools. [Issue](https://github.com/Homebrew/brew/issues/16309)",
        
        # Mixed content
        "Visit https://docs.google.com/spreadsheets/example and see [GitHub](https://github.com/example) for details",
        
        # Edge cases
        "URL at end: https://stackoverflow.com/help/how-to-ask ",
        "Multiple URLs: https://github.com/test and https://docs.google.com/example",
        
        # Complex URLs with parameters
        "After you submit your homework it will be graded based on the amount of questions in a particular homework. You can see how many points you have right on the page of the homework up top. Additionally in the leaderboard you will find the sum of all points you've earned - points for Homeworks, FAQs and Learning in Public. If homework is clear,(https://datatalks-club.slack.com/archives/C01FABYF2RG/p1706846846359379? others work as follows:"
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1} ---")
        print(f"Input:  {test_case}")
        result = convert_plain_urls_to_markdown(test_case)
        print(f"Output: {result}")
        print(f"Changed: {'Yes' if result != test_case else 'No'}")

if __name__ == "__main__":
    test_url_conversion()