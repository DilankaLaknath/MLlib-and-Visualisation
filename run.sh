#!/bin/bash
export FLASK_APP=web_app.py
export FLASK_DEBUG=1
nohup flask run &
sleep 2
python -c "import webbrowser; webbrowser.open('http://127.0.0.1:5000')"
