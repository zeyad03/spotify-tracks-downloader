import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import time
import pandas as pd

# App configuration.
app = Flask(__name__)

app.secret_key = 'SECRET_KEY'
app.config['SESSION_COOKIES'] = 'SPOTIFY_SESSION'

@app.route('/')
def login():
  spotify_oauth = createOauth()
  auth_url = spotify_oauth.get_authorize_url()
  print(auth_url)
  return redirect(auth_url)

@app.route('/authorize')
def authorize():
  spotify_oauth = createOauth()
  session.clear()
  code = request.args.get('code')
  token_info = spotify_oauth.get_access_token(code)
  session["token_info"] = token_info
  return redirect("/getTracks")

@app.route('/logout')
def logout():
  for key in list(session.keys()):
    session.pop(key)
  return redirect('/')

@app.route('/getTracks')
def get_tracks():
  session['token_info'], authorized = get_token()
  session.modified = True
  if not(authorized):
    return redirect('/')
  sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
  results = []
  iter = 0
  while True:
    offset = iter * 50
    iter += 1
    currGroup = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
    for idx, item in enumerate(currGroup):
      track = item['track']
      val = track['name'] + " - " + track['artists'][0]['name']
      results += [val]

    if (len(currGroup) < 50):
      break

  df = pd.DataFrame(results, columns=["song names"])
  df.to_csv('songs.csv', index=False)
  return "done"

# Check for token validation.
def get_token():
  token_valid = False
  token_info = session.get("token_info", {})

  # Check for already stored token.
  if not(session.get('token_info', False)):
    token_valid = False
    return token_info, token_valid
  
  # Check expired token.
  now = int(time.time())
  token_expired = session.get('token_info').get('expires_at') - now < 60

  # Referesh expired token.
  if (token_expired):
    spotify_oauth = createOauth()
    token_info = spotify_oauth.refresh_access_token(
      session.get('token_info').get('refresh_token')
    )

  token_valid = True
  return token_info, token_valid

def createOauth():
  return SpotifyOAuth(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    redirect_uri=url_for('authorize', _external=True),
    scope="user-library-read"
  )