---
id: 2e729f1271
question: 'I want the user to only be able to give feedback once per submission (+1
  or -1). For this I''m using a st.session attribute: submitted to enable or disable
  feedback buttons. When I submit text using the ask button. If I pressed +1, I''m
  allowed to repress +1 one more time (button not disabled). If I pressed -1, I''m
  allowed to repress +1 or -1 one more time (buttons not disabled). The buttons should
  be disabled if st.session.submitted is False. The issue is mainly in st.session.submitted,
  it gets somehow reassigned to True again, despite one feedback button being pushed.'
sort_order: 550
---

Solved:

[https://discuss.streamlit.io/t/streamlit-session-attributes-reassigned-somewhere/76059/2?u=mohammed2](https://discuss.streamlit.io/t/streamlit-session-attributes-reassigned-somewhere/76059/2?u=mohammed2)

