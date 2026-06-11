## AKA-Lab---Git-Safety-Foundation-Before-Vibe-Coding
- **Họ và tên học viên:** Hồ Đình Sơn
- **Trạng thái:** Đã hoàn thành 02 chứng chỉ Microsoft Learn.
- 
## 3. Danh sách lệnh Git đã sử dụng trong dự án
Dưới đây là các lệnh Git cốt lõi em đã thực hành thành thạo dưới máy tính:
- `git clone <url>`: Tải repository từ GitHub về máy cá nhân.
- `git checkout -b <tên_nhánh>`: Tạo nhánh mới và chuyển sang nhánh đó.
- `git checkout <tên_nhánh>`: Chuyển đổi qua lại giữa các nhánh.
- `git add .`: Lưu lại các thay đổi vào khu vực chờ (Staging Area).
- `git commit -m "tin_nhắn"`: Ghi lại lịch sử thay đổi kèm thông điệp có ý nghĩa.
- `git pull origin <tên_nhánh>`: Cập nhật và kéo code mới nhất từ GitHub về máy.
- `git push origin <tên_nhánh>`: Đẩy code và các nhánh từ máy cá nhân lên GitHub.
- `git reset --hard origin/main`: Ép trạng thái code ở máy đồng bộ sạch sẽ với GitHub khi bị kẹt lỗi.
- `git revert <commit_id>`: Hoàn tác an toàn một commit bị lỗi bằng cách tạo ra một commit đảo ngược.
- `git log --oneline`: Xem lịch sử commit rút gọn để quản lý mã nguồn.
## 📌 Khung Kiểm Tra Điều Kiện Hoàn Thành (Checklist)

- **Điều kiện 1:** Hoàn thành các module học tập lý thuyết -> Trạng thái: ✅ Hoàn thành (GitHub Foundations Part 1 & 2 trên Microsoft Learn).
- **Điều kiện 2:** Tạo GitHub repository cá nhân -> Trạng thái: ✅ Hoàn thành (Repository R chính chủ).
- **Điều kiện 3:** Có tối thiểu 10 commit có ý nghĩa -> Trạng thái: ✅ Hoàn thành (Kiểm tra tại mục Commits của Repo).
- **Điều kiện 4:** Có tối thiểu 3 branch thực hành -> Trạng thái: ✅ Hoàn thành (Gồm các nhánh: main, feature-login, feature-about).
- **Điều kiện 5:** Có tối thiểu 2 pull request -> Trạng thái: ✅ Hoàn thành (Kiểm tra tại mục Pull Requests Closed).
- **Điều kiện 6:** Có ít nhất 1 tình huống Conflict -> Trạng thái: ✅ Hoàn thành (Đã xảy ra và xử lý trực tiếp trên file README.md).
- **Điều kiện 7:** Có ít nhất 1 tình huống Rollback/Revert -> Trạng thái: ✅ Hoàn thành (Đã thực hành rollback thông qua hành động xóa file lỗi temp.txt).
- **Điều kiện 8:** Nộp ảnh chụp minh chứng Microsoft Learn -> Trạng thái: ✅ Hoàn thành (Học viên đính kèm ảnh bên dưới).
- **Điều kiện 9:** Mentor xác nhận đạt yêu cầu -> Chờ duyệt -> Chờ đánh giá từ Mentor 

## 📂 Chi Tiết Các Tình Huống Đã Thực Hành

### 1. Thực Hành Xử Lý Conflict (Xung đột)
* **Tình huống:** Sửa đổi file README.md độc lập ở cùng một vị trí trên hai nhánh main và feature-about, dẫn đến xung đột hệ thống khi mở Pull Request #2.
* **Cách giải quyết:** Bấm vào nút "Resolve conflicts" trực tiếp trên Web GitHub, tiến hành xóa bỏ các ký tự báo lỗi của Git (<<<<<<<, =======, >>>>>>>), chọn lọc giữ lại nội dung chính xác cuối cùng và thực hiện Commit merge để hoàn tất gộp nhánh an toàn.

### 2. Thực Hành Rollback / Revert (Hoàn tác)
* **Tình huống:** Giả lập hành động commit nhầm file lỗi hoặc thư mục đệm không cần thiết mang tên temp.txt.
* **Cách giải quyết:** Thực hiện hành động xóa file trực tiếp trên giao diện Web (Delete file). GitHub sẽ tự động tạo ra một commit mới mang tính chất phủ quyết (revert) để dọn dẹp file lỗi, đưa dự án về trạng thái ổn định trước đó mà không làm ảnh hưởng đến lịch sử làm việc.

---

## 🛡️ Nguyên Tắc Bảo Mật & Quy Trình Vibe Code Với AI

### 1. Nguyên tắc bảo mật khi dùng GitHub
* Tuyệt đối không đẩy mật khẩu, API key, hoặc token cá nhân lên môi trường public để tránh rò rỉ dữ liệu.
* Cấu hình và sử dụng file .gitignore ngay từ đầu dự án để tự động loại bỏ các file đệm, thư mục rác hệ thống (như __pycache__/, .env).

### 2. Quy trình sử dụng Git an toàn khi Vibe Code với AI
* **Không sửa đổi trực tiếp trên nhánh main:** Giữ nhánh main luôn là nơi chứa mã nguồn sạch, chạy ổn định và an toàn tuyệt đối.
* **Quản lý nhánh nghiêm ngặt:** Tạo branch độc lập riêng biệt cho từng tính năng hoặc từng thử nghiệm nhỏ trước khi nhờ AI hỗ trợ sinh code.
* **Kiểm tra kỹ lưỡng:** Sau khi AI sinh code, tiến hành đọc hiểu, rà soát lại logic, chạy thử nghiệm ổn định tại local rồi mới thực hiện commit từng bước rõ nghĩa.
* **Hợp nhất qua Pull Request:** Chỉ đưa code của AI vào dự án chính thông qua luồng Pull Request và kiểm tra xung đột kỹ càng trước khi bấm Merge.
* **Cứu hộ thần tốc:** Nếu AI sinh code lỗi hoặc làm hỏng cấu trúc project, sử dụng lịch sử thay
* ## 🏁 Kết Luận

Qua project thực hành thực tế này, em đã nắm vững và thao tác thành thạo các kỹ năng Git/GitHub cơ bản, chuẩn bị một tâm thế và nền tảng kỹ thuật vững chắc cho khóa học **Vibe Code**. 

> 📝 **Bài học lớn nhất:** Quá trình thực hành đã giúp em cải biến tư duy từ những sai lầm khi mắc phải xung đột hay commit lỗi. Khi hiểu rõ mục tiêu cốt lõi của từng yêu cầu, em có thể suy luận ra nhiều hướng xử lý bài toán khác nhau và sử dụng Git như một công cụ kiểm soát tư duy logic để đưa ra giải pháp đúng ý, ngắn gọn và súc tích nhất
