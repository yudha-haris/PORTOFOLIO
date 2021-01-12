import tkinter
from tkinter import *

class Book:
	# Constructor dalam Class Book
	def __init__(self, nama, tahun, penulis, penerbit):
		self.__nama = nama
		self.__tahun = tahun
		self.__penulis = penulis
		self.__penerbit = penerbit
	
	# Getter untuk mengakses variabel privat
	def get_nama(self):
		return self.__nama
	def get_tahun(self):
		return self.__tahun
	def get_penulis(self):
		return self.__penulis
	def get_penerbit(self):
		return self.__penerbit

	# Setter untuk memodifikasi variabel privat
	def set_nama(self, nama):
		self.__nama = nama
	def set_tahun(self, tahun):
		self.__tahun = tahun
	def set_penulis(self, penulis):
		self.__penulis = penulis
	def set_penerbit(self, penerbit):
		self.__penerbit = penerbit

	# Method mencetak identitas buku
	def get_book_description(self):
		print("Nama Buku: {}".format(self.get_nama())).pack()
		print("Tahun: {}".format(self.get_tahun()))
		print("Pengarang: {}".format(self.get_penulis()))
		print("Penerbit: {}".format(self.get_penerbit()))
	
	# operator overloading untuk method sorted() dengan mengambil nama buku saja
	def __eq__(self, other):
		if (self.get_nama() == other.get_nama()):
			return True
		else:
			return False
	def __lt__(self, other):
		if (self.get_nama() < other.get_nama()):
			return True
		else:
			return False

class FictionBook(Book):
	# Constructor dari Class dengan menerapkan konsep inheritance
	def __init__(self, nama, tahun, penulis, penerbit, jenis, genre):
		super().__init__(nama, tahun, penulis, penerbit)
		self.__jenis = jenis
		self.__genre = genre

	# Getter untuk mengakses variabel privat
	def get_jenis(self):
		return self.__jenis
	def get_genre(self):
		return self.__genre

	# Setter untuk memodifikasi variabel privat
	def set_jenis(self, jenis):
		self.__jenis = jenis
	def set_genre(self, genre):
		self.__genre = genre

	# method untuk mencetak identitas buku
	def get_book_description(self):
		return "Buku {}\nNama Buku: {}\nTahun: {}\nPengarang: {}\nPenerbit: {}\nGenre: {}".format(self.get_jenis(), self.get_nama(), self.get_tahun(), self.get_penulis(), self.get_penerbit(), self.get_genre())       

class ReferenceBook(Book):
	# Constructor dari Class dengan menerapkan konsep inheritance
	def __init__(self, nama, tahun, penulis, penerbit, jenis, kota_terbit):
		super().__init__(nama, tahun, penulis, penerbit)
		self.__jenis = jenis
		self.__kota_terbit = kota_terbit

	# Getter untuk mengakses variabel privat
	def get_jenis(self):
		return self.__jenis
	def get_kota_terbit(self):
		return self.__kota_terbit

	# Setter untuk memodifikasi variabel privat
	def set_jenis(self, jenis):
		self.__jenis = jenis
	def set_kota_terbit(self, kota_terbit):
		self.__kota_terbit = kota_terbit

	# method untuk mencetak identitas buku
	def get_book_description(self):
		return "Buku {}\nNama Buku: {}\nTahun: {}\nPengarang: {}\nPenerbit: {}\nKota Terbit: {}".format(self.get_jenis(), self.get_nama(), self.get_tahun(), self.get_penulis(), self.get_penerbit(), self.get_kota_terbit())

class Encyclopedia(Book):
	# Constructor dari Class dengan menerapkan konsep inheritance
	def __init__(self, nama, tahun, penulis, penerbit, jenis, revisi_num):
		super().__init__(nama, tahun, penulis, penerbit)
		self.__jenis = jenis
		self.__revisi_num = revisi_num

	# Getter untuk mengakses variabel privat
	def get_jenis(self):
		return self.__jenis
	def get_revisi_num(self):
		return self.__revisi_num

	# Setter untuk memodifikasi variabel privat
	def set_jenis(self, jenis):
		self.__jenis = jenis
	def set_revisi_num(self, revisi_num):
		self.__revisi_num = revisi_num

	# method untuk mencetak identitas buku
	def get_book_description(self):
		return "Buku {}\nNama Buku: {}\nTahun: {}\nPengarang: {}\nPenerbit: {}\nNomor Revisi: {}".format(self.get_jenis(), self.get_nama(), self.get_tahun(), self.get_penulis(), self.get_penerbit(), self.get_revisi_num())    

