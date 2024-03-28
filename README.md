
# Voice-Controlled Spotify Application

This Python project allows you to control the Spotify application on your laptop using voice commands. You can play, pause, and resume songs in Spotify simply by speaking into your microphone.

## Functionality

### Implemented Actions

- **Play**: Plays a song in the Spotify application.
- **Pause**: Pauses the currently playing song in Spotify.
- **Resume**: Resumes playback of the paused song in Spotify.

### How It Works

The project consists of a Python script that captures voice commands, recognizes the desired action (e.g., play, pause), and invokes the corresponding functionality to control Spotify.

## Modules Implemented

### Spotify Module (`actions/spotify.py`)

This module contains functions to interact with the Spotify application:

- `play()`: Plays a song in Spotify.
- `pause()`: Pauses the currently playing song.
- `resume()`: Resumes playback of the paused song.

## How to Run

1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd voice-controlled-spotify
   ```

2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```
   python main.py
   ```

4. **Provide Voice Commands**:
   Speak into your microphone and issue commands like "open Spotify and play the song," "pause the song," or "resume playback."

## Requirements

- Python 3.x
- SpeechRecognition
- pyaudio
- pyautogui
- spotipy
- pygame

## Note

- Make sure your microphone is properly configured and connected to your laptop.
- Spotify application must be installed and running on your laptop for the commands to work.
- Adjustments to microphone sensitivity or audio settings may be necessary for optimal performance.
