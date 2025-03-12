from langchain.chains import LLMChain
from langchain.chains.base import Chain
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

template = """Please support tourism in Japan.
input:{input}
output:"""


def create_chain() -> Chain:
    llm = Ollama(model='llama3.1:8b')
    prompt = PromptTemplate(template=template, input_variables=["input"])
    return LLMChain(prompt=prompt, llm=llm, verbose=True)
