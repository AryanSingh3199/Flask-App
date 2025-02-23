from flask import Flask
import os
import datetime
import pytz
import psutil
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Aryan Singh"

    system_username = os.getenv("USER") or os.getenv("USERNAME")

    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')


    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode("utf-8")
        top_display = "<pre>" + top_output[:1000] + "</pre>"  # Limiting output to 1000 characters
    except Exception as e:
        top_display = f"<p>Error fetching top output: {e}</p>"

    return f"""
    <html>
    <head><title>HTop Output</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {system_username}</p>
        <p><strong>Server Time (IST):</strong> {current_time}</p>
        <h2>Top Command Output:</h2>
        {top_display}
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
