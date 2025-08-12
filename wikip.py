import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import webbrowser
from tkinter import messagebox


win = tk.Tk()
win.geometry("600x650")
win.title("Wikipedia")
win.iconbitmap("wiki.ico")
win.resizable(False, False)

def open_url(url):
    if url:
        webbrowser.open(url)

def open(e):
    global full_url
    open_url(full_url)

def submit():
    global full_url,e1
    if e1.get().strip() == "":
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    detail = tk.Toplevel(win)
    detail.title(e1.get())
    detail.geometry("600x600")
    detail.config(bg="#D0D1D1")
    detail.resizable(False, False)

    e = e1.get()
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        'action': 'query',
        'list': 'search',
        'srsearch': e,
        'format': 'json',
        'utf8': 1,
        'srlimit': 1
    }
    search_resp = requests.get(search_url, params=search_params).json()
    search_results = search_resp.get('query', {}).get('search', [])
    title = search_results[0]['title']

    l1 = tk.Label(detail, text=title, font=("Helvetica", 24, 'bold'), cursor="hand2", bg="#D0D1D1", fg="#080808")
    l1.pack(pady=(20, 15))
    l1.bind("<Button-1>", open)

    page_url = "https://en.wikipedia.org/w/api.php"
    page_params = {
        'action': 'query',
        'titles': title,
        'prop': 'pageimages|extracts|info',
        'exintro': True,
        'explaintext': True,
        'inprop': 'url',
        'format': 'json',
        'pithumbsize': 300
    }
    page_resp = requests.get(page_url, params=page_params).json()
    pages = page_resp['query']['pages']
    page = next(iter(pages.values()))
    summary = page.get('extract', 'No summary available.')
    thumbnail = page.get('thumbnail', {}).get('source', None)
    full_url = page.get('fullurl', None)

    content_frame = tk.Frame(detail, bg="#D0D1D1")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    img_frame = tk.Frame(content_frame, width=310, height=310, bg="white", relief=tk.RAISED, borderwidth=2)
    img_frame.pack(side=tk.TOP, pady=10, anchor='center')

    label_image = tk.Label(img_frame, bg="white")

    if thumbnail:
        try:
            img_data = requests.get(thumbnail).content
            img = Image.open(BytesIO(img_data)).resize((300, 300))
            photo = ImageTk.PhotoImage(img)
            label_image.config(image=photo)
            label_image.image = photo
        except Exception:
            label_image.config(text="Image\nnot\navailable", font=("Segoe UI", 14), fg="gray")
    else:
        label_image.config(text="No Image", font=("Segoe UI", 14), fg="gray")
    label_image.place(x=2, y=2, width=300, height=300)

    text_frame = tk.Frame(content_frame, bg="white")
    text_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

    text_summary = tk.Text(text_frame, wrap=tk.WORD, font=("Segoe UI", 12), relief=tk.FLAT, bg="white")
    text_summary.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
    text_summary.insert(tk.END, summary)
    text_summary.config(state=tk.DISABLED)

    scrollbar = tk.Scrollbar(text_frame, command=text_summary.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_summary.config(yscrollcommand=scrollbar.set)
    e1.delete(0, tk.END)
def submit1(e):
    global full_url,e1
    if e1.get().strip() == "":
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    detail = tk.Toplevel(win)
    detail.title(e1.get())
    detail.geometry("600x600")
    detail.config(bg="#D0D1D1")
    detail.resizable(False, False)

    e = e1.get()
    search_url = "https://en.wikipedia.org/w/api.php"
    search_params = {
        'action': 'query',
        'list': 'search',
        'srsearch': e,
        'format': 'json',
        'utf8': 1,
        'srlimit': 1
    }
    search_resp = requests.get(search_url, params=search_params).json()
    search_results = search_resp.get('query', {}).get('search', [])
    title = search_results[0]['title']

    l1 = tk.Label(detail, text=title, font=("Helvetica", 24, 'bold'), cursor="hand2", bg="#D0D1D1", fg="#080808")
    l1.pack(pady=(20, 15))
    l1.bind("<Button-1>", open)

    page_url = "https://en.wikipedia.org/w/api.php"
    page_params = {
        'action': 'query',
        'titles': title,
        'prop': 'pageimages|extracts|info',
        'exintro': True,
        'explaintext': True,
        'inprop': 'url',
        'format': 'json',
        'pithumbsize': 300
    }
    page_resp = requests.get(page_url, params=page_params).json()
    pages = page_resp['query']['pages']
    page = next(iter(pages.values()))
    summary = page.get('extract', 'No summary available.')
    thumbnail = page.get('thumbnail', {}).get('source', None)
    full_url = page.get('fullurl', None)

    content_frame = tk.Frame(detail, bg="#D0D1D1")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    img_frame = tk.Frame(content_frame, width=310, height=310, bg="white", relief=tk.RAISED, borderwidth=2)
    img_frame.pack(side=tk.TOP, pady=10, anchor='center')

    label_image = tk.Label(img_frame, bg="white")

    if thumbnail:
        try:
            img_data = requests.get(thumbnail).content
            img = Image.open(BytesIO(img_data)).resize((300, 300))
            photo = ImageTk.PhotoImage(img)
            label_image.config(image=photo)
            label_image.image = photo
        except Exception:
            label_image.config(text="Image\nnot\navailable", font=("Segoe UI", 14), fg="gray")
    else:
        label_image.config(text="No Image", font=("Segoe UI", 14), fg="gray")
    label_image.place(x=2, y=2, width=300, height=300)

    text_frame = tk.Frame(content_frame, bg="white")
    text_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

    text_summary = tk.Text(text_frame, wrap=tk.WORD, font=("Segoe UI", 12), relief=tk.FLAT, bg="white")
    text_summary.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
    text_summary.insert(tk.END, summary)
    text_summary.config(state=tk.DISABLED)

    scrollbar = tk.Scrollbar(text_frame, command=text_summary.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_summary.config(yscrollcommand=scrollbar.set)
    e1.delete(0, tk.END)


img = Image.open("li.jpg").resize((600, 650))
bg_img = ImageTk.PhotoImage(img)
canvas = tk.Canvas(win, width=600, height=650, bg="black", highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, anchor="nw", image=bg_img)
canvas.create_text(120, 270, text="Enter", font=("Arial", 17, "bold"), fill="black")

e1 = tk.Entry(win, width=25, font=("Arial", 19), fg="white", bg="#6F6F6F", insertbackground="white", relief=tk.FLAT)
e1.place(x=170, y=255)
e1.bind("<Return>",submit1)

b1 = tk.Button(win, text="Search", font=("Arial", 13, 'bold'), width=13, height=2, bg="#82C8FA",
               fg="white", cursor="hand2", activebackground="#A4C6FA", command=submit)
b1.place(x=230, y=325)

win.mainloop()
