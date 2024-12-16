import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Digital Clock")
        
        # Create a label to display the time
        self.label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
        self.label.pack(padx=20, pady=20)

        # Start the clock
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")  # Get the current time in HH:MM:SS format
        self.label.config(text=current_time)  # Update the label with the current time
        
        # Animate the label
        self.animate_label()

        # Call this function again after 1 second (1000 milliseconds)
        self.label.after(1000, self.update_time)

    def animate_label(self):
        # Simple animation effect: change the color of the text
        current_color = self.label.cget("fg")
        new_color = "red" if current_color == "blue" else "blue"
        self.label.config(fg=new_color)

# Create the main window
root = tk.Tk()
clock = DigitalClock(root)

# Run the application
root.mainloop()