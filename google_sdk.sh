sudo apt-get install portaudio19-dev libffi-dev libssl-dev
python3 -m pip install --upgrade google-assistant-sdk[samples]
python3 -m pip install --upgrade google-auth-oauthlib[tool]
python3 -m pip install --upgrade google-assistant-sdk[samples]
python3 -m pip install --upgrade google-auth-oauthlib[tool]
google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
      --save --headless --client-secrets /media/robo/nvidia/client_secret_826256963145-d7dolbutep89vuhl90sd22l0pni0sj7n.apps.googleusercontent.com.json