class Shelf:

	# Constructor dari Class Shelf dengan parameter kumpulan buku bernilai default = []
	def __init__(self, nama, kumpulan_buku = []):
		self.__nama = nama
		self.__kumpulan_buku = kumpulan_buku

	# Getter untuk mengakses variabel privat
	def get_nama(self):
		return self.__nama
	def get_kumpulan_buku(self):
		return self.__kumpulan_buku

	# Setter untuk memodifikasi variabel privat
	def set_nama(self, nama):
		self.__nama = nama
	def set_kumpulan_buku(self, buku):
		self.__kumpulan_buku.append(buku)
	
	# method search_buku()
	def search_buku(self, nama_buku):
		if len(self.get_kumpulan_buku()) == 0:
			return "nope"
		else:
			ada = False
			for buku in self.get_kumpulan_buku():
				if buku.get_nama() == nama_buku:
					return buku.get_book_description()
			return "nope"

	
	# method list_buku()
	def list_buku(self):
		# list untuk menampung nama buku bervariabel penanda_buku
		global penanda_buku
		penanda_buku = []
		for buku in sorted(self.get_kumpulan_buku()):
			# semua buku yang ada di dalam rak dimasukkan ke LIST daftar
			daftar.append("- {}".format(buku.get_nama()))
			# semua buku yang ada di dalam rak juga dimasukkan ke LIST penanda_buku
			penanda_buku.append(buku.get_nama())

