import tkinter as tk
from tkinter import font
import os
from PIL import Image, ImageTk
import cairosvg
import io
from model.model import get_recommendations, update_track_rating

# colors and parameters
theme_bg = '#18161C'
theme_fg = '#fff'
theme_accent = '#7eeaff'
emoji_size = 48

# moods and icons
MOODS = [
    ('joy', '😃'),
    ('sadness', '😭'),
    ('surprise', '🥳'),
    ('anger', '🤬'),
    ('fear', '😱'),
    ('love', '💗'),
]
MOOD_SVG = {
    'joy': 'joy.svg',
    'sadness': 'sadness.svg',
    'surprise': 'surprise.svg',
    'anger': 'anger.svg',
    'fear': 'fear.svg',
    'love': 'love.svg',
}
FIRE_SVG = 'fire.svg'
POOP_SVG = 'poop.svg'

class MMmoodApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MMmood')
        self.resizable(False, False)
        self.configure(bg=theme_bg)
        self.protocol('WM_DELETE_WINDOW', self.destroy)
        self.minsize(400, 400)
        self.selected_mood = None
        self.recommendations = []
        self._svg_images = {}  # cache for PhotoImage
        self.content = tk.Frame(self, bg=theme_bg)
        self.content.pack(expand=True, fill='both')
        self.draw_main_screen()
        self.update_idletasks()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws // 2) - (w // 2)
        y = (hs // 2) - (h // 2)
        self.geometry(f'{w}x{h}+{x}+{y}')

    def get_svg_image(self, svg_path, size=32):
        key = (svg_path, size)
        if key in self._svg_images:
            return self._svg_images[key]
        if not svg_path or not os.path.exists(svg_path):
            return None
        try:
            png_bytes = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
            image = Image.open(io.BytesIO(png_bytes)).convert('RGBA')
            photo = ImageTk.PhotoImage(image)
            self._svg_images[key] = photo
            return photo
        except Exception as e:
            print(f'Error loading {svg_path}: {e}')
            return None

    def draw_main_screen(self):
        # draw the main mood selection screen
        for widget in self.content.winfo_children():
            widget.destroy()
        title_frame = tk.Frame(self.content, bg=theme_bg)
        title_frame.pack(pady=(30, 5))
        tk.Label(title_frame, text='MMMood', font=('Consolas', 32, 'bold'), fg=theme_fg, bg=theme_bg).pack()
        tk.Label(self.content, text='choose your mood today:', font=('Consolas', 11), fg=theme_fg, bg=theme_bg).pack(pady=(0, 20))
        grid_frame = tk.Frame(self.content, bg=theme_bg)
        grid_frame.pack()
        for i, (mood, emoji) in enumerate(MOODS):
            row, col = divmod(i, 3)
            f = tk.Frame(grid_frame, bg=theme_bg)
            f.grid(row=row, column=col, padx=30, pady=15)
            svg_img = self.get_svg_image(MOOD_SVG[mood], size=64)
            if svg_img:
                btn = tk.Button(f, image=svg_img, bg=theme_bg, bd=0, activebackground=theme_bg, command=lambda m=mood: self.show_recommendations(m), highlightthickness=0)
                btn.image = svg_img
            else:
                btn = tk.Button(f, text=mood, font=('Consolas', 18), bg=theme_bg, fg=theme_fg, bd=0, activebackground=theme_bg, command=lambda m=mood: self.show_recommendations(m), highlightthickness=0)
            btn.pack()
            tk.Label(f, text=mood, font=('Consolas', 11), fg=theme_fg, bg=theme_bg).pack()
        self.update_idletasks()
        self.center_window()

    def show_recommendations(self, mood):
        # show recommendations for the selected mood
        self.selected_mood = mood
        self.recommendations = get_recommendations(mood)
        self.draw_recommendations_screen()

    def draw_recommendations_screen(self):
        # draw the recommendations screen
        for widget in self.content.winfo_children():
            widget.destroy()
        title_frame = tk.Frame(self.content, bg=theme_bg)
        title_frame.pack(pady=(30, 5))
        tk.Label(title_frame, text='MMMood', font=('Consolas', 32, 'bold'), fg=theme_fg, bg=theme_bg).pack()
        tk.Label(self.content, text='recommended you:', font=('Consolas', 11), fg=theme_fg, bg=theme_bg).pack(pady=(0, 20))
        grid_frame = tk.Frame(self.content, bg=theme_bg)
        grid_frame.pack()
        for i, track in enumerate(self.recommendations[:4]):
            row, col = divmod(i, 2)
            f = tk.Frame(grid_frame, bg=theme_bg)
            f.grid(row=row, column=col, padx=60, pady=10, sticky='nsew')
            tk.Label(f, text=track.get('title', 'TRACK'), font=('Consolas', 15, 'bold'), fg=theme_fg, bg=theme_bg).pack()
            tk.Label(f, text=track.get('artist', 'Artist'), font=('Consolas', 11), fg=theme_fg, bg=theme_bg).pack()
            icons_frame = tk.Frame(f, bg=theme_bg)
            icons_frame.pack(pady=(5, 0))
            fire_img = self.get_svg_image(FIRE_SVG, size=24)
            poop_img = self.get_svg_image(POOP_SVG, size=24)
            if fire_img:
                fire_btn = tk.Button(icons_frame, image=fire_img, bg=theme_bg, bd=0, activebackground=theme_bg, command=lambda t=track: self.rate_track(t, 'yes'))
                fire_btn.image = fire_img
            else:
                fire_btn = tk.Button(icons_frame, text='fire', font=('Consolas', 12), bg=theme_bg, fg=theme_fg, bd=0, activebackground=theme_bg, command=lambda t=track: self.rate_track(t, 'yes'))
            fire_btn.pack(side='left', padx=2)
            if poop_img:
                poop_btn = tk.Button(icons_frame, image=poop_img, bg=theme_bg, bd=0, activebackground=theme_bg, command=lambda t=track: self.rate_track(t, 'no'))
                poop_btn.image = poop_img
            else:
                poop_btn = tk.Button(icons_frame, text='poop', font=('Consolas', 12), bg=theme_bg, fg=theme_fg, bd=0, activebackground=theme_bg, command=lambda t=track: self.rate_track(t, 'no'))
            poop_btn.pack(side='left', padx=2)
            tk.Label(f, text=track.get('genre', 'genre'), font=('Consolas', 10), fg=theme_fg, bg=theme_bg).pack(pady=(2, 0))
        for i in range(2):
            grid_frame.grid_columnconfigure(i, weight=1)
        for i in range(2):
            grid_frame.grid_rowconfigure(i, weight=1)
        refresh_btn = tk.Button(self.content, text='Refresh', font=('Consolas', 12), fg=theme_fg, bg=theme_bg, bd=1, highlightbackground=theme_fg, command=self.refresh_recommendations)
        refresh_btn.pack(pady=(20, 5))
        tk.Label(self.content, text='...or choose new mood', font=('Consolas', 10), fg=theme_fg, bg=theme_bg).pack(pady=(0, 10))
        choose_btn = tk.Button(self.content, text='←', font=('Consolas', 12), fg=theme_fg, bg=theme_bg, bd=0, command=self.draw_main_screen)
        choose_btn.pack()
        self.update_idletasks()
        self.center_window()

    def refresh_recommendations(self):
        # refresh recommendations for the selected mood
        if self.selected_mood:
            self.recommendations = get_recommendations(self.selected_mood)
            self.draw_recommendations_screen()

    def rate_track(self, track, rating):
        # update user_rating for a track and print info
        update_track_rating(track['_id'], rating)
        print(f"user_rating for track '{track.get('title', 'TRACK')}' changed to '{rating}'")

if __name__ == '__main__':
    app = MMmoodApp()
    app.mainloop()