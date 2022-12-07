import websocket
import json
import streamlit as st

# button to connect to websocket
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    ws = websocket.WebSocket()
    try:
            ws.connect("wss://socket-p45vitbqra-ew.a.run.app")
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