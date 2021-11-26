import os
import time
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.ttk import Progressbar

import self as self
from mutagen.mp3 import MP3
from ttkthemes import ThemedStyle
import tk as tk
from PIL import Image, ImageTk
from pygame import mixer

mixer.init()
playing = False
paused=False
mute=False
play_thread=None
to_break=False
songs=[]
top=Tk()
top.title("Music Player")
top.geometry("795x495")
style=ttk.Style()

style.configure("grey.Horizontal.TProgressbar",background="blue")
current_time=0

#defining count
def start_count(t):
    global current_time

    while current_time<=t and mixer.music.get_busy():
        global paused
        global dur_start
        global progress_bar
        global to_break
        if paused:
            continue
        elif to_break:
            break
        else :
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            dur_start['text'] = timeformat
            time.sleep(1)
            current_time+=1
            progress_bar['value'] = current_time
            progress_bar.update()
            #if current_time + 0.04 >= length:
            #    nextSong()

    if ((current_time)/60)+0.07>=t/60:
        #if isrep == False:
        nextSong()

 #   if to_break:
 #       current_time=0

 #       to_break=False
 #       return
 #   else :
 #       try:
 #           nextSong()
 #       except:
 #           pass

#function for exit button
def exit():
    top.destroy()

def music(event):
    global file
    global current_time
    current_time=0
    w=event.widget
    idx=int(w.curselection()[0])
    file=w.get(idx)
    global playing
    global paused
    global progress_bar
    playing = False
    if playing==False:
        global length

       # file = play_List.get(cs)
        animation(count)
        mixer.music.load(file)
        mixer.music.play()
        playing=True
        status_bar['text'] = 'Playing - ' + file

        play_button.config(image=pause_img)
        song = MP3(file)
        length = song.info.length
        p=(float)(length/60)
        mins, secs = divmod(length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        dur_end['text'] = timeformat
        progress_bar['maximum'] =p*60
        progress_bar.update()
        start_count(length)
    else:
        if paused==True:
            mixer.music.unpause()
            paused=False
            animation(count)
            status_bar['text'] = 'Playing - ' + file
            play_button['image'] = pause_img
            start_count(length)


        else :
            mixer.music.pause()
            paused = True
            stop_animation()
            play_button.config(image=play_image)
            status_bar['text'] = 'Music Paused'


#gif
file=r"D:\Desktop\python project images\gif8.gif"

info=Image.open(file)
frames=info.n_frames
im=[PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]
anim=None
count=0
def animation(count):
    global anim
    im2=im[count]
    gif_label.configure(image=im2)
    count+=1
    if count==frames:
        count=0
    anim=top.after(50,lambda:animation(count))

def stop_animation():
    top.after_cancel(anim)

#function for about button in media
def about():
    messagebox.showinfo("About", "This is an exclusive desktop music player.\n This application has built by group of 3 enthusiast .\n Hope so you will enjoy this player .\n Thank you for using this...")

#Function for open a file
def open_file():
    music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
    dir_ = filedialog.askdirectory(initialdir='D:/', title='Select Directory')
    os.chdir(dir_)
    status_bar['text'] = 'Playlist Updated.'
    dir_files = os.listdir(dir_)

    songs = []
    for file in dir_files:
        extent = file.split('.')[-1]
        for ex in music_ex:
            if ex == extent:
                play_List.insert(END, file)
                songs.append(file)
menubar=Menu(top)
file = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Media",menu=file)
file.add_command(label="Open",command=open_file)
file.add_separator()
file.add_command(label="About",command=about)
menubar.add_cascade(label="exit",command=exit)
Label(top, text='', bg='White', height=19, width=35, relief_='ridge').place(x=543, y=0)


#defining playlist
def set_playlist():
    music_ex = ['mp3', 'wav', 'mpeg', 'm4a', 'wma', 'ogg']
    dir_ = filedialog.askdirectory(initialdir='D:/', title='Select Directory')
    os.chdir(dir_)
    status_bar['text'] = 'Playlist Updated.'
    dir_files=os.listdir(dir_)
    play_List.delete(0, 'end')
    songs=[]
    for file in dir_files:
        extent=file.split('.')[-1]
        for ex in music_ex:
            if ex==extent:
                play_List.insert(END,file)
                songs.append(file)


Button(top, text='Add a Folder.', command=set_playlist, bd=2, font=('arialblack', 13), width=25).place(
    x=552, y=10)
play_List=Listbox(top,height=22,width=41)
play_List.bind('<<ListboxSelect>>',music)
play_List.place(x=544, y=50)


def on_enter_play(event):
    play_des.place(x=25, y=460)

def on_leave_play(event):
    play_des.place(x=1000, y=1000)

def on_enter_prev(event):
    prevsong.place(x=30, y=420)

def on_leave_prev(event):
    prevsong.place(x=1000, y=1000)

def on_enter_stop(event):
    stop.place(x=110, y=465)

def on_leave_stop(event):
    stop.place(x=1000, y=1000)

def on_enter_next(event):
    nextsong.place(x=130, y=420)

def on_leave_next(event):
    nextsong.place(x=1000, y=1000)

def on_enter_vol(event):
    speaker.place(x=195, y=445)

def on_leave_vol(event):
    speaker.place(x=1000, y=1000)

def on_enter_rep(event):
    mb.place(x=610, y=420)

def on_leave_rep(event):
    mb.place(x=1000, y=1000)

def on_enter_for(event):
    mf.place(x=685, y=455)

def on_leave_for(event):
    mf.place(x=1000, y=1000)

# define music function
def play_music():
    global playing
    global paused
    global progress_bar
    #global length

    if playing==False:
        global file
        global length
        global isrep
        file = play_List.get(ACTIVE)
        animation(count)
        mixer.music.load(file)
        mixer.music.play()
        playing=True
        isrep=False
        status_bar['text'] = 'Playing - ' + file

        play_button.config(image=pause_img)
        song = MP3(file)
        length = song.info.length
        p=(float)(length/60)
        mins, secs = divmod(length, 60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        dur_end['text'] = timeformat
        progress_bar['maximum'] =p*60
        progress_bar.update()
        start_count(length)
        print(length)
        print(current_time)

    else:
        if paused==True:
            mixer.music.unpause()
            paused=False
            animation(count)
            status_bar['text'] = 'Playing - ' + file
            play_button['image'] = pause_img
            start_count(length)


        else :
            mixer.music.pause()
            paused = True
            play_button.config(image=play_image)
            stop_animation()
            status_bar['text'] = 'Music Paused'

def nextSong():
    global playing
    global file
    global current_time
    current_time=0
    progress_bar['value'] = current_time
    progress_bar.update()
    index = play_List.index(ACTIVE)
    play_List.activate(index+1)
    file=play_List.get(ACTIVE)
    mixer.music.load(file)
    mixer.music.play()
    status_bar['text'] = 'Playing - ' + file
    play_button['image'] = pause_img
    playing = True
    song = MP3(file)
    length = song.info.length
    mins, secs = divmod(length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    dur_end['text'] = timeformat
    start_count(length)


def prevSong():
    global playing
    global file
    global current_time
    current_time = 0
    progress_bar['value'] = current_time
    progress_bar.update()
    index = play_List.index(ACTIVE)
    play_List.activate(index - 1)
    file = play_List.get(ACTIVE)
    mixer.music.load(file)
    mixer.music.play()
    status_bar['text'] = 'Playing - ' + file
    play_button['image'] = pause_img
    playing = True
    song = MP3(file)
    length = song.info.length
    mins, secs = divmod(length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    dur_end['text'] = timeformat
    start_count(length)





#stop function
def stop():
    mixer.music.stop()
    global playing
    global paused
    global dur_start
    global progress_bar
    global current_time
    global to_break
    to_break = True
    current_time = 0
    cur_playing = ''
    playing = False
    paused = False
    dur_start['text'] = '--:--'
    dur_end['text'] = '--:--'
    progress_bar['value'] = 0.0
    progress_bar.update()

    play_button['image'] = play_image
    status_bar['text'] = 'Music Stopped'
    to_break = False
    stop_animation()


def repeat():
    global isrep
    global  current_time
    isrep = True
    #current_time=0
    #mixer.music.play(-1)

backimg=ImageTk.PhotoImage(Image.open(r"D:\Desktop\python project images\bg2.jpg"))
#Paned Window
gif_label=Label(top,bg="black",image=backimg,bd=0)
gif_label.place(x=10,y=18)
#play button
global pause_img
global play_image
pause_img = ImageTk.PhotoImage(Image.open(r"D:\Desktop\python project images\pause.png"))
play_image=ImageTk.PhotoImage(Image.open(r'D:\Desktop\python project images\play.png'))
Label(top, text='', height=5, relief_='groove', width=200).place(x=0, y=395)
play_button = Button(top, image=play_image, bd=0,command=play_music)
play_button.place(x=10, y=440)
play_button.bind('<Enter>', on_enter_play)
play_button.bind('<Leave>', on_leave_play)
#prev button
prev_img=PhotoImage(file=r'D:\Desktop\python project images\prev.png')
prev_button = Button(top,command=prevSong, image=prev_img, bd=0)
prev_button.place(x=50, y=433)
prev_button.bind('<Enter>', on_enter_prev)
prev_button.bind('<Leave>', on_leave_prev)

#stop_button
stop_img=PhotoImage(file=r'D:\Desktop\python project images\stop.png')
stop_button=Button(top,image=stop_img,bd=0,command=stop)
stop_button.place(x=90,y=437)
stop_button.bind('<Enter>', on_enter_stop)
stop_button.bind('<Leave>', on_leave_stop)
#next_button
next_img=PhotoImage(file=r'D:\Desktop\python project images\next.png')
next_button=Button(top,command=nextSong,image=next_img,bd=0)
next_button.place(x=120,y=433)
next_button.bind('<Enter>', on_enter_next)
next_button.bind('<Leave>', on_leave_next)

#move backward
def Backward():
    global current_time

    if current_time>0 and current_time < length:
        current_time=current_time-10
        mixer.music.set_pos(current_time)
    else:
        prevSong()

#move forward
def Forward():
    global current_time
    if(current_time<length):
        current_time=current_time+10
        mixer.music.set_pos(current_time)
    else:
        nextSong()


#Speaker Function
def speak_func():
    global  mute
    if mute==False:
        mixer.music.set_volume(0.0)
        vol_button['image'] = mute_img
        mute=True
    else :
        mixer.music.set_volume(50.0)
        mute=False
        vol_button['image']=vol_img


def set_vol(num):
    global mute
    global status_bar
    global scale
    if num == float(0):
        vol_button['image'] = mute_img
        mixer.music.set_volume(0.0)
        mute = True
    elif mute == True:
        vol_button['image'] = vol_img
        num = scale.get()
        mixer.music.set_volume(float(num) / 100)
        mute = False
    else:
        volume = float(num) / 100
        mixer.music.set_volume(volume)

#volume button
global mute_img
global vol_img
mute_img=PhotoImage(file=r"D:\Desktop\python project images\mute.png")
vol_img=PhotoImage(file=r'D:\Desktop\python project images\vol.png')
vol_button=Button(top,image=vol_img,bd=0,command=speak_func)
vol_button.bind('<Enter>', on_enter_vol)
vol_button.bind('<Leave>', on_leave_vol)
vol_button.place(x=180,y=442)
# scale
scale=Scale(top,command=set_vol,from_=0 ,to=100,orient=HORIZONTAL,bd=0,width=8,	relief=GROOVE,troughcolor='orange',activebackground='blue',length=100)
scale.set(70)
mixer.music.set_volume(0.7)
scale.place(x=210,y=428)


#shufffle button
#shuffle_img=PhotoImage(file=r'D:\Desktop\python project images\shuffle.png')
#shuffle_button=Button(top,image=shuffle_img,bd=0)
#shuffle_button.place(x=600,y=440)

#Repeat button
repeat_img=PhotoImage(file=r"D:\Desktop\python project images\repeat.png")
repeat_button=Button(top,command=Backward,text='MB',bd=0)
repeat_button.place(x=635,y=440)
repeat_button.bind('<Enter>', on_enter_rep)
repeat_button.bind('<Leave>', on_leave_rep)
#Repeat button
repone_img=PhotoImage(file=r"D:\Desktop\python project images\rep_one.png")
repone_button=Button(top,command=Forward,text='MF',bd=0)
repone_button.place(x=665,y=440)
repone_button.bind('<Enter>', on_enter_for)
repone_button.bind('<Leave>', on_leave_for)
#duration
dur_start = Label(top, text='00:00', font=('Calibri', 10, 'bold'))
dur_start.place(x=5, y=400)
dur_end = Label(top, text='--:--', font=('Calibri', 10, 'bold'))
dur_end.place(x=750, y=400)

#progress_bar
progress_bar = ttk.Progressbar(top, orient='horizontal', length=705,style='grey.Horizontal.TProgressbar')
progress_bar.place(x=42, y=400)

#status bar
status_bar = Label(top, text='Welcome to Flash Player', relief_='groove', anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

#des labels
play_des = Label(top, text='Play/Pause', relief='groove')
nextsong= Label(top,text='Next Song',relief='groove')
prevsong= Label(top,text='Next Song',relief='groove')
stop=Label(top,text='Stop',relief='groove')
speaker=Label(top,text='speaker',relief='groove')
mb=Label(top,text='backward 10s',relief='groove')
mf=Label(top,text='forward 10s',relief='groove')

top.config(menu=menubar,background='black')
top.resizable(0,0)
top.mainloop()
