import requests
import json
import tkinter as tk
from tkinter import END
from threading import Thread

#QQ查手机绑定
def url_QQ():
    global qqSearch,text_pad
    qq = int(qqSearch.get())
    url_QQ = "https://api.xywlapi.cc/qqapi"
    param_QQ = {"qq":qq}    #参数输入
    resQQ = requests.get(url=url_QQ,params=param_QQ)
    status = resQQ.json()["status"]
    if status == 200:
        phoneOut = resQQ.json()["phone"]
        locat = resQQ.json()["phonediqu"]
        text_pad.insert(END,f"手机绑查询结果如下:\n手机号为:{phoneOut},手机号地区:{locat}\n\n")
    else:
        text_pad.insert(END,"查询失败\n")



#手机号查QQ
def url_Phone():
    global phoneSearch,text_pad
    phone = int(phoneSearch.get())
    url_Phone = "https://api.xywlapi.cc/qqphone"
    param_Phone = {"phone":phone}   #参数输入
    resPhone = requests.get(url=url_Phone,params=param_Phone)
    status = resPhone.json()["status"]
    if status == 200:
        qqOut = resPhone.json()["qq"]
        location = resPhone.json()["phonediqu"]
        text_pad.insert(END, f"Q绑查询结果如下:\nQQ号为:{qqOut},手机号地区:{location}\n\n")
    else:
        text_pad.insert(END, "查询失败\n")

def qq_thread():
    s = Thread(target=url_QQ)
    s.start()

def phone_thread():
    s = Thread(target=url_Phone)
    s.start()

windows = tk.Tk()
windows.title("作者:DEM0NS.本工具仅做测试使用，禁止用于违法行为")
windows.geometry('600x400')
windows.iconbitmap('.\\image\\test.ico')

'''
左边布局
'''
left_frame = tk.Frame(windows)
left_frame.pack(side=tk.LEFT,anchor=tk.N,padx=5,pady=5)

qq_frame = tk.LabelFrame(left_frame,text='QQ与手机互查',padx=5,pady=5)
qq_frame.pack()
#QQ查询
qqSearch = tk.StringVar(master=qq_frame)
tk.Label(qq_frame,text='输入QQ:(请勿多次点击)').pack(anchor=tk.W)
entry_qq = tk.Entry(qq_frame,textvariable=qqSearch)
entry_qq.pack(fill=tk.X)
buttonQqFrame = tk.Frame(qq_frame)
buttonQqFrame.pack()

searchButton = tk.Button(buttonQqFrame,text='查询',command=qq_thread)
searchButton.pack(side=tk.LEFT)

#手机查询
phoneSearch = tk.StringVar(master=qq_frame)
tk.Label(qq_frame,text="输入手机号：(请勿多次点击)").pack(anchor=tk.W)
entry_phone = tk.Entry(qq_frame,textvariable=phoneSearch)
entry_phone.pack(fill=tk.X)
buttonPhone = tk.Frame(qq_frame)
buttonPhone.pack()

searchButtonPhone = tk.Button(buttonPhone,text='查询',command=phone_thread)
searchButtonPhone.pack(side=tk.LEFT)



'''右边布局'''
right_frame = tk.Frame()
right_frame.pack(side=tk.LEFT,padx=5,pady=5,anchor=tk.N)

info_frame = tk.Frame(right_frame)
info_frame.pack()
tk.Label(info_frame,text="查询结果").pack(anchor=tk.W)

#文本框
text_pad = tk.Text(info_frame,width=50)
text_pad.pack(side=tk.LEFT,fill=tk.X)


#滚动条
send_textBar = tk.Scrollbar(info_frame)
send_textBar.pack(side=tk.RIGHT,fill=tk.Y)

windows.mainloop()


























