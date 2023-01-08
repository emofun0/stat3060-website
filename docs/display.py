import tkinter as tk


def show_window():
    window = tk.Tk()
    window.resizable(False, False)

    image = tk.PhotoImage(file='image/heat.png')
    image = image.subsample(2, 2)
    canvas = tk.Canvas(window, width=image.width(), height=image.height())
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    popup = tk.Toplevel()
    popup.overrideredirect(True)
    name = tk.StringVar()
    name.set('')
    label = tk.Label(popup, textvariable=name).pack()

    def highlight(num, x, y):
        r = num / 129 * 190
        canvas.create_oval(x - r, y - r, x + r, y + r, tag='circle_highlight', outline='red')

    def on_mouse_move(event):
        # 获取鼠标坐标
        x, y = event.x, event.y
        # 判断鼠标是否在范围内
        if 431 < x < 471 and 415 < y < 455:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('中天社区: 66\n监督组: 5\n综合组: 44\n金山街道综合网格指挥中心: 14')
            highlight(129, 451, 435)
        elif 574 < x < 614 and 275 < y < 315:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('云顶苑: 29')
            highlight(29, 594, 295)
        elif 611 < x < 651 and 232 < y < 272:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('云顶苑4栋高层: 1')
            highlight(1, 631, 252)
        elif 436 < x < 476 and 264 < y < 304:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('俊仕院: 52')
            highlight(52, 456, 284)
        elif 183 < x < 223 and 211 < y < 251:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('天骄苑: 86')
            highlight(86, 203, 231)
        elif 56 < x < 96 and 117 < y < 157:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('天骄苑38栋高层: 13')
            highlight(13, 76, 137)
        elif 291 < x < 331 and 283 < y < 323:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('爱唯大地幼儿园: 39')
            highlight(39, 311, 303)
        elif 286 < x < 326 and 486 < y < 526:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('金爵苑: 58')
            highlight(58, 306, 506)
        elif 549 < x < 589 and 448 < y < 488:
            popup.deiconify()
            popup.geometry('+{}+{}'.format(x + 15 + window.winfo_x(), y + 5 + window.winfo_y()))
            name.set('领秀苑: 55')
            highlight(55, 569, 468)
        else:
            popup.withdraw()
            try:
                canvas.delete('circle_highlight')
            except UnboundLocalError:
                pass

    canvas.bind('<Motion>', on_mouse_move)
    window.mainloop()


if __name__ == "__main__":
    show_window()