class KnowledgeShelf(Shelf):
    # Constructor untuk Class dengan menerapkan konsep inheritance
    def __init__(self, nama, kumpulan_buku = []):
        super().__init__(nama, kumpulan_buku)
    
    # method add_buku
    def add_buku(self, nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut):
        
        # menyesuaikan jenis buku untuk dimasukkan ke dalam class yang sesuai
        if jenis_buku == "Ensiklopedia":
            buku = Encyclopedia(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()
        elif jenis_buku == "Referensi":
            buku = ReferenceBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()

class WorldShelf(Shelf):
    # Constructor untuk Class dengan menerapkan konsep inheritance
    def __init__(self, nama, kumpulan_buku = []):
        super().__init__(nama, kumpulan_buku)
    
    # method add_buku
    def add_buku(self, nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut):
        
        # menyesuaikan jenis buku untuk dimasukkan ke dalam class yang sesuai
        if jenis_buku == "Ensiklopedia":
            buku = Encyclopedia(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()
        elif jenis_buku == "Fiksi":
            buku = FictionBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()

class MysteryShelf(Shelf):
    # Constructor untuk Class dengan menerapkan konsep inheritance
    def __init__(self, nama, kumpulan_buku = []):
        super().__init__(nama, kumpulan_buku)
    
    # method add_buku
    def add_buku(self, nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut):
        
        # menyesuaikan jenis buku untuk dimasukkan ke dalam class yang sesuai
        if jenis_buku == "Referensi":
            buku = ReferenceBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()
        elif jenis_buku == "Fiksi":
            buku = FictionBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()

class CompendiumShelf(Shelf):
    # Constructor untuk Class dengan menerapkan konsep inheritance
    def __init__(self, nama, kumpulan_buku = []):
        super().__init__(nama, kumpulan_buku)
    
    # method add_buku
        
        # menyesuaikan jenis buku untuk dimasukkan ke dalam class yang sesuaidef add_buku(self
    def add_buku(self,nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut):
        if jenis_buku == "Ensiklopedia":
            buku = Encyclopedia(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()
        elif jenis_buku == "Referensi":
            buku = ReferenceBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()
        elif jenis_buku == "Fiksi":
            buku = FictionBook(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
            # menambahkan buku ke dalam list dengan metode setter
            self.set_kumpulan_buku(buku)
            # Mencetak deskripsi buku
            return buku.get_book_description()

class Library:
	# Constructor untuk Class Library()
	def __init__(self):
		self.__kumpulan_rak = [KnowledgeShelf("Pengetahuan01", []), WorldShelf("Dunia01", []), MysteryShelf("Misteri01", []), CompendiumShelf("Compendium01", [])]
		self.__rak = [["Dunia01","Dunia"],["Compendium01","Compendium"],["Misteri01","Misteri"],["Pengetahuan01","Pengetahuan"]]
		self.__buku = []
	
	# getter untuk mengakses privat variabel
	def get_kumpulan_rak(self):
		return self.__kumpulan_rak
	def get_rak(self):
		return self.__rak
	def get_buku(self):
		return self.__buku

	# Setter untuk mengubah privat variabel
	def set_kumpulan_rak(self, rak):
		self.__kumpulan_rak.append(rak)
	def set_rak(self, rak):
		self.__rak.append(rak)
	def set_buku(self, buku):
		self.__buku.append(buku)

	# method add_rak dengan mencocokan jenis rak dan raknya
	def add_rak(self, rak, rak_tujuan):
		if rak_tujuan == "Pengetahuan":
			self.set_kumpulan_rak(KnowledgeShelf(rak))
		elif rak_tujuan == "Misteri":
			self.set_kumpulan_rak(MysteryShelf(rak))
		elif rak_tujuan == "Dunia":
			self.set_kumpulan_rak(WorldShelf(rak))
		elif rak_tujuan == "Compendium":
			self.set_kumpulan_rak(CompendiumShelf(rak))

	# method add_buku dengan menyesuaikan buku dengan rak yang akan ditempati
	def add_buku(self, nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut):
		for rak in self.get_kumpulan_rak():
			if(rak.get_nama() == nama_rak):
				return rak.add_buku(nama_buku, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

	# method search_buku di dalam class Library() melooping semua rak terlebih dahulu, rak hasil loop tadi diolah dalam class Shelf

	def search_buku(self, nama_buku):
		hasil_pencarian = ["Buku ditemukan\n\n"]
		for rak in self.get_kumpulan_rak():
			x = rak.search_buku(nama_buku)
			if x != "nope":
				hasil_pencarian.append(x)
		if len(hasil_pencarian) == 1:
			return "Buku dengan nama {} tidak ditemukan".format(nama_buku)
		else:
			return hasil_pencarian[0] + hasil_pencarian[1]

	# method list_buku() mencetak semua rak diikuti dengan buku yang ada dengan mengolah rak di class Shelf 
	def list_buku(self):

		# variabel untuk menyimpak rak dan buku secara berurutan
		global daftar
		daftar = []
		for rak in self.get_kumpulan_rak():
			# menambahkan rak pada LIST daftar
			daftar.append("{}".format(rak.get_nama()))
			# mengambil semua isi buku di rak
			rak.list_buku()
		return "\n".join(daftar)

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
		self.frames["add_buku"] = add_buku(master=container, controller=self)
		self.frames["add_rak"] = add_rak(master=container, controller=self)
		
		self.frames["Home"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_buku"].grid(row=0, column=0, sticky="NSEW")
		self.frames["add_rak"].grid(row=0, column=0, sticky="NSEW")

		# menampilkan halaman
		self.show_frame("Home")

	# method untuk mengganti halaman
	def show_frame(self, halaman):
		frame = self.frames[halaman]
		# tkraise digunakan untuk menimpa frame satu dengan yang lain
		frame.tkraise()

# Objek / Compostion yang memanggil class Library()
library = Library()

# implementasi dari list
def list_buku():

	# menampilkan dalam popUp
	window = Toplevel()
	Label(window, text="").pack()
	Label(window, text="Daftar Buku", font=("Metropolis Black", 15)).pack()

	if len(library.get_buku()) == 0:		# jika buku tidak ada
		Label(window, text="Belum ada buku di dalam sistem : (").pack()
		print("Belum ada buku di dalam sistem : (")
		print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
	else:
		Message(window, text=library.list_buku()).pack(side=TOP)
		print(library.list_buku())
		print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
	window.wm_geometry("300x300")
	window.configure()

class Home(Frame):
	# constructor __init__ untuk class Home()
	def __init__(self, master, controller):
		self.controller = controller  
		Frame.__init__(self, master)
		# menjalankan method make_widget()
		self.make_widget()

	# method make_widget
	def make_widget(self):
		print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
		# variabel yang isinya diperoleh dari isian Entry
		self.nama = StringVar(value="Masukkan nama buku...")

		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.pack(side=TOP, anchor=N, fill=X)
		self.frame_CENTER = Frame(self)
		self.frame_CENTER.pack(side=TOP, anchor=CENTER, fill=BOTH)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman add rak
		Button(self.frame_TOP, text="HOME", fg="black", font=("Comic Sans MS", 10),bg="#F6D12E").pack(side= LEFT)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="ADD RAK",command=lambda: self.controller.show_frame("add_rak"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= LEFT)
		# Jika Button ditekan akan mengarahkan pada halaman add buku
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="ADD BUKU", command=lambda: self.controller.show_frame("add_buku"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= LEFT)
		# Jika ditekan akan menjalankan method list_buku()
		Button(self.frame_TOP, text="LIST", command=list_buku, relief=FLAT, fg="black", font=("Comic Sans MS", 10)).pack(side= LEFT)
		
		Label(self.frame_CENTER, text="The Great Library", font=("Metropolis Black", 20 ), bg="#FF9F00", fg='white', pady=20).pack(side=TOP,fill=BOTH)
		Label(self.frame_CENTER, text="").pack()
		Entry(self.frame_CENTER, textvariable = self.nama, width= 30).pack(side=TOP, fill=BOTH, expand=YES, padx=20)
		#Jika ditekan akan menjalankan method cari_buku()
		Button(self.frame_CENTER, text="CARI BUKU", width=10, command=self.cari_buku, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").pack(side=TOP, padx=2, pady=10)

	def cari_buku(self):
		# menampilkan pada jendela baru
		overlay = Toplevel(self)
		# Apabila user tidak memasukkan nama buku yang dicari
		if self.nama.get() == "Masukkan nama buku...":
			Label(overlay, text="\nMasukkan nama buku!\n", font=("Metropolis Black", 12), fg="white", bg="red").pack(fill=BOTH)
			print("Perintah tidak valid")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			overlay.geometry("300x50")

		else:
			# Mencetak hasil pencarian
			Label(overlay, text="\nHasil Pencarian Buku:", font=("Metropolis Black", 15)).pack()
			Label(overlay, text=library.search_buku(self.nama.get())).pack()
			print(library.search_buku(self.nama.get()))
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			overlay.geometry("300x300")
		overlay.title("Error Message")

class add_rak(Frame):
	# Constructor untuk class add_rak()
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master
		Frame.__init__(self, master)

		# variabel privat
		self.__rak_saja = ["Dunia01","Compendium01","Misteri01","Pengetahuan01"]
		self.make_widget()

	# Getter untuk mengakses variabel privat
	def get_rak_saja(self):
		return self.__rak_saja

	# Setter untuk memodifikasi variabel privat
	def set_rak_saja(self, rak):
		self.__rak_saja.append(rak)

	# Method Make_widget()
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman add rak
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		Button(self.frame_TOP, text="ADD RAK",command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		# Jika Button ditekan akan mengarahkan pada halaman add buku
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="ADD BUKU", command=lambda: self.controller.show_frame("add_buku"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		# Jika ditekan akan menjalankan method list_buku()
		Button(self.frame_TOP, text="LIST", command=list_buku, relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=3)
		
		# LABEL
		Label(self, text="Tambahkan Rak", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, padx=60, pady=20)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx= 20)
		Label(self, text="JENIS RAK	").grid(row=3, sticky=W, padx= 20)


		# ENTRY
		self.nama_rak = StringVar()
		self.jenis_rak = StringVar()
		self.e1 = Entry(self, width="30", textvariable= self.nama_rak).grid(row=2, column=0, sticky = E, padx=0)
		self.e2 = Entry(self, width="30", textvariable=self.jenis_rak).grid(row=3, column=0, sticky = E, padx=0)

		# BUTTON
		Button(self, text="TAMBAHKAN", command=self.penampung_add_rak, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=8, column=0, sticky=E, padx= 20, pady=50)
	
	#Method penampung_add_rak() 
	def penampung_add_rak(self):
		# membuat overlay
		window = Toplevel(self.controller)

		# apabila user tidak mengisi Entry
		if self.nama_rak.get() == "":
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			print("Perintah Tidak Valid! ")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			x = "Perintah Tidak Valid! "
		elif self.jenis_rak.get() == "":
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			print("Perintah Tidak Valid! ")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			x = "Perintah Tidak Valid! "

		# Jika user mmengisi entry
		else:
			# Menggunakan Input dari Entry sebaagai string yang akan diolah
			pencacah = self.nama_rak.get() + " " + self.jenis_rak.get()
			# Menjadikan input terasebut menjadi list
			pencacah = pencacah.split(" ")

			# Mengecek ketersediaan rak
			if pencacah[0] in self.get_rak_saja():
				Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
				print("Rak dengan nama {} sudah ada di dalam sistem".format(pencacah[0]))
				print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
				x = "Rak dengan nama {} \nsudah ada di dalam sistem".format(pencacah[0])
			
			# Apabila rak belum ada, maka akan ditambahkan
			else:
				# Mencocokan rak dengan jenisnya
				if pencacah[1] == "Dunia":
					library.set_rak([pencacah[0],pencacah[1]])
					self.set_rak_saja(pencacah[0])
					print("Rak baru berhasil ditambahkan \n")
					print("Nama: {}".format(pencacah[0]))
					print("Jenis: {}".format(pencacah[1]))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					x = "Rak baru berhasil ditambahkan \n \nNama: {}\nJenis: {}".format(pencacah[0],pencacah[1])
					library.add_rak(pencacah[0],pencacah[1])
				elif pencacah[1] == "Pengetahuan":
					library.set_rak([pencacah[0],pencacah[1]])
					self.set_rak_saja(pencacah[0])
					print("Rak baru berhasil ditambahkan \n")
					print("Nama: {}".format(pencacah[0]))
					print("Jenis: {}".format(pencacah[1]))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					x = "Rak baru berhasil ditambahkan \n \nNama: {}\nJenis: {}".format(pencacah[0],pencacah[1])
					library.add_rak(pencacah[0],pencacah[1])
				elif pencacah[1] == "Misteri":
					library.set_rak([pencacah[0],pencacah[1]])
					self.set_rak_saja(pencacah[0])
					print("Rak baru berhasil ditambahkan \n")
					print("Nama: {}".format(pencacah[0]))
					print("Jenis: {}".format(pencacah[1]))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					x = "Rak baru berhasil ditambahkan \n \nNama: {}\nJenis: {}".format(pencacah[0],pencacah[1])
					library.add_rak(pencacah[0],pencacah[1])
				elif pencacah[1] == "Compendium":
					library.set_rak([pencacah[0],pencacah[1]])
					self.set_rak_saja(pencacah[0])
					print("Rak baru berhasil ditambahkan \n")
					print("Nama: {}".format(pencacah[0]))
					print("Jenis: {}".format(pencacah[1]))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					x = "Rak baru berhasil ditambahkan \n \nNama: {}\nJenis: {}".format(pencacah[0],pencacah[1])
					library.add_rak(pencacah[0],pencacah[1])
				else:
					Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
					print("Tidak dapat menambahkan Rak dengan jenis {}".format(pencacah[1]))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					
					x = "Tidak dapat menambahkan \nRak dengan jenis {}".format(pencacah[1])
		Label(window, text=x, font=("Comic Sans MS", 15)).pack()
		window.wm_geometry("300x300")

class add_buku(Frame):
	# Constructor __init__ untuk class add_buku
	def __init__(self, master, controller):
		self.controller = controller
		self.master = master  
		Frame.__init__(self, master)
		self.make_widget()

		# mengambil data rak dari class library() dengan method get_kumpulan_rak()
		self.data_rak = library.get_kumpulan_rak()

	# Method add widget
	def make_widget(self):
		# Membuat Frame
		self.frame_TOP = Frame(self)
		self.frame_TOP.grid(row=0, sticky=W)

		# Kumpulan Button, Entry, dan Label

		# Navigasi
		# Jika Buton ditekan akan mengarahkan pada halaman add rak
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="HOME", command=lambda: self.controller.show_frame("Home"), relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=0)
		# lambda: self.controller.show_frame adalah perintah untuk menjalankan method showfrane 
		Button(self.frame_TOP, text="ADD RAK",command=lambda: self.controller.show_frame("add_rak"),relief=FLAT,fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=1)
		# Jika Button ditekan akan mengarahkan pada halaman add buku
		Button(self.frame_TOP, text="ADD BUKU", command=None, bg="#F6D12E",fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=2)
		# Jika ditekan akan menjalankan method list_buku()
		Button(self.frame_TOP, text="LIST", command=list_buku, relief=FLAT, fg="black", font=("Comic Sans MS", 10)).grid(row=0, column=3)

		# Label
		Label(self, text="Tambahkan Buku", font=("Metropolis Black", 20)).grid(row=1,column=0, columnspan=2, pady=20, padx=60)
		Label(self, text="NAMA RAK	").grid(row=2, sticky=W, padx=20)
		Label(self, text="NAMA BUKU	").grid(row=3, sticky=W, padx=20)
		Label(self, text="TAHUN TERBIT	").grid(row=4, sticky=W, padx=20)
		Label(self, text="PENGARANG	").grid(row=5, sticky=W, padx=20)
		Label(self, text="PENERBIT	").grid(row=6, sticky=W, padx=20)
		Label(self, text="JENIS BUKU	").grid(row=7, sticky=W, padx=20)
		Label(self, text="ATRIBUT	").grid(row=8, sticky=W, padx=20)
		Label(self, text="").grid(row=9, sticky=W, padx=0)


		# Entry
		self.nama_rak = StringVar()
		self.nama_buku = StringVar()
		self.tahun_terbit = StringVar()
		self.pengarang_buku = StringVar()
		self.penerbit = StringVar()
		self.jenis_buku = StringVar()
		self.atribut = StringVar()
	
		self.e1 = Entry(self, width="30", textvariable=self.nama_rak).grid(row=2, column=0, sticky=E, padx=0)
		self.e2 = Entry(self, width="30", textvariable=self.nama_buku).grid(row=3, column=0, sticky=E, padx=0)
		self.e3 = Entry(self, width="30", textvariable=self.tahun_terbit).grid(row=4, column=0, sticky=E, padx=0)
		self.e4 = Entry(self, width="30", textvariable=self.pengarang_buku).grid(row=5, column=0, sticky=E, padx=0)
		self.e5 = Entry(self, width="30", textvariable=self.penerbit).grid(row=6, column=0, sticky=E, padx=0)
		self.e6 = Entry(self, width="30", textvariable=self.jenis_buku).grid(row=7, column=0, sticky=E, padx=0)
		self.e7 = Entry(self, width="30", textvariable=self.atribut).grid(row=8, column=0, sticky=E, padx=0)

		# Button
		Button(self, text="TAMBAHKAN", command=self.penampung_add_buku, relief=FLAT, font=("Comic Sans MS", 10), bg="#B81D13", fg="white").grid(row=10, column=0, sticky=E, padx=20, pady=20)
	# Method Penampung_add_buku()
	def penampung_add_buku(self):
		window = Toplevel(self.controller)
		window.geometry("300x300")

		# apabila user mengosongi
		if self.nama_rak.get() + self.nama_buku.get() + self.tahun_terbit.get() + self.pengarang_buku.get() + self.penerbit.get() + self.jenis_buku.get() + self.atribut.get() == "":
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n perintah tidak valid").pack()
			print("perintah tidak valid")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")			
		
		elif self.nama_rak.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.nama_buku.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.tahun_terbit.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.pengarang_buku.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.penerbit.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.jenis_buku.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")
		elif self.atribut.get() == "" :
			Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
			Label(window, text="\n Buku gagal ditambahkan : (").pack()
			print("Buku gagal ditambahkan : (")
			print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			window.geometry("300x300")

			# apabila user mengisi semua masukkan
		else:
			# membuat objek rak dengan memanggil objek library dengan method get_rak untuk mengambil rak
			rak = library.get_rak()

			# mengambil input dari entry
			pencacah = self.nama_rak.get() + " " + self.nama_buku.get() + " " + self.tahun_terbit.get() + " " + self.pengarang_buku.get() + " " + self.penerbit.get() + " " + self.jenis_buku.get() + " " + self.atribut.get()
			
			# membuat input tadi menjadi list
			pencacah = pencacah.split(" ")

			# Mengatur nama elemen list dalam variabel agar mudah untuk diolah
			nama_rak = pencacah[0]
			nama_buku = pencacah[1]
			tahun_terbit = pencacah[2]
			pengarang_buku = pencacah[3]
			penerbit = pencacah[4]
			jenis_buku = pencacah[5]
			atribut = pencacah[6]

            # Mengecek apakah rak sudah ada
			for i in range(len(rak)):
				if rak[i][0] == nama_rak:
					x = i
					break
				else:
					x = -63
			
			# Apabila rak tidak ada
			if x == -63:
				Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
				Label(window, text="\nBuku gagal ditambahkan :(").pack()
				print("Buku gagal ditambahkan : (")
				print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
			# Apabila rak sudah ada
			else:

				# mengecek kebenaran jenis
				jenis = ["Fiksi","Referensi","Ensiklopedia"]
				if not (jenis_buku in jenis):
					Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
					Label(window, text="\nBuku tidak dapat ditambahkan :( ").pack()
					print("Buku tidak dapat ditambahkan : (")
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
				
				# mengecek apakah buku sudah ada
				elif nama_buku in library.get_buku():
					Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
					Label(window, text="\nBuku dengan nama {} \nsudah ada di dalam sistem".format(nama_buku)).pack()
					print("Buku dengan nama {} \nsudah ada di dalam sistem".format(nama_buku))
					print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")

				else:

					# mwncocokan jenis buku agar buku bisa dimasukkan ke rak yang benar
					keterangan = "Buku baru berhasil ditambahkan \npada rak {} \n".format(nama_rak)
					if jenis_buku == "Fiksi":
						if (rak[x][1] == "Compendium"):
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku
							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")

						elif (rak[x][1] == "Misteri"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						elif (rak[x][1] =="Dunia"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						else:
							Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
							Label(window, text="\nBuku Gagal Ditambahkan : (").pack()
							print("Buku Gagal Ditambahkan : {")
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					elif jenis_buku == "Referensi":
						if (rak[x][1] == "Compendium"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						elif (rak[x][1] =="Pengetahuan") :
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						elif (rak[x][1] =="Misteri"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						else:
							Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
							Label(window, text="\nBuku Gagal Ditambahkan : (").pack()
							print("Buku gagal ditambahkan : {")
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
					elif jenis_buku == "Ensiklopedia":
						if (rak[x][1] == "Compendium"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						elif (rak[x][1] =="Pengetahuan"):
							
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							
							# Memanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)

							# untuk mendapatkan deskripsi buku

							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						elif (rak[x][1] =="Dunia"):
							# menambahkan nama buku ke dalam list buku
							library.set_buku(nama_buku)
							# emanggil objek library beserta objek add_buku dan memasukkan segala variabel untuk parameter
							deskripsi = library.add_buku(nama_buku, nama_rak, tahun_terbit, pengarang_buku, penerbit, jenis_buku, atribut)
							# untuk mendapatkan deskripsi buku
							Label(window, text=keterangan, font=("Metropolis Extra Bold", 12)).pack()
							Label(window, text=deskripsi, font=("Comic Sans MS", 10)).pack()
							print("Buku baru berhasil ditambahkan pada rak {} \n".format(nama_rak))
							print(deskripsi)
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
						else:
							Label(window, text="\nERROR", font=("Metropolis Black", 15)).pack()
							Label(window, text="\nBuku Gagal Ditambahkan : (").pack()
							print("Buku gagal ditambahkan : (")
							print("\nSelamat datang di The Great Library\nSilakan masukkan perintah")
if __name__ == '__main__':
	app = Underground()
	app.title('The Great Library')		# memberi judul
	app.wm_geometry("400x340")			# mengatur luas
	app.configure(bg ="#CB0B0B")		# mengatur warna backgrund
	app.mainloop()

print("Selesai, sistem dimatikan")