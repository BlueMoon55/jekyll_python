import tkinter as tk

root = tk.Tk()                    # メインウィンドウを作成
root.geometry('100x100')          # ウィンドウのサイズを設定
button1 = tk.Button(
    root, text='ボタン1').pack()  # ボタンを配置

button2 = tk.Button(
    root, text='ボタン2').pack()  # ボタンを配置

button3 = tk.Button(
    root, text='ボタン3').pack()  # ボタンを配置

root.mainloop()
