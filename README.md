# Chat Ting Ting - User Manual

> **Office Edition:** Automated Distribution of Payslips, Announcements & Spreadsheets for Staff and Employees

---

## I. Purpose & Scope

### 1. Purpose
**Chat Ting Ting** is an automation utility designed for Human Resources (HR), Payroll Accountants, Trade Unions, and Administrative Departments. It streamlines the mass distribution of personalized documents and announcements via Zalo with high precision, speed, and privacy.

### 2. Supported Scenarios
* **Periodic Payslips:** Automatically send personalized payslip images (captured directly from Excel) ensuring private and confidential compensation details for each employee.
* **Administrative Notices & Shift Schedules:** Broadcast formatted messages regarding working hours, shifts, attendance exceptions, and internal memos.
* **Document & Decision Attachments (PDF, Excel):** Dispatch individual attachments such as personal income tax statements, official appointments, or confirmation forms.

---

## II. Excel Template Design Principles (Data Preparation)

To ensure seamless automation, the workbook should be organized into two distinct worksheets:

1. **Sheet 1: `DanhSach` (Master Data Sheet)**
   * Contains the complete staff database.
   * Column A: Sequence index / Row ID (1, 2, 3...).
   * Column B: Full Name.
   * Column C: Zalo Recipient Identifier / Nickname.
   * Following Columns: Working days, Base salary, Allowances, Bonuses, Deductions, Net pay, etc.
2. **Sheet 2: `PhieuLuong` (Individual Payslip Template)**
   * Cleanly formatted as a printable receipt (with organizational headers, detailed earning items, and sign-off blocks).
3. **Index-Driven Dynamic Formula (`VLOOKUP` / `INDEX-MATCH` / `XLOOKUP`)**
   * On the `PhieuLuong` sheet, designate a specific cell as the **Index Selector** (e.g., cell `$C$2`).
   * All employee metadata and payment details on the template must dynamically look up data from `DanhSach` based on `$C$2`.
   * When `$C$2` increments from `1` to `2`, the entire payslip view immediately switches from Employee #1 to Employee #2.

---

## III. Step-by-Step Operation Guide

### Step 1: Connect Software to Excel (Mapping)
Keep the target Excel workbook open on your workstation.

1. **Declare File Chat:** Click `File chat` on the app interface. The application will automatically bind to the active Excel workbook.
2. **Assign Recipient Cell:** In Excel, select the cell containing the employee's Zalo contact identifier (on sheet `PhieuLuong`). Return to the application and click `Ô người nhận` (e.g., `Phiếu lương!$H$8`).
3. **Assign Index Cell:** Select the sequence/index control cell on sheet `PhieuLuong`. Return to the app and click `Ô nhảy số` (e.g., `Phiếu lương!$H$4`).
4. **Assign Visual Capture Range:** Select the entire payslip table area to be captured as an image. Return to the app and click `Vùng nội dung chat (hình)`.
5. **Assign Text Message (Optional):** To attach a friendly greeting (e.g., *"Dear Colleague, please find your monthly salary statement attached..."*), select the text cell and click `Vùng nội dung chat (text)`.
6. **Assign Row-Hiding Range & Keywords (Optional):** If the template contains zero or blank line items (e.g., *Bonus = 0*, *Deduction = Blank*), select the target range and specify keywords (e.g., `0; -; Blank; None`) to automatically collapse those rows prior to image capture.
7. **Assign File Attachment (Optional):** If sending individualized attachments, select the cell containing the local file path.

### Step 2: Save and Reload Configurations
* **Save Settings:** After completing Step 1, click `Lưu cài đặt`. The mapping configuration will be stored inside a hidden sheet named `ChatTingTingConfig` within the workbook.
* **Reload Settings Next Month:** For subsequent payroll cycles, simply open the workbook and click `Nạp cài đặt` to restore all mappings instantly.

### Step 3: Configure Parameters and Run
1. **Set Employee Range:** In the `Từ` (From) and `Tới` (To) fields, enter the sequence interval (e.g., from `1` to `150`).
2. **Safe Delay Interval:** Configure an interval between `4 - 8 seconds` to maintain safe sending velocity and prevent throttling.
3. **Check Connection Status:** Monitor the right-hand Log panel. Once it outputs `Zalo sẵn sàng.` (Zalo ready), the large green `Chat` button will become active.
4. **Launch Dispatch:** Click `Chat`. The automated dispatch routine will begin.

---

## IV. Troubleshooting Common Issues

| Issue / Log Message | Underlying Cause | Corrective Action |
| :--- | :--- | :--- |
| **`"Nick rỗng"`** | The recipient cell is blank or the employee lacks a valid Zalo identifier. | Review the roster row in Excel and populate the correct contact details. |
| **`"Không có hình / text / file để gửi"`** | The capture range is unselected or the formula yields an empty template. | Click `Nạp cài đặt` to verify ranges; ensure formulas compute valid data. |
| **`"Lỗi start_chat..."`** | Excel is trapped in In-Cell Edit Mode (cursor blinking inside an active cell). | Click on the Excel window and hit `Esc` or `Enter` to exit cell editing, then re-trigger. |
| **Zalo fails to open / `"Chưa login"`** | Background browser initialization pending or session expired. | Bring up the helper window and scan the QR code via mobile Zalo to authenticate. |
| **Payslip image truncated or misaligned** | Column width is too narrow or text wrapped poorly. | Adjust column widths in Excel or utilize the `Vùng dãn dòng` (AutoFit) feature before capture. |

---

## V. Data Security & Operational Policies

* **Zero-Interference Rule:** While the program is actively iterating rows and taking screen captures, **do not** type, move the mouse, or use clipboard copy/paste actions on the workstation.
* **Income Privacy Protection:** Under current platform mechanisms, messages are delivered via Zalo profile handles. You can send a generalized alert notice and attach a **password-protected PDF** dedicated to that recipient. Even if a misdirection occurs, compensation data remains secure. *(Bulk password-protected PDF generation is available via Excel Cappy).*
* **Emergency Halt:** If an error is spotted in the master payroll data, click `Dừng chat` immediately. The tool will safely complete the current recipient before halting.
* **Dry-Run Validation:** Prior to mass distribution (e.g., 500 recipients), always run a test pass from row `1` to `3` directed to the administrator's profile to verify visual clarity and layout.