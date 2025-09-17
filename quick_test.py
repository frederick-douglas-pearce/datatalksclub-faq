#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.getcwd())
from faq_processor import convert_plain_urls_to_markdown

test_text = "Check out: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1706846846359379?"
result = convert_plain_urls_to_markdown(test_text)
print("Input: ", test_text)
print("Output:", result)