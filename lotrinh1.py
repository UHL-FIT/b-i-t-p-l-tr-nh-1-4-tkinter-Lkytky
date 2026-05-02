import tkinter as tk

# 1. Khởi tạo cửa sổ gốc
root = tk.Tk()
root.title("Trần Minh Hiếu")  
root.geometry("500x500")      # đổi kích thước

# 2. Tạo Label
nhan_chao = tk.Label(root, text="Chào mừng sinh viên Đại học Hạ Long!")
nhan_chao.pack(pady=50)

# 3. Chạy chương trình
root.mainloop()

#Khi tăng kích thước cửa sổ từ 400x200 lên 500x500, dòng chữ chào mừng không thay đổi kích thước mà chỉ có khoảng trống xung quanh tăng lên. Điều này do Label hiển thị theo nội dung và không tự co giãn theo cửa sổ. Dòng chữ vẫn giữ nguyên vị trí tương đối do sử dụng pack với khoảng cách cố định (pady), nên khi cửa sổ lớn hơn thì phần không gian trống cũng tăng theo.