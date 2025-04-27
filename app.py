from flask import Flask, jsonify, render_template_string
import json
import os
from prometheus_client import Counter, Gauge, generate_latest, REGISTRY

app = Flask(__name__)

# Define Prometheus metrics
cpu_gauge = Gauge('system_cpu_usage', 'CPU usage percentage')
memory_gauge = Gauge('system_memory_usage', 'Memory usage percentage')
disk_gauge = Gauge('system_disk_free', 'Free disk space in GB')
request_counter = Counter('http_requests_total', 'Total HTTP Requests', ['endpoint'])

@app.route("/metrics")
def metrics():
    # Read the latest data
    update_metrics()
    return generate_latest(REGISTRY)

def update_metrics():
    """Update prometheus metrics from data.json"""
    try:
        with open('data.json') as f:
            data = json.load(f)
        # Update gauge values
        cpu_gauge.set(float(data["cpu_usage"]))
        memory_gauge.set(float(data["memory_usage"]))
        # Convert disk free to numerical value if needed
        disk_free = data["disk_free"].replace('G', '')
        disk_gauge.set(float(disk_free))
    except Exception as e:
        print(f"Error updating metrics: {e}")

@app.route("/api")
def api():
    request_counter.labels(endpoint='/api').inc()
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/")
def dashboard():
    request_counter.labels(endpoint='/').inc()
    with open('data.json') as f:
        data = json.load(f)
    
    # Updated HTML with Bootstrap for better UI
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>System Monitoring Dashboard</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <meta http-equiv="refresh" content="30">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <h1 class="mb-4 text-center">Server Monitoring Dashboard</h1>
            
            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="card border-primary">
                        <div class="card-header bg-primary text-white">
                            <h5 class="mb-0">CPU Usage</h5>
                        </div>
                        <div class="card-body">
                            <h2 class="display-4">{{ cpu }}%</h2>
                            <div class="progress mt-2">
                                <div class="progress-bar bg-primary" role="progressbar" style="width: {{ cpu }}%" 
                                     aria-valuenow="{{ cpu }}" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card border-success">
                        <div class="card-header bg-success text-white">
                            <h5 class="mb-0">Memory Usage</h5>
                        </div>
                        <div class="card-body">
                            <h2 class="display-4">{{ memory }}%</h2>
                            <div class="progress mt-2">
                                <div class="progress-bar bg-success" role="progressbar" style="width: {{ memory }}%" 
                                     aria-valuenow="{{ memory }}" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4 mb-4">
                    <div class="card border-warning">
                        <div class="card-header bg-warning text-dark">
                            <h5 class="mb-0">Disk Free</h5>
                        </div>
                        <div class="card-body">
                            <h2 class="display-4">{{ disk }}</h2>
                            <p class="text-muted">Available space</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="text-center mt-3">
                <a href="/api" class="btn btn-secondary">View JSON API</a>
                <a href="http://localhost:3000" class="btn btn-info">Open Grafana Dashboard</a>
                <a href="/metrics" class="btn btn-dark">Prometheus Metrics</a>
            </div>
            
            <div class="mt-5 text-center text-muted">
                <small>Auto-refreshes every 30 seconds • Last update: {% now 'timezone', '%H:%M:%S' %}</small>
            </div>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, cpu=data["cpu_usage"], memory=data["memory_usage"], disk=data["disk_free"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify, render_template  # יש לוודא שהמודול render_template מיובא

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # וודא שאתה Return את קובץ ה-HTML שלך

@app.route('/api/system-stats', methods=['GET'])
def system_stats():
    # כאן תשים לוגיקה לקבלת הנתונים
    data = {
        'cpu': 30,      # זה ערך דוגמה, תחליף עם ערך אמיתי
        'memory': 16,   # זה ערך דוגמה, תחליף עם ערך אמיתי
        'disk': 250     # זה ערך דוגמה, תחליף עם ערך אמיתי
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

