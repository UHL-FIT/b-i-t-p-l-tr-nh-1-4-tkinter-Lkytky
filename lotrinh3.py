import tkinter as tk

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x250")

# 🔹 Đổi sang cột 0 co giãn
root.columnconfigure(0, weight=1)

# 1. Tạo các thành phần
nhan_ma_sv = tk.Label(root, text="Mã sinh viên:")
o_nhap_ma_sv = tk.Entry(root)

nhan_ho_ten = tk.Label(root, text="Họ và tên:")
o_nhap_ho_ten = tk.Entry(root)

# Hàng 0
nhan_ma_sv.grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Hàng 1
nhan_ho_ten.grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

#Khi cho cột nhãn co giãn, các nhãn bị kéo rộng nhưng vẫn dồn về bên trái nên tạo khoảng trống dư thừa, trong khi ô nhập không được mở rộng → giao diện mất cân đối; vì vậy thực tế chỉ nên cho cột chứa ô nhập co giãn để tận dụng không gian hiệu quả.