import requests
import json
from tkinter import *


def generate():
  response = requests.get("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
    headers={
      "X-Mashape-Key": "qhvD1xyT6WmshzMIiIRXF9IeWENfp1lCjGXjsnVLFJ7CjONvKE",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json"
    }
  )

  data = response.json()

  for i in data:
      global quote
      global author
      quote = (i["quote"])
      author = (i["author"])
      print(quote)
      print(author)


generate()


# window = Tk()
#
# b1 = Button(window, text = "Generate Quote!", command=generate)
# b1.grid(row=2, column = 1)
#
# l1 = Label(window, text="Quote")
# l1.grid(row=0, column=0)
#
# l2 = Label(window, text="Author")
# l2.grid(row=0, column=1)
#
# e1_value = StringVar()
# e1 = Entry(window, textvariable=quote)
# e1.grid(row=1, column=0)
#
# e2_value = StringVar()
# e2 = Entry(window, textvariable=author)
# e2.grid(row=1, column=1)
#
#
# window.mainloop()