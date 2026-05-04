import tkinter as tk
from tkinter import messagebox  # Thêm để dùng popup
from datetime import datetime  # Thêm để lấy thời gian

def xu_ly_du_lieu():
    # 1. Lấy dữ liệu
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # 2. Lấy thời gian hiện tại
    thoi_gian = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    
    # 3. In ra Terminal (kèm thời gian)
    print(f"[{thoi_gian}] MSSV: {mssv} - Họ tên: {ho_ten}")
    
    # 4. Kiểm tra dữ liệu
    
    # ❌ MSSV không phải số
    if not mssv.isdigit():
        messagebox.showerror("Lỗi", "MSSV phải là số!")  # Popup lỗi
        return
    
    # ❌ Họ tên rỗng
    if ho_ten.strip() == "":
        messagebox.showerror("Lỗi", "Không được để trống họ tên!")
        return
    
    # ✅ Hợp lệ
    nhan_ket_qua.config(
        text=f"Chào sinh viên: {ho_ten} ({mssv})",
        fg="blue"
    )
    
    # 5. Xóa trắng ô nhập sau khi thành công
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()