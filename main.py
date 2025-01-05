import streamlit as st
from scrapingcode import scrape_website, split_dom_content, clean_body_content, extract_body_content

from parsingcode import parse_with_ollama


st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ")

if st.button("Scrape The Website!"): #if they press the button then scrape the site
    st.write("Scraping the Website...") # prompt while scraping
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("How would you like to visualize or use the data from this website?")

    if st.button("Get My Results"):
        if parse_description:
            st.write("Parsing the Website...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description) #connect it to the Ollama AI
            st.write(result)#write the result to the terminal