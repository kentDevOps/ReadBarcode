from common.sqlProcess import *
from common.log import *
from PySide6.QtWidgets import (QFileDialog)
def load_combo_box_prj(combo_box, table_name, column_name):
    rs = get_value_db(table_name, column_name)# Lấy dữ liệu từ database
    combo_box.clear()# Xóa dữ liệu cũ trong combo box
    combo_box.addItems(["None"])# Thêm một mục "None" vào combo box để người dùng có thể chọn nếu không muốn chọn dự án nào
    combo_box.addItems(item[0] for item in rs)# Thêm dữ liệu mới vào combo box, item[0] vì get_value_db trả về một list các tuple, mỗi tuple có một phần tử là giá trị của cột cần lấy
def load_cbx_line(combo_box, table_name, column_name, condition_col, condition_val):
    rs = get_value_cbx_line(table_name, column_name, condition_col, condition_val)
    combo_box.clear()
    combo_box.addItems(["None"])
    combo_box.addItems(item[0] for item in rs)
def chbox_mode_changed(button,chk_individual,chk_bulk):# Hàm xử lý khi người dùng chọn một trong hai checkbox (Individual hoặc Bulk)
    print(f"Bạn vừa chọn: {button.text()}")# In ra tên của checkbox vừa được chọn
    selected_mode = button.text()# Lấy tên của checkbox vừa được chọn
    #send_text_signal.emit(selected_mode) # Gửi tín hiệu với tên của checkbox vừa được
    if button == chk_individual:
        # Làm gì đó khi chọn Individual
        pass
    elif button == chk_bulk:
        # Làm gì đó khi chọn Bulk
        pass
def on_btnAddImg_clicked(send_text_signal,chk_bulk,chk_individual):# Hàm xử lý khi người dùng click vào nút Add Image
    iniPath = os.path.normpath(read_ini("DIRECTORY","imgPath"))# Lấy đường dẫn mặc định từ file config.ini để mở file dialog ở thư mục đó
    selected_files = []
    if chk_individual.isChecked():
        print("Bạn đang ở chế độ Individual. Hãy chọn một ảnh để thêm.")
        # Thêm code để mở file dialog và chọn một ảnh
       
# Mở hộp thoại chọn 1 file ảnh
        # Dialog sẽ trả về đường dẫn của file ảnh đã chọn, hoặc None nếu người dùng hủy bỏ
        #_ ở đây là một biến tạm để nhận giá trị thứ hai mà QFileDialog.getOpenFileNames trả về (danh sách các filter đã chọn), nhưng chúng ta không cần dùng đến nó nên đặt là _ để tránh lỗi
        file_path, _ = QFileDialog.getOpenFileNames(
            None, 
            "Select Multiple Images", 
            iniPath, 
            "Image Files (*.png *.jpg *.bmp)"
        )
        if file_path:
            print(f"Đã chọn 1 file: {file_path}")
            selected_files = [file_path]
            #return [file_path]
    elif chk_bulk.isChecked():
        print("Bạn đang ở chế độ Bulk. Hãy chọn một folder để thêm nhiều ảnh.")
        # Thêm code để mở folder dialog và chọn một folder chứa nhiều ảnh   
# CHẾ ĐỘ BULK: Chọn cả một thư mục
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder Containing Images", iniPath)
        
        if folder_path:
            # Lấy tất cả file trong folder có đuôi ảnh phù hợp
            valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
            file_list = [
                os.path.join(folder_path, f) 
                for f in os.listdir(folder_path) 
                if f.lower().endswith(valid_extensions)
            ]
            
            print(f"Tìm thấy {len(file_list)} file ảnh trong thư mục: {folder_path}")
            selected_files = file_list
            #return file_list
    if selected_files:
            # PHÁT TÍN HIỆU: Gửi danh sách ảnh về cho Main
            send_text_signal.emit(selected_files) 
            print(f"Đã gửi {len(selected_files)} ảnh qua Signal")
    return selected_files