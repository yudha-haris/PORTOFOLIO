import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

def load_file():
	file_name = askopenfilename(filetypes=[("All files", "*")])
	if not file_name:
		return
	text_file = open(file_name, 'r', encoding="utf-8")
	result = text_file.read()
	global database
	database = eval(result)
	overlay_status.destroy()

def save_file():
	file_name = asksaveasfilename(filetypes=[("All files", "*")])
	if not file_name:
		return
		
	with open(file_name, "w") as output_file:
		output_file.write(str(database))
		overlay_status.destroy()  

def status():
	# GUI
	global overlay_status
	overlay_status = Toplevel()
	overlay_status.geometry("300x300")
	frame_BOT = Frame(overlay_status)
	frame_BOT.pack(side=BOTTOM)
	Label(overlay_status, text="\nSTATUS", font=("Metropolis Black", 15)).pack()
	Button(frame_BOT, text="SAVE", command=save_file).pack(side=LEFT, pady=10)
	Label(frame_BOT, text="	").pack(side=LEFT)
	Button(frame_BOT, text="LOAD", command=load_file).pack(side=LEFT, pady=10)

	# ACTION
	status_data = []
	for x,y in database.items():
		status_data.append(f"___{x}___")
		for i in range(len(y)):
			if i % 6 == 0:
				status_data.append(f"{y[i]}, stock: {y[i+5]}")
	if status_data == []:
		result_status_data = "Belum ada buku maupun rak!"
	else:
		result_status_data = "\n".join(status_data)
	Label(overlay_status, text=result_status_data).pack() 

