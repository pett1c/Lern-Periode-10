import tkinter as tk
from gui import MusicRecommenderGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Music Recommender")
    app = MusicRecommenderGUI(root)
    root.mainloop()