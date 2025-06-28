from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("🔔 Webhook Received!")
    print("📈 Symbol:", data.get('ticker'))
    print("⏰ Time:", datetime.fromtimestamp(data.get('time')/1000))
    print("💵 Price:", data.get('close'))
    print("🎯 TP:", data.get('plot_1'))
    print("🛡 SL:", data.get('plot_2'))
    print("📊 Score:", data.get('plotchar_0'))
    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
