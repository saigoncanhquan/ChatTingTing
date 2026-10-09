# Hướng Dẫn Sử Dụng Phần Mềm Chat Ting Ting

> **Phiên bản Văn phòng:** Nghiệp vụ Gửi Phiếu Lương, Thông Báo & Bảng Biểu Cho Cán Bộ, Công Nhân Viên

---

## I. Mục Đích & Phạm Vi Áp Dụng

### 1. Mục đích nghiệp vụ
**Chat Ting Ting** là công cụ tự động hóa hỗ trợ bộ phận Hành chính - Nhân sự (HR), Kế toán tiền lương, Ban chấp hành Công đoàn và Văn phòng cơ quan giải quyết bài toán phân phối dữ liệu cá nhân hóa số lượng lớn qua Zalo một cách nhanh chóng, chuẩn xác và bảo mật thông tin.

### 2. Phạm vi tài liệu và biểu mẫu áp dụng
Tài liệu này áp dụng cho các nghiệp vụ nội bộ phổ biến bao gồm:
* **Phiếu báo lương từng kỳ:** Gửi hình ảnh phiếu lương chi tiết từng nhân viên (chụp trực tiếp từ bảng tính lương) đảm bảo tính riêng tư, bảo mật thông tin thu nhập của từng cá nhân.
* **Thông báo công văn, chấm công, ca kíp:** Gửi nội dung tin nhắn văn bản thông báo ngày công, lịch trực, vi phạm chấm công, thông tin họp nội bộ.
* **Đính kèm bảng biểu, quyết định (File PDF, Excel):** Tự động gửi kèm thông báo thuế TNCN, quyết định bổ nhiệm, biểu mẫu xác nhận đến từng cán bộ công nhân viên (CBCNV).

---

## II. Nguyên Tắc Thiết Kế File Excel Mẫu (Chuẩn Bị Dữ Liệu)

Trước khi vận hành phần mềm, file Excel lương/thông báo của cơ quan, đơn vị nên được bố cục thành 2 trang tính (sheet):

1. **Sheet 1: `DanhSach` (Bảng tổng hợp dữ liệu)**
   * Chứa toàn bộ danh sách CBCNV.
   * Cột A: Số thứ tự (1, 2, 3...).
   * Cột B: Họ và tên.
   * Cột C: Tên Nick / Số Zalo.
   * Các cột tiếp theo: Ngày công, Lương cơ bản, Phụ cấp, Thưởng, Giảm trừ, Thực lĩnh...
2. **Sheet 2: `PhieuLuong` (Biểu mẫu hiển thị cá nhân)**
   * Được thiết kế, định dạng đẹp mắt như một mẫu phiếu in thực tế (có logo, tiêu đề đơn vị, bảng kê chi tiết khoản mục).
3. **Cơ chế Ô Nhảy Số (`VLOOKUP` / `INDEX-MATCH` / `XLOOKUP`)**
   * Tại sheet `PhieuLuong`, chỉ định một ô làm **Ô Số Thứ Tự** (ví dụ ô `$C$2`).
   * Toàn bộ dữ liệu họ tên, phòng ban, tiền lương trên phiếu sẽ sử dụng công thức dò tìm tham chiếu vào ô `$C$2` này.
   * Khi ô `$C$2` đổi giá trị từ `1` sang `2`, toàn bộ dữ liệu trên phiếu lương sẽ tự động chuyển từ Nhân viên 1 sang Nhân viên 2.

---

## III. Các Bước Vận Hành Trên Chat Ting Ting

### Bước 1: Kết nối phần mềm với bảng tính Excel (Mapping)
Mở sẵn file Excel chứa bảng tính cần gửi trên máy tính.

1. **Khai báo File chat:** Nhấn nút `File chat` trên giao diện phần mềm. Hệ thống sẽ tự động nhận diện tên file Excel đang hoạt động.
2. **Gán Ô người nhận:** Trên Excel, chọn ô chứa Tên / Nick Zalo của nhân viên (tại sheet `PhieuLuong`). Quay lại phần mềm nhấn nút `Ô người nhận` (địa chỉ ô sẽ tự nạp, ví dụ: `Phiếu lương!$H$8`).
3. **Gán Ô nhảy số:** Nhấp chọn ô STT điều khiển công thức dò tìm trên sheet `PhieuLuong`. Quay lại phần mềm bấm `Ô nhảy số` (ví dụ: `Phiếu lương!$H$4`).
4. **Gán Vùng nội dung chat (hình ảnh phiếu lương):** Quét chọn toàn bộ khung phiếu lương cần gửi (từ tiêu đề đến chân trang). Quay lại bấm `Vùng nội dung chat (hình)`.
5. **Gán Lời chào văn bản (Tùy chọn):** Nếu muốn gửi kèm tin nhắn chữ (ví dụ: *"Chào anh/chị, phòng Kế toán xin gửi thông báo lương tháng..."*), chọn ô chứa lời chào rồi bấm `Vùng nội dung chat (text)`.
6. **Gán Vùng ẩn dòng & Từ vựng (Tùy chọn):** Nếu phiếu có dòng khoản mục bằng 0 hoặc rỗng (như *Thưởng = 0*, *Kỷ luật = Trống*), chọn vùng này và nhập từ khóa (ví dụ: `0; -; Trống; Hủy`) để phần mềm tự giấu dòng đó trước khi chụp ảnh.
7. **Gán File đính kèm (Tùy chọn):** Nếu gửi kèm file văn bản/quyết định riêng, chọn ô chứa đường dẫn file trên máy tính.

