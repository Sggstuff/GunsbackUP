from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import os

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Route for server status
@app.route("/")
def home():
    return jsonify({"status": "Server is running!"})

# Example route for testing
@app.route("/api/test", methods=["GET"])
def test_route():
    return jsonify({"message": "API is working!"})

# Socket.IO event for player connections
@socketio.on("connect")
def on_connect():
    print("A client connected")
    emit("server_message", {"message": "Welcome to the private server!"})

@socketio.on("disconnect")
def on_disconnect():
    print("A client disconnected")

# Socket.IO custom event
@socketio.on("custom_event")
def handle_custom_event(data):
    print(f"Received data: {data}")
    emit("response_event", {"message": "Event received!"})

# Run the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT as an environment variable
    socketio.run(app, host="0.0.0.0", port=port)

