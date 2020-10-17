from tkinter import *
from tksheet import Sheet


class Form:
    def __init__(self):
        root.title = "Tugas Besar Sistem Parkir"
        self.title()
        self.search()
        self.plat()
        self.timeIn()
        self.timeOut()
        self.cost()
        self.costPerHour()
        root.columnconfigure(0, pad=3)
        root.columnconfigure(1, pad=3)
        root.columnconfigure(2, pad=3)
        root.columnconfigure(3, pad=3)

        root.rowconfigure(0, pad=3)
        root.rowconfigure(1, pad=3)
        root.rowconfigure(2, pad=3)
        root.rowconfigure(3, pad=3)

    def title(self):
        groupName = Label(root, text="Aplikasi Parkir Kelompok 7", font="ARIAL 18 bold")
        groupName.grid(row=0, column=0, padx=(50, 10), pady=(20, 10))

    def search(self):
        search_txt = Label(root, text="Cari NoPol")
        search_txt.grid(row=1, column=0)

        field_search = Entry(root, width=25, textvariable=var_search)
        field_search.grid(row=1, column=1)

    def plat(self):
        text_plat = Label(root, text="No Plat Polisi")
        text_plat.grid(row=3, column=0)

        field_plat = Entry(root, width=25, textvariable=var_plat)
        field_plat.grid(row=3, column=1)

    def timeIn(self):
        text_in = Label(root, text="Waktu Masuk")
        text_in.grid(row=4, column=0)

        field_in = Entry(root, width=25, textvariable=var_in)
        field_in.grid(row=4, column=1)

    def timeOut(self):
        text_out = Label(root, text="Waktu Keluar")
        text_out.grid(row=5, column=0)

        field_out = Entry(root, width=25, textvariable=var_out)
        field_out.grid(row=5, column=1)

    def cost(self):
        text_cost = Label(root, text="Biaya")
        text_cost.grid(row=6, column=0)

        field_cost = Entry(root, width=25, textvariable=var_cost)
        field_cost.grid(row=6, column=1)

    def costPerHour(self):

        text_info = Label(root, text="Biaya Per Jam", font="Arial 12 bold")
        text_info.grid(row=1, rowspan=2, column=3)

        text_costPerHour = Label(root, text="Rp. 2000", font="ROBOTO 20 bold" ,foreground="RED")
        text_costPerHour.grid(row=2, rowspan=3, column=3)


class TableLastOut():
    def __init__(self):
        text_customer_latest = Label(root, text="List Pelanggan Urut Terakhir Keluar", font="ROBOTO 13")
        text_customer_latest.grid(row=8, column=0, columnspan=2, padx=5 , pady=(80,10))

        self.frame = tableFrameLatest
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(self.frame,
                           page_up_down_select_row=True,
                           # empty_vertical = 0,
                           column_width=120,
                           startup_select=(0, 1, "rows"),
                           # row_height = "4",
                           # default_row_index = "numbers",
                           # default_header = "both",
                           # empty_horizontal = 0,
                           # show_vertical_grid = False,
                           # show_horizontal_grid = False,
                           # auto_resize_default_row_index = False,
                           # header_height = "3",
                           # row_index_width = 100,
                           # align = "e",
                           # header_align = "w",
                           # row_index_align = "w",
                           data=sorted(list_last_out, key=lambda x: x[2], reverse=TRUE),
                           # to set sheet data at startup
                           headers=["No Plat Polisi", "Masuk", "Keluar", "Biaya"],
                           # set_all_heights_and_widths = True, #to fit all cell sizes to text at start up
                           # headers = 0, #to set headers as first row at startup
                           # headers = [f"Column {c}\nnewline1\nnewline2" for c in range(30)],
                           # theme = "light green",
                           # row_index = 0, #to set row_index as first column at startup
                           # total_rows = 2000, #if you want to set empty sheet dimensions at startup
                           # total_columns = 30, #if you want to set empty sheet dimensions at startup
                           height=200,  # height and width arguments are optional
                           width=500  # For full startup arguments see DOCUMENTATION.md
                           )
        # self.sheet.hide("row_index")
        # self.sheet.hide("header")
        # self.sheet.hide("top_left")
        self.sheet.enable_bindings(("single_select",  # "single_select" or "toggle_select"
                                    "drag_select",  # enables shift click selection as well
                                    "column_drag_and_drop",
                                    "row_drag_and_drop",
                                    "column_select",
                                    "row_select",
                                    "column_width_resize",
                                    "double_click_column_resize",
                                    # "row_width_resize",
                                    # "column_height_resize",
                                    "arrowkeys",
                                    "row_height_resize",
                                    "double_click_row_resize",
                                    "right_click_popup_menu",
                                    "rc_select",
                                    "rc_insert_column",
                                    "rc_delete_column",
                                    "rc_insert_row",
                                    "rc_delete_row",
                                    "hide_columns",
                                    "copy",
                                    "cut",
                                    "paste",
                                    "delete",
                                    "undo",
                                    "edit_cell"))
        # self.sheet.disable_bindings() #uses the same strings
        # self.sheet.enable_bindings()

        self.frame.grid(row=9, column=0, columnspan=2, sticky="nswe", padx=5)
        self.sheet.grid(row=9, column=0, columnspan=2, sticky="nswe", padx=5)

    def set_data(self):
        self.sheet.set_sheet_data(sorted(list_last_out, key=lambda x: x[2], reverse=TRUE))


