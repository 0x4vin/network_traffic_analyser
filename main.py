from app import app
from analyzer.capture import start_capture
import threading

# Start the packet capture in a separate thread
def start_packet_capture():
    start_capture()

if __name__ == '__main__':
    # Start packet capture
    threading.Thread(target=start_packet_capture).start()
    app.run(debug=True, host='0.0.0.0', port=5000)
