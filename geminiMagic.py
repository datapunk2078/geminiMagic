# install Vertex AI SDK for Python
# ! pip3 install --upgrade --user google-cloud-aiplatform

# Import the necessary packages
import vertexai.preview.generative_models as genai
import IPython.core.magic as magic
from IPython.display import Markdown, display
from IPython.core.magic_arguments import (argument, magic_arguments, parse_argstring)
# from IPython.core.magic import parse_magic_args
import argparse

# Configure your API key if needed
# GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
# genai.configure(api_key=GOOGLE_API_KEY)
   
# Define a helper function to print the response from Gemini
def print_res(responses):
    
    res_md = ""
    for response in responses:
        # print(response.text, end="")
        res_md = res_md + response.text
    
    # Convert the string to Markdown
    display(Markdown(data=res_md))
    
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Define a custom magic function
@magic.magics_class
class GeminiMagic(magic.Magics):
    
    # Define a cell magic function
    @magic.line_cell_magic
    @magic_arguments()
    @argument("-a", "--cache", type=str2bool, default=False, help="To retrieve from cache or not") #To be implemented
    @argument("-c", "--chat", type=str2bool, default=True, help="Chat mode or session mode")
    @argument("-n", "--new_chat", type=str2bool, default=False, help="New chat or not") #To be implemented
    @argument("-i", "--chat_history", type=str2bool, default=False, help="Chat history or None") #To be implemented
    @argument("-t", "--temperature", type=float, default=0.7, help="Temperature for the generation")
    @argument("-p", "--p", type=float, default=0.9, help="Top-p for the generation")
    @argument("-k", "--k", type=int, default=32, help="Top-k for the generation")
    @argument("-d", "--candidate", type=int, default=1, help="Number of candidates for the generation")
    @argument("-x", "--max_token_output", type=int, default=8192, help="Maximum number of tokens for the output")
    @argument("-m", "--markdown_output", type=str2bool, default=True, help="Convert the output in markdown format")
    def gemini(self, line, cell):
        # Get the parsed arguments
        args = parse_argstring(self.gemini, line)
        # args = parse_magic_args(self.gemini, line)
        print(args)
        generation_config = genai.GenerationConfig(
            temperature=args.temperature,
            top_p=args.p,
            top_k=args.k,
            candidate_count=args.candidate,
            max_output_tokens=args.max_token_output,
        )
        
        # Get the model
        model = genai.GenerativeModel("gemini-pro")
        
        # Generate the response
        if args.chat:
            # Use the chat method
            
            # Enforce reply in MD format
            if args.markdown_output:
                cell = cell + " please response in markdown format"
            
            print("chat mode is enabled")
            responses = model.start_chat().send_message(cell, generation_config=generation_config, stream=True)
        else:
            # Use the generate_content method
            print("session mode is enabled")
            responses = model.generate_content(cell, generation_config=generation_config, stream=True)
        
        # Print the response
        print_res(responses)

# Register the magic function
def load_ipython_extension(ipython):
    ipython.register_magics(GeminiMagic)
