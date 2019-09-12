ListGPA = [2.1,2.5,4,3]

def hadiah (GPA):
    bonus = 500000
    hadiah = GPA*bonus
    return hadiah

for GPA in ListGPA:
    if GPA > 2.5:
        print("Selamat anda mendapatkan", hadiah(GPA))
    else :
        print("Maaf anda belum beruntung")