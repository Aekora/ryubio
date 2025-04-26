from flask import Flask, request, redirect, send_from_directory
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static')

# Serve frontend
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# Serve static files
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Discord OAuth callback
@app.route('/auth/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Missing authorization code", 400
    
    data = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': os.getenv('REDIRECT_URI'),
        'scope': 'identify guilds.join'
    }
    
    response = requests.post(
        'https://discord.com/api/oauth2/token',
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    if response.status_code != 200:
        return "Authentication failed", 400
    
    return redirect('/?verified=true')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)