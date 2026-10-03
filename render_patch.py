"""
render_patch.py
Render pe basic.py ko chalane ke liye wrapper.
Flask server + Telegram bot ek saath.
"""
import os
import sys
import threading
import asyncio
import logging

# Flask setup
from flask import Flask
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "OTP Bot is running", 200

@flask_app.route('/health')
def health():
    return "OK", 200

def run_flask_server():
    """Flask server ko background thread me chalao."""
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def run_bot():
    """basic.py ka main() call karo."""
    import basic
    basic.main()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("render_patch")
    logger.info("Starting Flask + Bot wrapper...")
    
    # Flask thread
    flask_thread = threading.Thread(target=run_flask_server, daemon=True)
    flask_thread.start()
    logger.info("[FLASK] Keep-alive server started on port %s", os.environ.get("PORT", 10000))
    
    # Bot thread
    logger.info("[BOT] Starting Telegram bot...")
    run_bot()