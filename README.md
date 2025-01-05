This project is a Streamlit-based AI-powered web scraper designed to extract, clean, and process website content using large language models (LLMs) for natural language understanding

Its combines web scraping, advanced LLMs, and a user-friendly design, to allow users to enter any prompt to extract and analyze data from any website.

The development process involved (inside a virtual enviroment):

Content Scraping: A Python-based module was implemented to scrape website DOM elements and extract meaningful body content

Data Cleaning: Custom cleaning functions were developed to remove extraneous HTML tags and metadata, preparing the text for analysis

LLM Integration: Initially integrated with Ollama AI, the project enables the use of local LLMs for parsing user-defined instructions and generating results tailored to specific queries

Proxy Configuration: Configured a list of proxies, either static or rotating, to be used for making requests to the target website. This helps in bypassing IP-based restrictions and scraping websites without being detected as a bot (such as Amazon, which was one of the issues I had)

Chunk Processing: Large website content is split into smaller chunks, allowing the LLM to process data efficiently and accurately

Interactive UI: Built with Streamlit, the project provides an intuitive interface for users to input URLs, define how the data should be processed, and view results in real time


Python Libraries Used:

streamlit 
langchain 
langchain_ollama
selenium
beautifulsoup4
lxml 
html5lib
python-dotenv


