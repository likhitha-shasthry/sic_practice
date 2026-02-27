from flask import Flask, render_template_string, jsonify
from gpiozero import LED

app = Flask(__name__)
led = LED(17)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart LED Controller</title>
    <style>
        body {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .card {
            background: rgba(0,0,0,0.4);
            padding: 40px;
            border-radius: 20px;
            width: 300px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        h1 {
            margin-bottom: 10px;
        }

        .status {
            font-size: 22px;
            margin: 20px 0;
        }

        .on {
            color: #00ff99;
        }

        .off {
            color: #ff6b6b;
        }

        button {
            background: #00c6ff;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            color: white;
            border-radius: 30px;
            cursor: pointer;
            transition: 0.3s;
            margin-top: 20px;
        }

        button:hover {
            transform: scale(1.1);
            box-shadow: 0 0 15px #00c6ff;
        }

        .footer {
            margin-top: 25px;
            font-size: 12px;
            opacity: 0.7;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1> Smart LED</h1>
        <div id="status" class="status off">Status: OFF</div>
        <button onclick="toggleLED()">Toggle LED</button>
        <div class="footer">LED Controll</div>
    </div>

<script>
function toggleLED() {
    fetch("/toggle")
    .then(response => response.json())
    .then(data => {
        let status = document.getElementById("status");
        if (data.state === "ON") {
            status.innerHTML = "Status: ON";
            status.className = "status on";
        } else {
            status.innerHTML = "Status: OFF";
            status.className = "status off";
        }
    });
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/toggle")
def toggle():
    if led.is_lit:
        led.off()
        return jsonify(state="OFF")
    else:
        led.on()
        return jsonify(state="ON")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
