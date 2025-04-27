
from flask import Flask, jsonify, render_template_string
import json

app = Flask(__name__)

@app.route("/api")
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/")
def dashboard():
    with open('data.json') as f:
        data = json.load(f)
    html = '''
    <h1>Server Monitoring Dashboard</h1>
    <ul>
      <li><strong>CPU Usage:</strong> {{ cpu }}%</li>
      <li><strong>Memory Usage:</strong> {{ memory }}%</li>
      <li><strong>Disk Free:</strong> {{ disk }}</li>
    </ul>
    '''
    return render_template_string(html, cpu=data["cpu_usage"], memory=data["memory_usage"], disk=data["disk_free"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
