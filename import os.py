import os

# Yeh jadoo wali line pata lagayegi ki aapki script exactly kis folder mein hai
folder_address = os.path.dirname(os.path.abspath(__file__))
file_address = os.path.join(folder_address, "tracker_file.txt")

# File banai aur usme kuch likha
with open(file_address, "w") as file:
    file.write("Main yahan chhipi thi!")

# Screen par exact address print karwaya
print(f"✅ MIL GAYI! Aapki file exact is location par hai:\n{file_address}")