import tkinter
from tkinter import *
class Underground(Tk):
	# Implementasi ini saya dapatkan dari internet dengan keyword "Tkinter multiple frame"
	# diambil dari beberapa tautan, di antaranya
	# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
	# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028

	# constructor untuk class Underground
	def __init__(self):
		#__init__ untuk class Tk
		Tk.__init__(self)

		# membuat container sebagai frame untuk halaman halaman yang ingin ditampilkan
		container = Frame(self)
		container.pack(expand=TRUE)
		
		# menambahkan variabel self.frames dengan dictionary
		self.frames = {}

		# menambahkan isi dictionary self.frames dengan key = nama Class yang ingin ditampilkan
		# dan value adalah menjadikan class sebagai halaman
		self.frames["Home"] = Home(master=container, controller=self)
		self.frames["login"] = login(master=container, controller=self)
		self.frames["Home_Front"] = Home_Front(master=container, controller=self)
		self.frames["add_buku"] = add_buku(master=container, controller=self)
		self.frames["sub_buku"] = sub_buku(master=container, controller=self)
		self.frames["add_rak"] = add_rak(master=container, controller=self)
		self.frames["sub_rak"] = sub_rak(master=container, controller=self)
		self.frames["rak_menu"] = rak_menu(master=container, controller=self)
		self.frames["buku_menu"] = buku_menu(master=container, controller=self)
		
		self.frames["Home"].grid(row=0, column=0, sticky="NSEW")
		self.frames["login"].grid(row=0, column=0, sticky="NSEW")
		self.frames["Home_Front"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_buku"].grid(row=0, column=0, sticky="NSEW")
		self.frames["sub_buku"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_rak"].grid(row=0, column=0, sticky="NSEW")
		self.frames["sub_rak"].grid(row=0, column=0, sticky="NSEW")
		self.frames["rak_menu"].grid(row=0, column=0, sticky="NSEW")
		self.frames["buku_menu"].grid(row=0, column=0, sticky="NSEW")

		# menampilkan halaman
		self.show_frame("Home_Front")

	# method untuk mengganti halaman
	def show_frame(self, halaman):
		frame = self.frames[halaman]
		# tkraise digunakan untuk menimpa frame satu dengan yang lain
		frame.tkraise()

class Home_Front(Frame):
	# constructor __init__ untuk class Home()
	def __init__(self, master, controller):
		self.controller = controller  
		Frame.__init__(self, master)
		# menjalankan method make_widget()
		self.make_widget()

	# method make_widget
	def make_widget(self):
		# variabel yang isinya diperoleh dari isian Entry
		self.nama = StringVar(value="Masukkan nama buku...")

		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.pack(side=TOP, anchor=N, fill=X)
		self.frame_CENTER = Frame(self)
		self.frame_CENTER.pack(side=TOP, anchor=CENTER, fill=BOTH)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		Button(self.frame_TOP, text="HOME", fg="black", font=("Comic Sans MS", 10),bg="#F6D12E").pack(side= LEFT)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="LOG IN",command=lambda: self.controller.show_frame("login"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= RIGHT)
		
		Label(self.frame_CENTER, text="E-PERPUS", font=("Metropolis Black", 20 ), bg="#FF9F00", fg='white', pady=20).pack(side=TOP,fill=BOTH)
		Label(self.frame_CENTER, text="").pack()
		Entry(self.frame_CENTER, textvariable = self.nama, width= 30).pack(side=TOP, fill=BOTH, expand=YES, padx=20)
		#Jika ditekan akan menjalankan method cari_buku()
		Button(self.frame_CENTER, text="CARI BUKU", width=10, command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").pack(side=TOP, padx=2, pady=10)
		
class login(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		
		# LABEL
		Label(self, text="LOG IN Admin", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="Username	").grid(row=2, sticky=W, padx= 20)
		Label(self, text="Password	").grid(row=3, sticky=W, padx= 20)

		# ENTRY
		self.username = StringVar()
		self.password = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.username).grid(row=2, column=1, sticky = W, padx=0)
		self.e2 = Entry(self, width="30", textvariable= self.password).grid(row=3, column=1, sticky = W, padx=0)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="LOG IN", command=self.login, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

	def login(self):
		if self.username.get() + self.password.get() == "adminadmin":
			self.controller.show_frame("Home")
		else:
			print("username/pw salah")

class Home(Frame):
	# constructor __init__ untuk class Home()
	def __init__(self, master, controller):
		self.controller = controller  
		Frame.__init__(self, master)
		# menjalankan method make_widget()
		self.make_widget()

	# method make_widget
	def make_widget(self):
		# variabel yang isinya diperoleh dari isian Entry
		self.nama = StringVar(value="Masukkan nama buku...")

		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.pack(side=TOP, anchor=N, fill=X)
		self.frame_CENTER = Frame(self)
		self.frame_CENTER.pack(side=TOP, anchor=CENTER, fill=BOTH)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		Button(self.frame_TOP, text="HOME", fg="black", font=("Comic Sans MS", 10),bg="#F6D12E").pack(side= LEFT)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= LEFT)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= LEFT)
		Button(self.frame_TOP, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= RIGHT, padx=18)
		
		Label(self.frame_CENTER, text="E-PERPUS", font=("Metropolis Black", 20 ), bg="#FF9F00", fg='white', pady=20).pack(side=TOP,fill=BOTH)
		Label(self.frame_CENTER, text="").pack()
		Entry(self.frame_CENTER, textvariable = self.nama, width= 30).pack(side=TOP, fill=BOTH, expand=YES, padx=20)
		#Jika ditekan akan menjalankan method cari_buku()
		Button(self.frame_CENTER, text="CARI BUKU", width=10, command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").pack(side=TOP, padx=2, pady=10)

class rak_menu(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		Button(self.frame_TOP_Left, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=3, sticky=E)
		
		# LABEL
		Label(self, text="Menu Rak", font=("Metropolis Black", 20)).grid(row=1,column=0,sticky=E, padx=120, pady=20)

		# BUTTON
		Button(self, text="\nTAMBAHKAN RAK\n", command=lambda: self.controller.show_frame("add_rak"), relief=FLAT, font=("Metropolis", 12, "bold"), bg="blue", fg="white").grid(row=2,
		 column=0, padx= 20, pady=2, rowspan=2)
		Button(self, text="\n      HAPUS RAK      \n", command=lambda: self.controller.show_frame("sub_rak"), relief=FLAT, font=("Metropolis", 12, "bold"), bg="blue", fg="white").grid(row=4,
		 column=0, padx= 20, pady=10, rowspan=2)

class buku_menu(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		# Jika Button ditekan akan mengarahkan pada halaman BUKU
		Button(self.frame_TOP, text="BUKU", command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		Button(self.frame_TOP_Left, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=5, sticky=E, padx=18)
		
		# LABEL
		Label(self, text="Menu Buku", font=("Metropolis Black", 20)).grid(row=1,column=0,sticky=E, padx=120, pady=20)

		# BUTTON
		Button(self, text="\nTAMBAHKAN BUKU\n", command=lambda: self.controller.show_frame("add_buku"), relief=FLAT, font=("Metropolis", 12, "bold"), bg="blue", fg="white").grid(row=2,
		 column=0, padx= 20, pady=2, rowspan=2)
		Button(self, text="\nPINJAMKAN BUKU\n", command=lambda: self.controller.show_frame("sub_buku"), relief=FLAT, font=("Metropolis", 12, "bold"), bg="blue", fg="white").grid(row=4,
		 column=0, padx= 20, pady=10, rowspan=2)

class add_rak(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		
		# LABEL
		Label(self, text="Tambahkan Rak", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx= 20)

		# ENTRY
		self.nama_rak = StringVar()
		self.jenis_rak = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=1, sticky = W, padx=0)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="TAMBAHKAN", command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)
	 
class sub_rak(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		
		# LABEL
		Label(self, text="Hapus Rak", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx= 20)

		# ENTRY
		self.nama_rak = StringVar()
		self.jenis_rak = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=1, sticky = W, padx=0)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="HAPUS", command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

class sub_buku(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.make_widget()

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman RAK
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		# Jika Button ditekan akan mengarahkan pada halaman BUKU
		Button(self.frame_TOP, text="BUKU", command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		
		# LABEL
		Label(self, text="Pinjamkan Buku", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA BUKU	").grid(row=2, sticky=W, padx= 20)
		Label(self, text="JUMLAH	").grid(row=3, sticky=W, padx= 20)	

		# ENTRY
		self.nama_rak = StringVar()
		self.jumlah = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=1, sticky = W, padx=0)
		self.e2 = Entry(self, width="30", textvariable= self.jumlah).grid(row=3, column=1, sticky = W, padx=0)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="PINJAMKAN", command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

class add_buku(Frame):
	# Constructor __init__ untuk class add_buku
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master  
		Frame.__init__(self, master)
		self.make_widget()

	# Method add widget
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)

		# Label
		Label(self, text="Tambahkan Buku", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, pady=20, padx=60)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx=20)
		Label(self, text="NAMA BUKU	").grid(row=3, sticky=W, padx=20)
		Label(self, text="TAHUN	").grid(row=4, sticky=W, padx=20)
		Label(self, text="PENGARANG	").grid(row=5, sticky=W, padx=20)
		Label(self, text="PENERBIT	").grid(row=6, sticky=W, padx=20)
		Label(self, text="JENIS BUKU	").grid(row=7, sticky=W, padx=20)
		Label(self, text="STOK	").grid(row=8, sticky=W, padx=20)
		Label(self, text="").grid(row=9, sticky=W, padx=0)


		# Entry
		self.nama_rak = StringVar()
		self.nama_buku = StringVar()
		self.tahun_terbit = StringVar()
		self.pengarang_buku = StringVar()
		self.penerbit = StringVar()
		self.jenis_buku = StringVar()
		self.stok = StringVar()
	
		self.e1 = Entry(self, width="30", textvariable=self.nama_rak).grid(row=2, column=1, sticky=W, padx=0)
		self.e2 = Entry(self, width="30", textvariable=self.nama_buku).grid(row=3, column=1, sticky=W, padx=0)
		self.e3 = Entry(self, width="30", textvariable=self.tahun_terbit).grid(row=4, column=1, sticky=W, padx=0)
		self.e4 = Entry(self, width="30", textvariable=self.pengarang_buku).grid(row=5, column=1, sticky=W, padx=0)
		self.e5 = Entry(self, width="30", textvariable=self.penerbit).grid(row=6, column=1, sticky=W, padx=0)
		self.e6 = Entry(self, width="30", textvariable=self.jenis_buku).grid(row=7, column=1, sticky=W, padx=0)
		self.e7 = Entry(self, width="30", textvariable=self.stok).grid(row=8, column=1, sticky=W, padx=0)

		# Button
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=10, column=0, sticky=W, padx=20, pady=20)
		Button(self, text="TAMBAHKAN", command=NONE, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=10, column=1, sticky=W, padx=20, pady=20)

if __name__ == '__main__':
	app = Underground()
	app.title('APLIKASI PERPUSTAKAAN')		# memberi judul
	app.wm_geometry("400x340")			# mengatur luas
	app.configure(bg ="#CB0B0B")		# mengatur warna backgrund
	app.mainloop()