class TableGreatestPayment():
    def __init__(self):
        text_customer_latest = Label(root, text="List Pelanggan Banyak Bayar", font="ROBOTO 13")
        text_customer_latest.grid(row=8, column=2, columnspan=2, padx=5, pady=(80,10))

        self.frame = tableFramePayment
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                           page_up_down_select_row = True,
                           #empty_vertical = 0,
                           column_width = 120,
                           startup_select = (0,1,"rows"),
                           #row_height = "4",
                           #default_row_index = "numbers",
                           #default_header = "both",
                           #empty_horizontal = 0,
                           #show_vertical_grid = False,
                           #show_horizontal_grid = False,
                           #auto_resize_default_row_index = False,
                           #header_height = "3",
                           #row_index_width = 100,
                           #align = "e",
                           #header_align = "w",
                            #row_index_align = "w",
                           data=sorted(list_most_cost, key=lambda x: x[3], reverse=TRUE),
                           # to set sheet data at startup
                           headers=["No Plat Polisi", "Masuk", "Keluar", "Biaya"],
                            #set_all_heights_and_widths = True, #to fit all cell sizes to text at start up
                            #headers = 0, #to set headers as first row at startup
                            #headers = [f"Column {c}\nnewline1\nnewline2" for c in range(30)],
                           #theme = "light green",
                            #row_index = 0, #to set row_index as first column at startup
                            #total_rows = 2000, #if you want to set empty sheet dimensions at startup
                            #total_columns = 30, #if you want to set empty sheet dimensions at startup
                            height = 200, #height and width arguments are optional
                            width = 500 #For full startup arguments see DOCUMENTATION.md
                            )
        #self.sheet.hide("row_index")
        #self.sheet.hide("header")
        #self.sheet.hide("top_left")
        self.sheet.enable_bindings(("single_select", #"single_select" or "toggle_select"
                                         "drag_select",   #enables shift click selection as well
                                         "column_drag_and_drop",
                                         "row_drag_and_drop",
                                         "column_select",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         #"row_width_resize",
                                         #"column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "right_click_popup_menu",
                                         "rc_select",
                                         "rc_insert_column",
                                         "rc_delete_column",
                                         "rc_insert_row",
                                         "rc_delete_row",
                                    "hide_columns",
                                         "copy",
                                         "cut",
                                         "paste",
                                         "delete",
                                         "undo",
                                         "edit_cell"))
        #self.sheet.disable_bindings() #uses the same strings
        #self.sheet.enable_bindings()

        self.frame.grid(row=9, column=2, columnspan=2, sticky="nswe", padx=5)
        self.sheet.grid(row=9, column=2, columnspan=2, sticky="nswe", padx=5)

    def set_data(self):
        self.sheet.set_sheet_data(sorted(list_most_cost, key=lambda x: x[3], reverse=TRUE))


# value submit onclick button
def submit():
    list_last_out.append([
        var_plat.get(),
        var_in.get(),
        var_out.get(),
        var_cost.get()
    ])
    list_most_cost.append([
        var_plat.get(),
        var_in.get(),
        var_out.get(),
        int(var_cost.get())
    ])
    var_plat.set("")
    var_in.set("")
    var_out.set("")
    var_cost.set("")
    TableLastOut().set_data()
    TableGreatestPayment().set_data()


root = Tk()
root.geometry("1100x550")

var_search = StringVar(root)
var_plat = StringVar(root)
var_in = StringVar(root)
var_out = StringVar(root)
var_cost = StringVar(root)


# Array List
list_last_out = [
    ["B 2044 XYZ", "10:05:69", "12:00:20", 10000],
    ["B 1415 ABC", "10:05:69", "14:00:20", 8000],
    ["E 1234 BY", "10:05:69", "13:00:20", 6000]
]
list_most_cost = [
    ["B 2044 XYZ", "10:05:69", "12:00:20", 10000],
    ["B 1415 ABC", "10:05:69", "14:00:20", 8000],
    ["E 1234 BY", "10:05:69", "13:00:20", 6000]
]


# Inisiate FrameLayout
formFrame = Frame(root)
tableFrameLatest = Frame(root)
tableFramePayment = Frame(root)


#Button Search & Submit
search_btn = Button(root, text="Cari")
search_btn.grid(row=1, column=2)

submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=6, column=2)


# Call All Layout
Form()
TableLastOut()
TableGreatestPayment()

mainloop()
