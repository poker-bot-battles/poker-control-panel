import websocket
import json
import streamlit as st

# button to connect to websocket
ws = websocket.WebSocket()
try:
        ws.connect("ws://localhost:8765")
        st.write("Connected to websocket")
except Exception as e:
    st.write("Connection failed error: ", e)

# check connection
if st.button("Check connection"):
    st.write("Connection status: ", ws.connected)

# check connected clients
if st.button("Check connected clients"):
    ws.send(json.dumps({"cmd": "get clients"}))
    result = ws.recv()
    st.write("Connected clients: ", json.loads(result)['clients'])

if st.button("Load"):
    try:
        ws.send(json.dumps({"cmd": "load"}))
        st.write("Load message sent")
    except Exception as e:
        st.write("Load failed error: ", e)

# button to send start message to websocket

if st.button("Start"):
    try:
        ws.send(json.dumps({"cmd": "start"}))
        st.write("Start message sent")
    except Exception as e:
        st.write("Start failed error: ", e)





