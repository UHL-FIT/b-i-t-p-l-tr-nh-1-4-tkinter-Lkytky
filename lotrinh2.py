import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
root.geometry("400x300")

# 🔹 Thêm dòng này (đổi nền xám nhạt)
root.configure(bg="#f8f9fa")

# 1. Nhãn tiêu đề với Phông chữ và Màu sắc
nhan_truong = tk.Label(
    root, 
    text="TRƯỜNG ĐẠI HỌC HẠ LONG", 
    font=("Arial", 14, "bold"), 
    fg="white", 
    bg="#0056b3"
)
nhan_truong.pack(fill="x", pady=10)

# 2. Nhãn hiển thị họ tên
nhan_ten = tk.Label(root, text="Họ tên: Nguyễn Văn A", font=("Arial", 12))
nhan_ten.pack(pady=5)

# 3. Nhãn hiển thị MSSV với màu đỏ nổi bật
nhan_msv = tk.Label(root, text="MSSV: 22010001", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)

# 🔹 Thêm dòng khoa (màu xanh lá)
nhan_khoa = tk.Label(
    root,
    text="Khoa: Công nghệ thông tin",
    font=("Arial", 12),
    fg="green"
)
nhan_khoa.pack(pady=5)

# 4. Tạo nút bấm để thoát chương trình (chỉ thêm width, height)
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#dc3545",
    fg="white",
    width=20,
    height=2
)
nut_thoat.pack(pady=20)

root.mainloop()