%%gemini magic function
Overview
The %%gemini magic function is a wrapper around Google Gemini on Jupyter notebook for easier data exploration. It provides a convenient way to interact with Gemini, a conversational AI model, from within a Jupyter notebook.

Installation
To install the %%gemini magic function, run the following command in your terminal:

pip install vertexai-preview-generative-models
Once installed, you can load the magic function by running the following command in a Jupyter notebook:

%load_ext vertexai.preview.generative_models.gemini_magic
Usage
The %%gemini magic function can be used in two modes: chat mode and session mode.

Chat mode
In chat mode, the %%gemini magic function allows you to have a conversation with Gemini. To start a chat, simply type in a cell the text you want to say to Gemini. Gemini will then respond with a message in the next cell.

For example, to start a chat with Gemini about the weather, you could type the following in a cell:

%%gemini
Hello Gemini, what's the weather like today?
Gemini would then respond with a message in the next cell, such as:

Today's weather is mostly sunny with a high of 75 degrees Fahrenheit.
You can continue the conversation by typing in more cells.

Session mode
In session mode, the %%gemini magic function allows you to ask Gemini questions and receive answers. To ask a question, simply type in a cell the question you want to ask. Gemini will then respond with an answer in the next cell.

For example, to ask Gemini a question about the history of the United States, you could type the following in a cell:

%%gemini
What is the history of the United States?
Gemini would then respond with an answer in the next cell, such as:

The history of the United States begins with the arrival of European settlers in North America in the 16th century. The first permanent English settlement was Jamestown, Virginia, founded in 1607. Over the next century, thirteen colonies were established along the Atlantic coast.
You can continue the session by asking more questions.

Arguments
The %%gemini magic function supports a number of arguments that can be used to control its behavior. These arguments are:

-a, --cache: To retrieve from cache or not (To be implemented)
-c, --chat: Chat mode or session mode (default: True)
-n, --new_chat: New chat or not (To be implemented)
-i, --chat_history: Chat history or None (To be implemented)
-t, --temperature: Temperature for the generation (default: 0.7)
-p, --p: Top-p for the generation (default: 0.9)
-k, --k: Top-k for the generation (default: 32)
-d, --candidate: Number of candidates for the generation (default: 1)
-x, --max_token_output: Maximum number of tokens for the output (default: 8192)
-m, --markdown_output: Convert the output in markdown format (default: True)
Examples
Here are some examples of how to use the %%gemini magic function:

To have a conversation with Gemini about the weather, you could type the following in a cell:
%%gemini
Hello Gemini, what's the weather like today?
To ask Gemini a question about the history of the United States, you could type the following in a cell:
%%gemini
What is the history of the United States?
To generate a poem about a sunset, you could type the following in a cell:
%%gemini
Generate a poem about a sunset.
Conclusion
The %%gemini magic function is a powerful tool for interacting with Gemini from within a Jupyter notebook. It can be used to have conversations, ask questions, and generate creative content.
