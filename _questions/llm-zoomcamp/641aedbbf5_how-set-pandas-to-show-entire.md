---
course: llm-zoomcamp
id: 641aedbbf5
images:
- description: 'image #1'
  id: image_1
  path: images/llm-zoomcamp/image_603bbc41.png
question: How set Pandas to show entire text content in a column. Useful to view the
  entire Explanation column content in the LLM-as-judge section of the offline-rag-evaluation
  notebook
section: 'Module 4: Monitoring'
sort_order: 510
---

By default, in the dataframe visualization, Pandas truncate the text content in a column to 50 characters. In order to view the entire explanation given by the judge llm for a NON RELEVANT answer, as in figure:

<{IMAGE:image_1}>

The instruction to show the results must be preceded by:

pd.set_option('display.max_colwidth', None)

Here are the specs for the display_max_colwidth option, as describide in the [official docs](https://pandas.pydata.org/docs/user_guide/options.html):

display.max_colwidth : int or None

The maximum width in characters of a column in the repr of

a pandas data structure. When the column overflows, a "..."

placeholder is embedded in the output. A 'None' value means unlimited.

[default: 50] [currently: 50]

