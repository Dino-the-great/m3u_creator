from tkinter import *
from tkinter import ttk,filedialog,messagebox
from file_create import generate_m3u

origin_window = Tk()
origin_window.title("M3U Generator")
selected_path = StringVar()



def openfiles():
   file_path = filedialog.askopenfilenames(title="Select files")
   selected_path.set(file_path)
   print(selected_path.get())

def opendirectory():
   directory_path = filedialog.askdirectory(title="Select files", initialdir="/", mustexist=True)
   selected_path.set(directory_path)
   print(selected_path.get())

def confirmrun(selected_path):
   if len(selected_path.get()) == 0:
      messagebox.showinfo("No path selected")
      return
   result = messagebox.askyesno("Confirm", "Generate m3u files for this folder?")
   if result:
      log = generate_m3u(selected_path.get())
      messagebox.showinfo("Run Log", log)
   else:
      pass



main_window = ttk.Frame(origin_window, padding=(12,12,12,12))
main_window.grid(column=0, row=0, sticky=(N, W, E, S))

picker_label =  ttk.Label(main_window, text="Please pick a directory or group of files:")
picker_label.grid(column=0,row=0)


file_label = ttk.Label(main_window, text="Please Select a Files")
file_label.grid(column=0,row=1)
file_button = ttk.Button(main_window, text="Select File", command=openfiles)
file_button.grid(column=1,row=1)


directory_label = ttk.Label(main_window, text="Please Select a Folder")
directory_label.grid(column=0,row=2)
directory_button = ttk.Button(main_window, text="Select Folder", command=opendirectory)
directory_button.grid(column=1,row=2)


select_path_label = ttk.Label(main_window, text="Your chosen file/directory:")
select_path_label.grid(column=0,row=3)
path_label = ttk.Label(main_window, textvariable=selected_path)
path_label.grid(column=1,row=3)

run_button = ttk.Button(main_window, text="Run", command=lambda: confirmrun(selected_path))
run_button.grid(column=0,row=4)


origin_window.mainloop()