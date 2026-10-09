import tkinter as tk

class HoverTooltip:
    """
    Hiển thị khung chú thích (tooltip) bóng mượt khi người dùng rê chuột vào một widget cụ thể.
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.id = None
        
        # Bắt sự kiện rê chuột vào và ra
        self.widget.bind("<Enter>", self.schedule_show)
        self.widget.bind("<Leave>", self.hide_tooltip)
        self.widget.bind("<ButtonPress>", self.hide_tooltip)

    def schedule_show(self, event=None):
        self.unschedule()
        # Đợi 400ms mới hiện tooltip để tạo cảm giác mượt mà, không bị chớp khi lướt chuột ngang qua
        self.id = self.widget.after(400, self.show_tooltip)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show_tooltip(self, event=None):
        self.unschedule()
        if not self.text:
            return
            
        # Tính toán vị trí chuột / widget
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        # Tạo cửa sổ Toplevel nổi
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Ẩn thanh tiêu đề
        tw.wm_attributes("-topmost", True) # Luôn nằm trên các cửa sổ khác
        
        # Đặt vị trí
        tw.wm_geometry(f"+{x}+{y}")
        
        # Thiết kế giao diện Tooltip
        frame = tk.Frame(tw, background="#333333", borderwidth=0)
        frame.pack(ipadx=2, ipady=2)
        
        label = tk.Label(
            frame, 
            text=self.text, 
            justify="left",
            background="#333333", 
            foreground="#FFFFFF",
            relief="flat", 
            borderwidth=0,
            font=("Segoe UI", 9),
            padx=8,
            pady=8
        )
        label.pack()

    def hide_tooltip(self, event=None):
        self.unschedule()
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
