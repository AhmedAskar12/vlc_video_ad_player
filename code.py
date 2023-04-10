import customtkinter
import tkinter as tk
import vlc

# Configuring tkinter frame.
frame = tk.Tk()
frame.configure(bg='#212325')
frame.geometry("700x400")
APP_NAME = "frame"
frame.title(APP_NAME)

VideoFrame = customtkinter.CTkFrame(master=frame, corner_radius=0)
VideoFrame.place(relx=0.005, y=0, relwidth=1, relheight=1)

VFrame = tk.Label(VideoFrame, bg="#2a2d2e")
VFrame.place(relx=0, rely=0, relheight=.9, relwidth=1)

Registratyion = tk.Label(VFrame, text="Add Media", bg="#2a2d2e", fg="gray29", font=("Roboto Medium", -20))
Registratyion.place(relx=0.0, rely=0, relheight=1, relwidth=1)

video_link="https://movmi.co/wp-content/uploads/2022/10/mov_bbb.mp4" # The link of the online hosted video.

PlayButton = customtkinter.CTkButton(master=VideoFrame, text="Play", command=lambda: AdPlayer.play(video_link),
                                     hover_color="#8B4000" ,fg_color="#EE7600",
                                     corner_radius=0)
PlayButton.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

# Ad player class.
class AdPlayer():

    # Creating VLC player

    def play(self,video_link):


        VFrame.instance = vlc.Instance()
        VFrame.player = VFrame.instance.media_player_new()
        # Function to start player from given source
        Media = VFrame.instance.media_new(video_link)
        Media.get_mrl()
        VFrame.player.set_media(Media)
        VFrame.player.set_hwnd(VFrame.winfo_id())
        VFrame.player.play()


# Defining the class.
AdPlayer=AdPlayer()
frame.mainloop()