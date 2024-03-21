import tkinter as tk
from tkinter import messagebox
import random

class MastermindGame:
    def __init__(self, master):
        # Inisialisasi permainan dengan jendela utama (master)
        self.master = master
        self.master.title("Mastermind Game")
        self.master.geometry("400x350")

        # Dictionary untuk memetakan nomor warna ke namanya
        self.colors = {
            1: "Merah", 2: "Putih", 3: "Hitam", 4: "Kuning",
            5: "Hijau", 6: "Biru", 7: "Coklat", 8: "Ungu",
            9: "Pink", 10: "Cyan"
        }

        # Menghasilkan kode rahasia acak dengan 4 warna
        self.secret_code = [random.randint(1, 10) for _ in range(4)]
        
        # Jumlah percobaan yang diperbolehkan dan nilai percobaan saat ini
        self.attempts_left = 5
        self.current_attempt = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]

        # Menyiapkan GUI
        self.create_gui()

    def create_gui(self):
        # Membuat komponen GUI permainan
        self.create_guess_row()
        self.create_input_rows()
        self.create_feedback_area()

    def create_guess_row(self):
        # Membuat baris tempat warna yang ditebak akan ditampilkan
        guess_frame = tk.Frame(self.master)
        guess_frame.pack(pady=10)

        # Label untuk mewakili setiap warna yang ditebak
        self.guess_labels = []
        for i in range(4):
            label = tk.Label(guess_frame, text="?", width=5, height=2, bg="lightgray", relief="solid")
            self.guess_labels.append(label)
            label.grid(row=0, column=i, padx=5)

    def create_input_rows(self):
        # Membuat baris untuk input pengguna (menebak)
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=5)

        # Widget Entry untuk memasukkan warna, dan tombol untuk mengirimkan tebakan
        for i in range(4):
            entry = tk.Entry(input_frame, textvariable=self.current_attempt[i], width=5)
            entry.grid(row=0, column=i, padx=5)

        guess_button = tk.Button(input_frame, text="Tebak", command=self.check_guess)
        guess_button.grid(row=0, column=4, padx=5)

    def create_feedback_area(self):
        # Membuat area untuk menampilkan umpan balik, kesempatan tersisa, dan informasi warna
        feedback_frame = tk.Frame(self.master)
        feedback_frame.pack(pady=10)

        # Label untuk umpan balik, kesempatan tersisa, dan informasi warna
        self.feedback_label = tk.Label(feedback_frame, text="Umpan Balik: ")
        self.feedback_label.pack()

        self.chances_label = tk.Label(feedback_frame, text=f"Kesempatan: {self.attempts_left}")
        self.chances_label.pack()

        info_label_1 = tk.Label(feedback_frame, text="1=Merah, 2=Putih, 3=Hitam, 4=Kuning, 5=Hijau,")
        info_label_1.pack()

        info_label_2 = tk.Label(feedback_frame, text="6=Biru, 7=Coklat, 8=Ungu, 9=Pink, 10=Cyan")
        info_label_2.pack()

    def check_guess(self):
        # Memeriksa tebakan pengguna terhadap kode rahasia
        guess = [var.get() for var in self.current_attempt]
        correct_positions = sum([1 for i in range(4) if guess[i] == self.secret_code[i]])
        
        # Memeriksa apakah semua posisi benar, jika ya, akhiri permainan
        if correct_positions == 4:
            self.end_game("100% benar. Anda berhasil menebak semua warna.")
        else:
            # Mengurangi percobaan dan memperbarui GUI
            self.attempts_left -= 1
            if self.attempts_left == 0:
                # Jika tidak ada percobaan lagi, akhiri permainan
                self.end_game("Anda kehabisan kesempatan. Game direset.")
            else:
                # Memperbarui warna yang ditebak, umpan balik, dan kesempatan tersisa
                self.update_guess_labels(guess, correct_positions)
                self.update_feedback(correct_positions)
                self.update_chances()

    def update_guess_labels(self, guess, correct_positions):
        # Memperbarui warna yang ditebak berdasarkan posisi yang benar
        for i, label in enumerate(self.guess_labels):
            if guess[i] == self.secret_code[i]:
                label.config(text=self.colors[guess[i]], bg="lightgray")
            elif guess[i] in self.secret_code:
                label.config(text="?", bg="white")
            else:
                label.config(text="?", bg="lightgray")

    def update_feedback(self, correct_positions):
        # Memperbarui label umpan balik berdasarkan jumlah posisi yang benar
        percentage = (correct_positions / 4) * 100
        self.feedback_label.config(text=f"{correct_positions} warna benar. Coba lagi!")

    def update_chances(self):
        # Memperbarui label kesempatan tersisa
        self.chances_label.config(text=f"Kesempatan: {self.attempts_left}")

    def end_game(self, message):
        # Mengakhiri permainan dan menampilkan kotak pesan dengan kode yang benar
        correct_code = [self.colors[color] for color in self.secret_code]
        messagebox.showinfo("Game Over", f"{message}\nJawaban yang benar: {correct_code}")
        self.reset_game()

    def reset_game(self):
        # Mereset permainan dengan menghasilkan kode rahasia baru dan mereset percobaan
        self.secret_code = [random.randint(1, 10) for _ in range(4)]
        self.attempts_left = 5

        # Mereset elemen GUI
        for label in self.guess_labels:
            label.config(text="?", bg="lightgray")

        self.feedback_label.config(text="Umpan Balik: ")
        self.chances_label.config(text=f"Kesempatan: {self.attempts_left}")

        for var in self.current_attempt:
            var.set(0)

if __name__ == "__main__":
    # Membuat jendela utama dan memulai permainan
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()