### Bước 2: Lưu và nạp cấu hình nhanh cho các kỳ sau
* **Lưu cấu hình:** Sau khi kết nối xong Bước 1, nhấn nút `Lưu cài đặt`. Cấu hình được lưu vào một trang tính ẩn mang tên `ChatTingTingConfig` trong chính file Excel đó.
* **Nạp cấu hình kỳ sau:** Vào các kỳ tiếp theo, bạn chỉ cần mở file Excel và bấm nút `Nạp cài đặt`, không cần gán lại địa chỉ các ô.

### Bước 3: Thiết lập tham số và tiến hành gửi
1. **Thiết lập dải gửi:** Tại mục `Từ` và `Tới`, nhập số thứ tự nhân viên cần gửi (ví dụ: Từ `1` tới `150`).
2. **Khoảng nghỉ an toàn (Khuyến nghị):** Đặt thời gian nghỉ ngẫu nhiên từ `4 - 8 giây` để đảm bảo lưu lượng gửi an toàn, tránh vi phạm chính sách gửi tin dồn dập.
3. **Kiểm tra trạng thái Zalo:** Quan sát khung Nhật ký bên phải. Khi xuất hiện thông báo `Zalo sẵn sàng.`, nút `Chat` lớn màu xanh sẽ sáng lên.
4. **Bắt đầu gửi:** Nhấn nút `Chat`. Tiến trình gửi sẽ diễn ra hoàn toàn tự động.

---

## IV. Xử Lý Các Tình Huống Thường Gặp (Troubleshooting)

| Hiện tượng / Thông báo | Nguyên nhân thực tế | Biện pháp xử lý của nhân sự / kế toán |
| :--- | :--- | :--- |
| **Nhật ký báo: `"Nick rỗng"`** | Ô người nhận tại dòng đó bị bỏ trống hoặc người nhận chưa có nick Zalo. | Kiểm tra lại danh sách nhân sự tại dòng đó, bổ sung thông tin chính xác. |
| **Nhật ký báo: `"Không có hình / text / file để gửi"`** | Chưa chọn vùng in phiếu lương hoặc công thức Excel đang trả về kết quả rỗng. | Bấm `Nạp cài đặt` để kiểm tra vùng chọn; rà soát công thức Excel xem có bị lỗi hiển thị không. |
| **Phần mềm báo: `"Lỗi start_chat..."`** | Người dùng đang nhấp đúp chuột vào ô tính khiến Excel rơi vào chế độ chỉnh sửa (Edit Mode). | Nhấp vào Excel và bấm phím `Esc` hoặc `Enter` để thoát chế độ sửa ô, sau đó thao tác lại trên phần mềm. |
| **Zalo không mở hoặc báo `"Chưa login"`** | Trình duyệt phụ trợ chưa khởi động xong hoặc phiên đăng nhập Zalo đã hết hạn. | Mở giao diện nền, sử dụng ứng dụng Zalo trên điện thoại quét mã QR để đăng nhập. |
| **Hình phiếu lương bị mờ / lệch chữ** | Cột Excel quá hẹp hoặc dữ liệu tràn ô. | Chỉnh độ rộng cột Excel hoặc dùng tính năng `Vùng dãn dòng` để phần mềm tự động AutoFit trước khi chụp. |

---

## V. Quy Định An Toàn Dữ Liệu & Lưu Ý Bảo Mật Nội Bộ

* **Nguyên tắc không can thiệp:** Trong suốt quá trình phần mềm đang điều khiển Excel nhảy số và chụp ảnh, **tuyệt đối không** thao tác chuột, gõ phím hay sao chép (copy/paste) tác vụ khác trên máy tính để tránh làm sai lệch dữ liệu chụp màn hình.
* **Bảo mật thông tin thu nhập:** Do cơ chế của Zalo, phần mềm thực hiện gửi đích danh theo Nick Zalo. Bạn có thể gửi thông báo chung *"CÓ LƯƠNG VỀ"* bằng tin nhắn/hình ảnh, đồng thời đính kèm file PDF có đặt mật khẩu riêng cho từng người. Cách này đảm bảo kể cả khi gửi nhầm nick cũng không bị lộ thông tin thu nhập. *(Chức năng tạo hàng loạt file PDF có mật khẩu được hỗ trợ qua tiện ích Excel Cappy).*
* **Dừng gửi khẩn cấp:** Nếu phát hiện sai lệch số liệu bảng lương tổng, bấm ngay nút `Dừng chat`. Hệ thống sẽ hoàn thành nốt nhân viên hiện tại rồi dừng lại để bạn chỉnh sửa file.
* **Kiểm tra thử nghiệm (Dry-Run):** Trước khi phát lệnh cho toàn thể cơ quan (ví dụ: 500 người), luôn thực hiện gửi thử từ dòng `1` đến `3` cho chính tài khoản của cán bộ quản trị để kiểm tra độ nét và bố cục.