import pyttsx3
import tkinter as tk

def speak():
    text_to_speak = entry.get()
    friend.say(text_to_speak)
    friend.runAndWait()

def change_rate(value):
    rate = int(value)
    friend.setProperty('rate', rate)
    rate_label.config(text=f"Speech Rate: {rate}")

# Initialize the text-to-speech engine
friend = pyttsx3.init()

# Create the Tkinter window
root = tk.Tk()
root.title("Text-to-Speech")

# Entry widget to input text
entry = tk.Entry(root, width=100)
entry.pack(pady=10)

# Button to trigger speech
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack()

# Slider to change speech rate
rate_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL, label="Speech Rate", command=change_rate)
rate_slider.set(150)  # Set an initial value
rate_slider.pack()

# Label to display current speech rate
rate_label = tk.Label(root, text="Speech Rate: 150")
rate_label.pack()

# Run the Tkinter event loop
root.mainloop()
