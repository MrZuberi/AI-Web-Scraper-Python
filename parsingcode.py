#Using Ollama to run LLMs on my computer locally

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# A template to instruct the AI model (ollama) with what we want it to do with user prompts
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string (''), nothing else."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    "5. **Do not provide false data, make sure you carefully read what the user has inputted."
)

model = OllamaLLM(model = "llama3.2")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model #goes to prompt and then calls the model
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start =1):

        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})

        print(f"Parsing chunks: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results) #take reulsts and join them with a  new line character