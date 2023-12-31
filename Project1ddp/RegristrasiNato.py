from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x600")

f_data = open("data.txt", "a")
notice = Label(root, text="file is created").place(x=100, y=370)

changefont = tkinter.font.Font(size=20)

judl = Label(root, text="Nato Donuts", font=changefont)
judl.place(x=80, y=10)

labelfr = LabelFrame(root, text="result", padx=20, pady=20)
labelfr.place(x=60, y=380)

nama = Label(root, text="Nama Pemesan").place(x=20, y=50)
Alamat = Label(root, text="Alamat Customer").place(x=20, y=90)
total = Label(root, text="Jumlah Pesanan").place(x=20, y=130)
nomorhp = Label(root, text="Nomor Wa").place(x=20, y=170)
email = Label(root, text="Email").place(x=20, y=210)
varian = Label(root, text="Varian").place(x=20, y=290)

e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root)
e4 = Entry(root, width=40)
e5 = Entry(root, width=40)

e1.place(x=20, y=70)
e2.place(x=20, y=110)
e3.place(x=20, y=150)
e4.place(x=20, y=190)
e5.place(x=20, y=230)

r = StringVar()
r.set("Nato Mini")

rb = Radiobutton(root, text="Nato Mini", variable=r, value="Nato Mini").place(x=20, y=310)
rb2 = Radiobutton(root, text="Nato Reguler", variable=r, value="Nato Reguler").place(x=120, y=310)


def get_harga(varian):
    if varian == "Nato Mini":
        return 30000
    elif varian == "Nato Reguler":
        return 27000
    else:
        return 0


def cetak():
    class orang:
        def __init__(self, nama, Alamat, total, nomorhp, email, varian):
            self.nama = nama
            self.Alamat = Alamat
            self.total = total
            self.nomorhp = nomorhp
            self.email = email
            self.varian = varian

        def hasil(self):
            harga = get_harga(self.varian)
            total_harga = harga * int(self.total)

            lbl_text = (
                f"Terimakasihh Pesananmu Kami Terima!\n\n"
                f"Nama Pemesan: {self.nama}\n"
                f"Alamat Customer: {self.Alamat}\n"
                f"Jumlah Pesanan: {self.total}\n"
                f"Nomor Wa: {self.nomorhp}\n"
                f"Email: {self.email}\n"
                f"Varian: {self.varian}\n"
                f"Total Harga: {total_harga}\n\n"
                f"Silahkan Konfirmasikan Pesananmu Melalui Whatsapp"
            )
            lbl = Label(labelfr, text=lbl_text)
            lbl.grid()

            f_data.write(f"Nama Pemesan: {self.nama}\nAlamat Customer: {self.Alamat}\nJumlah Pesanan: {self.total}\nNomor Wa: {self.nomorhp}\nEmail: {self.email}\nVarian: {self.varian}\nTotal Harga: {total_harga}\n")
            f_data.write("Terimakasihh Pesananmu Kami Terima!\nSilahkan Konfirmasikan Pesananmu Melalui Whatsapp\n\n")

    ditampilkan = orang(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), r.get())
    ditampilkan.hasil()

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


btn = Button(root, text="submit", command=cetak).place(x=100, y=350)

root.mainloop()

