# streamlit-searchbox

A streamlit custom component for a autocomplete searchbox

![Example](./img/example.gif)

## Installation

```python
pip install streamlit-searchbox
```

## Example Usage

```python
import streamlit as st
import wikipedia

from streamlit_searchbox import st_searchbox

def search_wikipedia(searchterm: str) -> List[str]:
    return wikipedia.search(searchterm) if searchterm else []

selected_value = st_searchbox(search_wikipedia, key="wiki_searchbox")

if selected_value:
    st.markdown("You've selected: %s" % selected_value)
```
