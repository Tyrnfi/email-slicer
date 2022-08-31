from tkinter import tkinter as tk
window = tk.Tk()
window.geometry("480x440")
window.config(bg="#BE361A")
window.resizable(width=False,height=False)
window.title('Simple Email Slicer')

greeting = tk.Label(text="Welcome to A Simple Email Slicer!",font=(12),foreground="white",background="black")
Info = tk. Label(text="Enter your email id click the done button!\n The application will extract your username and domain name.",foreground= "white",background="#BE361A",font=(10))
entry_label = tk.Label(foreground= "white",font=(10),background="black",text="Enter Your Email Id: ") 
result_label =tk.Label(font=(10),foreground= "white",background="black",text="The results are as follows:")
empty_label0=tk.Label(background="#BE361A")
empty_label1=tk.Label(background="#BE361A")
empty_label2=tk.Label(background="#BE361A")
empty_label3=tk.Label(background="#BE361A")
empty_label4=tk.Label(background="#BE361A")
empty_label5=tk.Label(background="#BE361A")
 
#The Entry box
entry = tk.Entry(font=(11),width=50,justify='center')
 
#The two Buttons
button = tk.Button(text="Done!",font=(11))
reset=tk.Button(text="Reset!",font=(11))
 
#Result
text_box = tk.Text(height=5,width=50)
 
#Packing Everything Together
empty_label0.pack()
greeting.pack()
Info.pack()
empty_label1.pack()
entry_label.pack()
empty_label4.pack()
entry.pack()
empty_label2.pack()
button.pack()
empty_label5.pack()
reset.pack()
empty_label3.pack()
result_label.pack()


 
window.mainloop()

