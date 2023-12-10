from gtts import gTTS
import pygame
import tempfile
import os
import tkinter as tk
def speak_bangla():
    text_to_speak = entry.get()

    # Create a temporary file to save the generated audio
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_filename = temp_file.name + ".mp3"

    # Generate Bangla text-to-speech
    tts = gTTS(text=text_to_speak, lang='bn')
    tts.save(temp_filename)

    # Play the generated audio
    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up temporary file
    os.remove(temp_filename)

# Create the Tkinter window
root = tk.Tk()
root.title("Bangla Text-to-Speech")

# Entry widget to input Bangla text
entry = tk.Entry(root, width=100)
entry.pack(pady=10)

# Button to trigger Bangla text-to-speech
speak_button = tk.Button(root, text="Speak Bangla", command=speak_bangla)
speak_button.pack()

# Run the Tkinter event loop
root.mainloop()