database = {}

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
		self.frames["add_stok_buku"] = add_stok_buku(master=container, controller=self)
		self.frames["sub_buku"] = sub_buku(master=container, controller=self)
		self.frames["add_rak"] = add_rak(master=container, controller=self)
		self.frames["sub_rak"] = sub_rak(master=container, controller=self)
		self.frames["rak_menu"] = rak_menu(master=container, controller=self)
		self.frames["buku_menu"] = buku_menu(master=container, controller=self)
		
		self.frames["Home"].grid(row=0, column=0, sticky="NSEW")
		self.frames["login"].grid(row=0, column=0, sticky="NSEW")
		self.frames["Home_Front"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_buku"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_stok_buku"].grid(row=0, column=0, sticky="NSEW")
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
		Button(self.frame_TOP, text="HOME", fg="black", font=("Metropolis", 10),bg="#DFE3EE").pack(side= LEFT)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="LOG IN",command=lambda: self.controller.show_frame("login"), relief=FLAT, fg="black", font=("Metropolis", 10)).pack(side= RIGHT, padx = 18)
		
		Label(self.frame_CENTER, text="E-PERPUS", font=("Metropolis Black", 20 ), bg="#0E68CE", fg='white', pady=20).pack(side=TOP,fill=BOTH)
		Label(self.frame_CENTER, text="").pack()
		Entry(self.frame_CENTER, textvariable = self.nama, width= 30).pack(side=TOP, fill=BOTH, expand=YES, padx=20)
		#Jika ditekan akan menjalankan method cari_buku()
		Button(self.frame_CENTER, text="CARI BUKU", width=10, command=self.cari_buku, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").pack(side=TOP, padx=2, pady=10)
	
	def cari_buku(self):
		# menampilkan pada jendela baru
		overlay = Toplevel(self)
		# Apabila user tidak memasukkan nama buku yang dicari
		if self.nama.get() == "Masukkan nama buku...":
			Label(overlay, text="\nMasukkan nama buku!\n", font=("Metropolis", 12)).pack(fill=BOTH)
			overlay.geometry("300x50")
			overlay.title("Error Message")
		else:
			Label(overlay, text="\nHasil Pencarian Buku:", font=("Metropolis Black", 15)).pack()
			config = 0
			for x,y in database.items():
				for i in range(len(y)):
					if y[i] == self.nama.get():
						template = f"Nama Buku\nTahun Terbit\nPengarang\nPenerbit\nJenis Buku\nStok"
						result =  f": {y[i]}\n: {y[i+1]}\n: {y[i+2]}\n: {y[i+3]}\n: {y[i+4]}\n: {y[i+5]}"
						Message(overlay, text=template).pack(side=LEFT, padx =20)
						Message(overlay, text=result).pack(side=LEFT, padx=5)
						config = 1
						break
			if config == 0:
				result = "Buku tidak ditemukan!"
				Label(overlay, text=result).pack()
			overlay.title("Hasil Pencarian")
			overlay.geometry("300x300")
				
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
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		# LABEL
		Label(self, text="LOG IN Admin", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="Username	").grid(row=2, sticky=W, padx= 20)
		Label(self, text="Password	").grid(row=3, sticky=W, padx= 20)

		# ENTRY
		self.username = StringVar()
		self.password = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.username).grid(row=2, column=0,sticky = E, columnspan=2)
		self.e2 = Entry(self, width="30", textvariable= self.password).grid(row=3, column=0,sticky = E, columnspan=2)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="LOG IN", command=self.login, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

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
		self.make_widget()

	# method make_widget
	def make_widget(self):
		self.nama = StringVar(value="Masukkan nama buku...")

		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.pack(side=TOP, anchor=N, fill=X)
		self.frame_CENTER = Frame(self)
		self.frame_CENTER.pack(side=TOP, anchor=CENTER, fill=BOTH)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", fg="black", font=("Metropolis", 10),bg="#DFE3EE").pack(side= LEFT)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, fg="black", font=("Metropolis", 10)).pack(side= LEFT)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Metropolis", 10)).pack(side= LEFT)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).pack(side= LEFT)
		Button(self.frame_TOP, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Metropolis", 10)).pack(side= RIGHT, padx=18)
		
		Label(self.frame_CENTER, text="E-PERPUS", font=("Metropolis Black", 20 ), bg="#3B5998", fg='white', pady=20).pack(side=TOP,fill=BOTH)
		Label(self.frame_CENTER, text="").pack()
		Entry(self.frame_CENTER, textvariable = self.nama, width= 30).pack(side=TOP, fill=BOTH, expand=YES, padx=20)
		Button(self.frame_CENTER, text="CARI BUKU", width=10, command=self.cari_buku, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").pack(side=TOP, padx=2, pady=10)
	
	def cari_buku(self):
		overlay = Toplevel(self)
		if self.nama.get() == "Masukkan nama buku...":
			Label(overlay, text="\nMasukkan nama buku!\n", font=("Metropolis", 12)).pack(fill=BOTH)
			overlay.geometry("300x50")
			overlay.title("Error Message")
		else:
			Label(overlay, text="\nHasil Pencarian Buku:", font=("Metropolis Black", 15)).pack()
			config = 0
			for x,y in database.items():
				for i in range(len(y)):
					if y[i] == self.nama.get():
						template = f"Nama Buku\nTahun Terbit\nPengarang\nPenerbit\nJenis Buku\nStok"
						result =  f": {y[i]}\n: {y[i+1]}\n: {y[i+2]}\n: {y[i+3]}\n: {y[i+4]}\n: {y[i+5]}"
						Message(overlay, text=template).pack(side=LEFT, padx =20)
						Message(overlay, text=result).pack(side=LEFT, padx=5)
						config = 1
						break
			if config == 0:
				result = "Buku tidak ditemukan!"
				Label(overlay, text=result).pack()
			overlay.title("Hasil Pencarian")
			overlay.geometry("300x300")

class rak_menu(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)
		Button(self.frame_TOP_Left, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=4, sticky=E)
		
		# LABEL
		Label(self, text="Menu Rak", font=("Metropolis Black", 20)).grid(row=1,column=0,sticky=E, padx=120, pady=20)

		# BUTTON
		Button(self, text="TAMBAHKAN RAK", command=lambda: self.controller.show_frame("add_rak"), relief=SOLID, font=("Metropolis", 12, "bold"), fg="black").grid(row=2,
		 column=0, padx= 20, pady=2, rowspan=2)
		Button(self, text="      HAPUS RAK      ", command=lambda: self.controller.show_frame("sub_rak"), relief=SOLID, font=("Metropolis", 12, "bold"), fg="black").grid(row=4,
		 column=0, padx= 20, pady=10, rowspan=2)

class buku_menu(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)
		Button(self.frame_TOP_Left, text="LOG OUT", command=lambda: self.controller.show_frame("Home_Front"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=5, sticky=E, padx=18)
		
		# LABEL
		Label(self, text="Menu Buku", font=("Metropolis Black", 20)).grid(row=1,column=0,sticky=E, padx=120, pady=20)

		# BUTTON
		Button(self, text=" TAMBAHKAN BUKU ", command=lambda: self.controller.show_frame("add_buku"), relief=SOLID, font=("Metropolis", 12, "bold")).grid(row=2,
		 column=0, padx= 20, pady=2, rowspan=2)
		Button(self, text="  PINJAMKAN BUKU  ", command=lambda: self.controller.show_frame("sub_buku"), relief=SOLID, font=("Metropolis", 12, "bold")).grid(row=4,
		 column=0, padx= 20, pady=10, rowspan=2)
		Button(self, text="TAMBAH STOK BUKU", command=lambda: self.controller.show_frame("add_stok_buku"), relief=SOLID, font=("Metropolis", 12, "bold")).grid(row=6,
		 column=0, padx= 20, pady=2, rowspan=2)

class add_rak(Frame):
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)
		
		# LABEL
		Label(self, text="   Tambahkan Rak", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx= 20)

		# ENTRY
		self.nama_rak = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=0, sticky = E, columnspan=2)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="TAMBAHKAN", command=self.tambah_rak, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

	def tambah_rak(self):
		# GUI
		overlay = Toplevel(self)
		overlay.geometry("300x50")
		
		# ACTION
		kumpulan_rak = database.keys()
		if self.nama_rak.get() in kumpulan_rak:
			Label(overlay, text=f"Rak dengan nama {self.nama_rak.get()} sudah ada!").pack()
		else:
			# ACTION
			database.update({self.nama_rak.get():[]})
			# GUI
			Label(overlay, text=f"Rak dengan nama {self.nama_rak.get()} berhasil ditambahkan!").pack()
	 
class sub_rak(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)

		# LABEL
		Label(self, text="        HAPUS RAK", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, column=0, sticky=W, padx= 20)

		# ENTRY
		self.nama_rak = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=0, sticky = E, columnspan=2)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("rak_menu"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="HAPUS", command=self.hapus_rak, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

	def hapus_rak(self):
		
		# GUI
		global overlay_sub_rak
		overlay_sub_rak = Toplevel(self)
		overlay_sub_rak.geometry("300x50")
		# ACTION
		kumpulan_rak = database.keys()
		if self.nama_rak.get() in kumpulan_rak:
			if len(database[self.nama_rak.get()]) != 0:

				# GUI
				overlay_sub_rak.title("Warning")
				Label(overlay_sub_rak, text="Masih ada buku di rak, tetap lanjutkan?").pack()
				Button(overlay_sub_rak, text="YES", command=self.popup).pack()
			else:
				# ACTION
				database.pop(self.nama_rak.get())

				# GUI
				Label(overlay_sub_rak, text=f"Rak dengan nama {self.nama_rak.get()} berhasil dihapus").pack()
		else:
			Label(overlay_sub_rak, text=f"Tidak ditemukan rak dengan nama {self.nama_rak.get()}").pack()
		
	def popup(self):
		# Action
		database.pop(self.nama_rak.get())

		# GUI
		overlay_sub_rak.destroy()
		overlay= Toplevel(self)
		overlay.geometry("300x50")
		Label(overlay, text=f"Rak dengan nama {self.nama_rak.get()} berhasil dihapus").pack()
		
class sub_buku(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)
		
		# LABEL
		Label(self, text="  Pinjamkan Buku", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA BUKU	").grid(row=2, sticky=W, padx= 20)
		Label(self, text="JUMLAH	").grid(row=3, sticky=W, padx= 20)	

		# ENTRY
		self.nama_buku = StringVar()
		self.jumlah = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_buku).grid(row=2, column=0,sticky = E, columnspan=2)
		self.e2 = Entry(self, width="30", textvariable= self.jumlah).grid(row=3, column=0,sticky = E, columnspan=2)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="PINJAMKAN", command=self.pinjamkan_buku, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

	def pinjamkan_buku(self):
		# GUI
		overlay = Toplevel(self)
		overlay.geometry("300x50")

		# ACTION
		config = 0
		for x,y in database.items():
			for i in range(len(y)):
				if self.nama_buku.get() == y[i]:
					if int(y[i+5]) < int(self.jumlah.get()):
						Label(overlay, text="Jumlah buku kurang dari permintaan!").pack()
						config = 1
						break
					else:
						y[i+5] = str(int(y[i+5]) - int(self.jumlah.get()))
						Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()}\ndipinjamkan sebanyak {self.jumlah.get()}").pack()
						config = 1
						break
		if config == 0:
			Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()} tidak ada!").pack()

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
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)
		
		# Label
		Label(self, text="  Tambahkan Buku", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, pady=20, padx=60)
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
	
		self.e1 = Entry(self, width="30", textvariable=self.nama_rak).grid(row=2, column=0,sticky = E, columnspan=2)
		self.e2 = Entry(self, width="30", textvariable=self.nama_buku).grid(row=3, column=0,sticky = E, columnspan=2)
		self.e3 = Entry(self, width="30", textvariable=self.tahun_terbit).grid(row=4, column=0,sticky = E, columnspan=2)
		self.e4 = Entry(self, width="30", textvariable=self.pengarang_buku).grid(row=5, column=0,sticky = E, columnspan=2)
		self.e5 = Entry(self, width="30", textvariable=self.penerbit).grid(row=6, column=0,sticky = E, columnspan=2)
		self.e6 = Entry(self, width="30", textvariable=self.jenis_buku).grid(row=7, column=0,sticky = E, columnspan=2)
		self.e7 = Entry(self, width="30", textvariable=self.stok).grid(row=8, column=0,sticky = E, columnspan=2)

		# Button
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=10, column=0, sticky=W, padx=20, pady=20)
		Button(self, text="TAMBAHKAN", command=self.add_buku, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=10, column=1, sticky=W, padx=20, pady=20)
	
	def add_buku(self):
		# GUI
		overlay = Toplevel(self)
		overlay.geometry("300x50")

		# VARIABEL
		kumpulan_rak = database.keys()
		template = [self.nama_buku.get(),self.tahun_terbit.get(),self.pengarang_buku.get(),self.penerbit.get(),self.jenis_buku.get(),self.stok.get()]
		
		# ACTION
		if self.nama_rak.get() in kumpulan_rak:
			for i in template:
				database[self.nama_rak.get()].append(i)
				# GUI
			Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()}\nberhasil ditambahkan pada rak {self.nama_rak.get()}").pack()
			print(database)
		else:
			database.update({self.nama_rak.get():template})
			# GUI
			Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()}\nberhasil ditambahkan pada rak {self.nama_rak.get()}").pack()

