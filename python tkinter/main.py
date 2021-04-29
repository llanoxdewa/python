import tkinter

main_windows = tkinter.Tk()

print(main_windows.__dict__)
main_windows.title('bullshit animation with python')
label1 = tkinter.Label(main_windows, text = 'welcome',width=50)
label2 = tkinter.Label(main_windows, text = 'pilihlah salah satu tombol',width=50)

botton1 = tkinter.Button(main_windows, text = 'yes',width=50)
botton2 = tkinter.Button(main_windows, text = 'no',width=50)
button3 = tkinter.Button(main_windows, text= 'quit',width=50)

label1.pack()
label2.pack()
botton1.pack()
botton2.pack()

main_windows.mainloop()