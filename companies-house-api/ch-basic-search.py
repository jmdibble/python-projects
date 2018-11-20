from tkinter import *
import requests

def search_num():
    url_num = "https://4cQ10i70oDMnmWrJKB6QnHNEgU8enNwgw4zNLegU:@api.companieshouse.gov.uk/company/"
    full_url = (url_num + num_text.get())
    response_company = requests.get(full_url)
    data_co = response_company.json()
    co_name = str(data_co["company_name"])
    e1.delete(0, END)
    e1.insert(0, co_name)

def search_name():
    url_num = "https://4cQ10i70oDMnmWrJKB6QnHNEgU8enNwgw4zNLegU:@api.companieshouse.gov.uk/search/companies?q="
    full_url = (url_num + name_text.get())
    response_numbers = requests.get(full_url)
    data_co = response_numbers.json()
    co_num = str(data_co["items"][0]["company_number"])
    e2.delete(0, END)
    e2.insert(0, co_num)


window = Tk()

window.wm_title("Companies House API Search")

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="Number")
l2.grid(row=1, column=0)

name_text=StringVar()
e1 = Entry(window, textvariable=name_text, width = 50)
e1.grid(row=0, column=1)

num_text=StringVar()
e2 = Entry(window, textvariable=num_text, width = 50)
e2.grid(row=1, column=1)

# ls1 = Listbox(window, width = 50, columnspan=2)
# ls1.grid(row=3, column=0)

b1 = Button(window, text="Search Number", command=search_num)
b1.grid(row=4, column=0)

b2 = Button(window, text="Search Name", command=search_name)
b2.grid(row=4, column=1)


window.mainloop()