class add_stok_buku(Frame):
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)
		self.make_widget()

	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)
		self.frame_TOP_Left = Frame(self)
		self.frame_TOP_Left.grid(row=0, sticky=E)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="RAK",command=lambda: self.controller.show_frame("rak_menu"),relief=FLAT,fg="black", font=("Metropolis", 10)).grid(row=0, column=1)
		Button(self.frame_TOP, text="BUKU", command=None, bg="#DFE3EE",fg="black", font=("Metropolis", 10)).grid(row=0, column=2)
		Button(self.frame_TOP, text="STATUS", command=status, relief=FLAT, fg="black", font=("Metropolis", 10)).grid(row=0, column=3)

		# LABEL
		Label(self, text="     TAMBAH STOK", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, column=0, sticky=W, padx= 20)
		Label(self, text="JUMLAH	").grid(row=3, column=0, sticky=W, padx= 20)

		# ENTRY
		self.nama_buku = StringVar()
		self.jumlah = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_buku).grid(row=2, column=0, sticky = E, columnspan=2)
		self.e2 = Entry(self, width="30", textvariable= self.jumlah).grid(row=3, column=0, sticky = E, columnspan=2)

		# BUTTON
		Button(self, text="<< BACK", command=lambda: self.controller.show_frame("buku_menu"), relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=0, sticky=W, padx= 20, pady=50)
		Button(self, text="TAMBAH", command=self.pinjamkan_buku, relief=FLAT, font=("Metropolis", 10), bg="#003B7A", fg="white").grid(row=8, column=1, sticky=E, padx= 20, pady=50)

	def pinjamkan_buku(self):
		# GUI
		overlay = Toplevel(self)
		overlay.geometry("300x50")

		# ACTION
		config = 0
		for x,y in database.items():
			for i in range(len(y)):
				if self.nama_buku.get() == y[i]:
					y[i+5] = str(int(y[i+5]) + int(self.jumlah.get()))
					Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()}\nditambahkan sebanyak {self.jumlah.get()}").pack()
					config = 1
					break
		if config == 0:	
			Label(overlay, text=f"Buku dengan nama {self.nama_buku.get()} tidak ada!").pack()

if __name__ == '__main__':
	app = Underground()
	app.title('APLIKASI PERPUSTAKAAN')	
	app.wm_geometry("400x340")	
	app.configure(bg ="#81BAC2")	
	app.mainloop()