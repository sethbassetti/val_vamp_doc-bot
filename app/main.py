# import requirements needed
from flask import Flask, render_template, request
from utils import get_base_url
from aitextgen import aitextgen
import openai
import os


openai.api_key = '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'
# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 8000
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)
else:
    app = Flask(__name__, static_url_path=base_url+'static')

    
    
    
# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    x = "Hello"
    return render_template('index.html', variable="")

@app.route(f'{base_url}', methods=['POST'])
def get_text():
    prompt = request.form['prompt']
    aiText = openai.Completion.create(
        engine = 'text-davinci-002',
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    text = aiText["choices"][0]["text"]
    return render_template('index.html', variable=text)

# define additional routes here
# for example:
# @app.route(f'{base_url}/team_members')
# def team_members():
#     return render_template('team_members.html') # would need to actually make this page

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    website_url = 'https://cocalc14.ai-camp.dev/'
    print(f'Try to open\n\n    {website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)
