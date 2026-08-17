import os
from django.conf import settings
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Initialize the Groq client once at module load
_llm = None

def get_llm():
    global _llm
    if _llm is None:
        _llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.GROQ_MODEL,
            streaming=True
        )
    return _llm

def generate_title(first_message_content: str) -> str:
    """Generate a short title (max 5 words) based on the first message."""
    llm = get_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a very short, concise title (maximum 5 words) for a chat thread starting with this message. Only return the title itself, no quotes, no extra text."),
        ("human", "{message}")
    ])
    chain = prompt | llm
    response = chain.invoke({"message": first_message_content})
    return response.content.strip('"').strip()

def stream_chat_response(messages: list, new_message_content: str):
    """
    Takes a list of LangChain Message objects (history) and the new user message.
    Yields chunks of text directly from the LangChain streaming response.
    """
    llm = get_llm()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful, concise AI assistant. Format your response in markdown."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm
    
    for chunk in chain.stream({"history": messages, "input": new_message_content}):
        if chunk.content:
            yield chunk.content


if __name__ == "__main__":
    for chunk in stream_chat_response([], "What is Django?"):
        print(chunk, end="", flush=True)