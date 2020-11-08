#1. Pengalaman saya dalam bahasa pemograman python bisa dibilang cukup lama, saya mengenal python sekitar dua tahun yang lalu
#   namun kemampuan saya masih ditingkat dasar karena tidak terlalu sering berlatih sejak awal. saya belajar python secara otodidak
#   melalui chanel youtube dan beberapa blog. Belajar secara otodidak membuat saya bingung karena tidak ada kurikulum atau
#   struktur yang lebih mudah untuk belajar python sehingga pengetahuan saya mengenai python kurang terstuktur dan masih dasar.
#2. Saya berharap kedepannya ada kelas python unutk web developer karena pekerjaan sebagai web developer juga banyak dibutuhkan.
#3. 
class manipulasi:
    def __init__(self,data):
        self.data = data
        
    def soal_a(self):
        print(self.data.capitalize())
        
    def soal_b(self):
        print(self.data.lower())
        
    def soal_c(self):
        print(self.data.upper())
        
    def soal_d(self):
        print(self.data.split())

data = manipulasi('saya tinggal di Indonesia')

data.soal_a()
data.soal_b()
data.soal_c()
data.soal_d()