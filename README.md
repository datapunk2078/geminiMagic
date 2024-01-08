# Gemini Magic Function
This magic function is a wrapper on Google Gemini for easier data exploration in Jupyter notebooks. It provides a convenient way to interact with Gemini and generate text, code, or other content.

## Installation
To install the magic function, run the following command in your terminal:
pip install geminiMagic

## Usage
To use the magic function, first load it into your Jupyter notebook by running the following command:

%load_ext gemini_magic
Once the magic function is loaded, you can use it by typing %%gemini followed by the desired arguments and cell content.

## Arguments
The magic function supports the following arguments:

-a, --cache: Whether to retrieve the response from the cache. Default is False.  
-c, --chat: Whether to use the chat mode or the session mode. Default is True.  
-n, --new_chat: Whether to start a new chat. Default is False.  
-i, --chat_history: Whether to include the chat history in the request. Default is False.  
-t, --temperature: The temperature for the generation. Default is 0.7.  
-p, --p: The top-p for the generation. Default is 0.9.  
-k, --k: The top-k for the generation. Default is 32.  
-d, --candidate: The number of candidates for the generation. Default is 1.  
-x, --max_token_output: The maximum number of tokens for the output. Default is 8192.  
-m, --markdown_output: Whether to convert the output in markdown format. Default is True.  

## Examples
Here are a few examples of how to use the magic function:

To generate a text response from a given prompt:
%%gemini
Hello, how are you?
To generate a code response from a given prompt:
%%gemini -m False
def add_two_numbers(a, b):
  return a + b
To start a new chat session:
%%gemini -n
Hi there, I'm Gemini. How can I help you today?
To continue a chat session:
%%gemini -c
I'm not sure how to do that. Can you give me an example?

# Additional Information
For more information on the magic function, please refer to the following resources:

Gemini Magic Function Documentation  
Google Gemini Documentation  
