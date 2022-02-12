import  tkinter as tk
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
root=tk.Tk()

canvas=tk.Canvas(root, height=700, width=800)
canvas.pack()

bi=tk.PhotoImage(file='suresync-suite-background.png')
bl=tk.Label(root, image=bi)
bl.place(relheight=1, relwidth=1)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0, rely=0, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0.8, rely=0, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.2)

pathtophoto = Image.open("tes.png")
image1 = ImageTk.PhotoImage(pathtophoto)
panel1 = tk.Label(root, image=image1)
panel1.image = image1 #keep a reference
panel1.place(relx=0.8, rely=0.8, relheight=0.2, relwidth=0.2)





def Run():
    button_text.set("Select-Data")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    x="Program Ran Successfully \nAll Charts Loaded \nThank You."
    button_text.set("Charts_Loading........")
    import Preprocessing_module
    import Visualization_module
    Preprocessing_module.data_preprocessing(filename)
    newCasesBySpecimenDate=Preprocessing_module.newCasesBySpecimenDate_df
    df_age_groups=Preprocessing_module.age_groups_df
    df_cum_cases=Preprocessing_module.cum_cases_df
    cum_cases_sum=Preprocessing_module.cum_cases_sum
    Visualization_module.plot_charts_by_newCasesBySpecimenDate(newCasesBySpecimenDate)
    Visualization_module.plot_charts_by_age_groups(df_age_groups)
    Visualization_module.plot_charts_by_rollingrates(df_cum_cases)
    Visualization_module.plot_charts_by_rollingsum(cum_cases_sum)
    button_text.set("Run") 
    
    text_box=tk.Text(frame, height=1, width=10, padx=15, pady=15 )
    text_box.insert(1.0, x)
    text_box.place(relx=0.1, rely=0.7, relheight=0.3, relwidth=0.8)

frame=tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.25, rely=0.25, relheight=0.5, relwidth=0.5)

Label=tk.Label(frame, text="This Software takes in the Data_set and Return Charts. \n \n Click the Run button below to select the Dataset and \
await the Charts; Charts will open in a new window.\n \n ENSURE TO CLOSE EACH CHART TO OPEN THE NEXT", bg='gray')
Label.place(relx=0.1, rely=0.3, relheight=0.2, relwidth=0.8)

button_text=tk.StringVar()
button=tk.Button(frame, textvariable=button_text, bg='gray', command=lambda: Run())
button_text.set("Run")
button.place(relx=0.4, rely=0.55, relheight=0.1, relwidth=0.2)

root.mainloop()
