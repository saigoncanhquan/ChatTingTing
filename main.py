import tkinter as tk
from tkinter import ttk, scrolledtext
import tkinter.font as tkfont
from tooltip import HoverTooltip
from guide_data import TOOLTIP_DATA, README_CONTENT

class ChatTingTingGuideApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Chat Ting Ting - Interactive Visual Guide")
        self.geometry("800x550")
        
        # Nền xám bạc văn phòng
        self.configure(bg="#E0E0E0")
        self.resizable(False, False)
        
        self.init_ui()
        
    def init_ui(self):
        # Thiết lập Font chữ
        self.font_normal = tkfont.Font(family="Segoe UI", size=9)
        self.font_bold = tkfont.Font(family="Segoe UI", size=9, weight="bold")
        self.font_chat = tkfont.Font(family="Segoe UI", size=14, weight="bold")
        
        # Khung chứa chính (chia 2 cột)
        main_frame = tk.Frame(self, bg="#E0E0E0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        left_frame = tk.Frame(main_frame, bg="#E0E0E0")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        right_frame = tk.Frame(main_frame, bg="#E0E0E0")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        # ==================== CỘT TRÁI ====================
        
        # Hàng 1: Nút Chat và Nút Gia Hạn
        row1 = tk.Frame(left_frame, bg="#E0E0E0")
        row1.pack(fill=tk.X, pady=(0, 10))
        
        btn_chat = tk.Button(
            row1, text="Chat >", bg="#1E9E60", fg="white", 
            font=self.font_chat, relief=tk.FLAT, width=12, height=1
        )
        btn_chat.pack(side=tk.LEFT)
        HoverTooltip(btn_chat, TOOLTIP_DATA["btn_chat"])
        
        btn_giahan = tk.Button(
            row1, text="GIA HẠN", bg="#F0F0F0", fg="#333333", 
            font=self.font_normal, relief=tk.RIDGE, bd=2
        )
        btn_giahan.pack(side=tk.RIGHT, anchor="ne")
        
        # Hàng 2: Từ / Tới / Bước
        row2 = tk.Frame(left_frame, bg="#E0E0E0")
        row2.pack(fill=tk.X, pady=5)
        
        tk.Label(row2, text="Từ", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT)
        tk.Entry(row2, width=8, font=self.font_normal).pack(side=tk.LEFT, padx=(5, 10))
        
        tk.Label(row2, text="Tới", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT)
        tk.Entry(row2, width=8, font=self.font_normal).pack(side=tk.LEFT, padx=(5, 10))
        
        tk.Label(row2, text="Bước", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT)
        tk.Entry(row2, width=5, font=self.font_normal).pack(side=tk.LEFT, padx=(5, 0))
        
        # Hàng 3 -> 10: Các trường mapping
        self.create_form_row(left_frame, "File chat", "DanhSachLuong_T10.xlsx")
        
        btn_nick, _ = self.create_form_row(left_frame, "Nick Zalo", "Phiếu lương!$H$8")
        HoverTooltip(btn_nick, TOOLTIP_DATA["btn_nick"])
        
        btn_nhayso, _ = self.create_form_row(left_frame, "Ô nhảy số", "Phiếu lương!$C$2")
        HoverTooltip(btn_nhayso, TOOLTIP_DATA["btn_nhayso"])
        
        # Vùng ẩn dòng + Từ vựng (Row đặc biệt)
        row_andong = tk.Frame(left_frame, bg="#E0E0E0")
        row_andong.pack(fill=tk.X, pady=2)
        btn_andong = tk.Button(row_andong, text="Vùng ẩn dòng", width=16, anchor="w", font=self.font_normal, relief=tk.RAISED, bd=1)
        btn_andong.pack(side=tk.LEFT, padx=(0, 5))
        tk.Entry(row_andong, width=12, font=self.font_normal).pack(side=tk.LEFT)
        
        tk.Label(row_andong, text="Từ vựng", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT, padx=(10, 5))
        tk.Entry(row_andong, font=self.font_normal).pack(side=tk.LEFT, fill=tk.X, expand=True)
        HoverTooltip(btn_andong, TOOLTIP_DATA["btn_andong"])
        
        self.create_form_row(left_frame, "Vùng dãn dòng", "")
        
        btn_vunghinh, _ = self.create_form_row(left_frame, "Vùng ND chat (hình)", "Phiếu lương!$A$1:$H$25")
        HoverTooltip(btn_vunghinh, TOOLTIP_DATA["btn_vunghinh"])
        
        self.create_form_row(left_frame, "Vùng ND chat (text)", "")
        self.create_form_row(left_frame, "File đính kèm", "")
        
        # Khoảng nghỉ
        row_nghi = tk.Frame(left_frame, bg="#E0E0E0")
        row_nghi.pack(fill=tk.X, pady=2)
        tk.Label(row_nghi, text="Khoảng nghỉ", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT, padx=(0, 10))
        entry_nghi = tk.Entry(row_nghi, width=5, font=self.font_normal)
        entry_nghi.insert(0, "4")
        entry_nghi.pack(side=tk.LEFT)
        tk.Label(row_nghi, text="giây", bg="#E0E0E0", font=self.font_normal).pack(side=tk.LEFT, padx=5)
        HoverTooltip(entry_nghi, TOOLTIP_DATA["entry_khoangnghi"])
        
        # Hàng Nút Lưu / Xóa / Nạp
        row_action = tk.Frame(left_frame, bg="#E0E0E0")
        row_action.pack(fill=tk.X, pady=(10, 5))
        
        btn_luu = tk.Button(row_action, text="Lưu cài đặt", font=self.font_normal, relief=tk.RAISED, bd=1, width=12)
        btn_luu.pack(side=tk.LEFT, padx=(0, 5))
        btn_xoa = tk.Button(row_action, text="Xóa", font=self.font_normal, relief=tk.RAISED, bd=1, width=8)
        btn_xoa.pack(side=tk.LEFT, padx=5)
        btn_nap = tk.Button(row_action, text="Nạp cài đặt", font=self.font_normal, relief=tk.RAISED, bd=1, width=12)
        btn_nap.pack(side=tk.LEFT, padx=5)
        
        HoverTooltip(btn_luu, TOOLTIP_DATA["btn_luu_nap"])
        HoverTooltip(btn_nap, TOOLTIP_DATA["btn_luu_nap"])
        
        # Hàng lấy danh bạ và HDSD
        row_bot = tk.Frame(left_frame, bg="#E0E0E0")
        row_bot.pack(fill=tk.X, pady=5)
        
        tk.Button(row_bot, text="Lấy danh bạ Zalo", font=self.font_normal, relief=tk.RAISED, bd=1).pack(side=tk.LEFT)
        
        lbl_guide = tk.Label(row_bot, text="Hướng dẫn sử dụng", fg="blue", cursor="hand2", font=self.font_normal, bg="#E0E0E0")
        lbl_guide.pack(side=tk.RIGHT)
        # Bind sự kiện mở cửa sổ HDSD
        lbl_guide.bind("<Button-1>", lambda e: self.show_guide_window())
        
        # Checkbox always on top
        chk_var = tk.IntVar()
        chk_var.set(1)
        tk.Checkbutton(left_frame, text="Luôn hiện trên đầu", variable=chk_var, bg="#E0E0E0", font=self.font_normal).pack(anchor="w", pady=5)
        
        # Progress bar
        progress = ttk.Progressbar(left_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        progress.pack(fill=tk.X, pady=(5, 0))
        tk.Label(left_frame, text="0%", bg="#E0E0E0", font=self.font_normal).pack(anchor="e")
        
        
        # ==================== CỘT PHẢI (NHẬT KÝ) ====================
        
        # Khung nhật ký giả lập
        log_frame = tk.Frame(right_frame, bg="#E0E0E0")
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(log_frame, text="Nhật ký", bg="#E0E0E0", font=self.font_bold).pack(anchor="w", pady=(0, 5))
        
        log_text = scrolledtext.ScrolledText(
            log_frame, 
            width=40, 
            height=30, 
            font=self.font_normal, 
            bg="#F0F0F0", 
            fg="#000000",
            relief=tk.SUNKEN,
            bd=2
        )
        log_text.pack(fill=tk.BOTH, expand=True)
        
        # Nội dung giả lập theo yêu cầu
        mock_log = (
            "Đã nạp file chat cũ.\n"
            "Khởi động Zalo...\n"
            "Zalo sẵn sàng.\n"
        )
        log_text.insert(tk.END, mock_log)
        log_text.config(state=tk.DISABLED) # Chỉ đọc


    def create_form_row(self, parent, btn_text, default_val=""):
        """Hàm tiện ích tạo 1 dòng gồm 1 Nút bấm và 1 Ô nhập liệu"""
        row = tk.Frame(parent, bg="#E0E0E0")
        row.pack(fill=tk.X, pady=2)
        
        btn = tk.Button(row, text=btn_text, width=16, anchor="w", font=self.font_normal, relief=tk.RAISED, bd=1)
        btn.pack(side=tk.LEFT, padx=(0, 5))
        
        entry = tk.Entry(row, font=self.font_normal)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        if default_val:
            entry.insert(0, default_val)
            
        return btn, entry
        
    def show_guide_window(self):
        """Mở cửa sổ hiển thị Hướng dẫn sử dụng lấy từ file README_VI.md"""
        guide_win = tk.Toplevel(self)
        guide_win.title("Hướng Dẫn Sử Dụng - Chat Ting Ting")
        guide_win.geometry("750x650")
        guide_win.configure(bg="#FFFFFF")
        
        text_widget = scrolledtext.ScrolledText(
            guide_win, 
            wrap=tk.WORD, 
            font=("Segoe UI", 10), 
            padx=15, 
            pady=15,
            bg="#FFFFFF"
        )
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, README_CONTENT)
        text_widget.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = ChatTingTingGuideApp()
    app.mainloop()
