'''
Nhập các thành phần cần thiết từ thư viện PySide6 để 
-tạo cửa sổ chính (QMainWindow), 
-quản lý vòng đời ứng dụng (QApplication) 
-hiện thông báo lỗi (QMessageBox).
-QButtonGroup để quản lý nhóm checkbox
'''
from PySide6.QtWidgets import (QApplication,QMessageBox,QMainWindow,QButtonGroup)
'''
- QPixmap: Hiển thị ảnh: QPixmap được tối ưu hóa để vẽ hình ảnh lên các widget như 
   QLabel hoặc QPushButton , Hỗ trợ nhiều định dạng , tương tác với .qrc file
'''
from PySide6.QtGui import (QPixmap)# QPixmap là một lớp trong PySide6 dùng để xử lý hình ảnh. Nó cho phép bạn tải, hiển thị và thao tác với các hình ảnh trong ứng dụng của mình. QPixmap được tối ưu hóa để vẽ hình ảnh lên các widget như QLabel hoặc QPushButton, và hỗ trợ nhiều định dạng hình ảnh khác nhau. Bạn cũng có thể sử dụng QPixmap để tương tác với các file .qrc (Qt Resource Collection) để quản lý tài nguyên hình ảnh trong ứng dụng của mình.
from PySide6.QtCore import (Signal) # Signal để tạo tín hiệu tùy chỉnh, có thể dùng để truyền dữ liệu giữa các phần của ứng dụng
from UI.gui import Ui_MainWindow # import giao dien tu file gui.py
from UI.interface import * # import ham load du lieu vao combo box tu file interface.py
'''
traceback: Cực kỳ quan trọng, dùng để "truy vết" vị trí chính xác dòng code 
nào gây ra lỗi khi chương trình bị crash.
'''
import os,sys,traceback # import các thư viện liên quan tới hệ thống, đường dẫn , ghi lỗi
from common.log import *
from common.fileProcess import chk_mandatory_folder
'''Tạo một lớp tên là MainWindow kế thừa từ QMainWindow. 
Nó sẽ đóng vai trò là "bộ não" điều khiển toàn bộ giao diện của bạn.
'''
class MainWindow(QMainWindow):
    send_text = Signal(list)
#region---------------------Khoi Tao----------------------------
    def __init__(self, parent = None):
        try:
            QMainWindow.__init__(self)# Khởi tạo lớp cha (QMainWindow)
            self.ui = Ui_MainWindow()# Tạo một đối tượng giao diện từ class đã import
            self.ui.setupUi(self)# Đổ toàn bộ các nút bấm, layout từ file UI vào cửa sổ này
            #Show Window
            self.setWindowTitle("Effective Way For Label Approval Process - ZALO : 0375803690")
            icon_path = self.load_form_icon()
            self.setWindowIcon(icon_path) # set icon cho title
            self.center_on_screen() # set gui to the center
            chk_mandatory_folder("database")
            chk_mandatory_folder("img")
            self.image_storage = [] # Biến toàn cục để lưu đường dẫn ảnh đã chọn, có thể dùng để truyền dữ liệu giữa các hàm trong class này
            self.send_text.connect(self.store_data) # Kết nối tín hiệu send_text với hàm store_data để khi send_text.emit được gọi, store_data sẽ nhận dữ liệu và xử lý
            self.current_index = 0   # Vị trí ảnh đang xem (0 là ảnh đầu tiên)
            # Load data to combo box
            self.ui.configFr_prj_list.blockSignals(True) 
            '''# do việc load dữ liệu vào combo box sẽ kích hoạt sự kiện currentTextChanged, 
            nên tạm thời block tín hiệu để tránh lỗi blocksignal
            - sau khi load xong thì unblock để sự kiện hoạt động bình thường
            - Phải dùng lambda để truyền tham số vào hàm load_cbx_line, 
              nếu không sẽ bị lỗi vì hàm này cần 4 tham số mà sự kiện chỉ truyền 1 (text)
            '''
            load_combo_box_prj(self.ui.configFr_prj_list, "project", "projectName")
        # Event for Gui
            self.ui.configFr_prj_list.blockSignals(False)# Unblock signals after loading data    
            self.ui.configFr_prj_list.currentTextChanged.connect(lambda text: load_cbx_line(self.ui.configFr_line_list, "lineN", "line", "project", self.ui.configFr_prj_list.currentText()))
            
            # Thiết lập nhóm checkbox để chỉ cho phép chọn một trong hai (Individual hoặc Bulk)
            self.mode_group = QButtonGroup(self) # Tạo một nhóm để quản lý các checkbox
            self.mode_group.addButton(self.ui.chkbox_individual,1) # Thêm checkbox "Individual" vào nhóm với ID là 1
            self.mode_group.addButton(self.ui.chkbox_bulk,2) # Thêm checkbox "Bulk" vào nhóm với ID là 2
            # Thiết lập chế độ loại trừ (Chỉ cho phép chọn 1)
            self.mode_group.setExclusive(True)
            # 2. Kết nối sự kiện click của cả nhóm
            self.mode_group.buttonClicked.connect(lambda button: chbox_mode_changed(self.send_text,button,self.ui.chkbox_individual,self.ui.chkbox_bulk))# Kết nối sự kiện click của nhóm checkbox với hàm xử lý on_mode_changed
            # Nút AddImage để load ảnh hoặc folder event
            self.ui.btnAddImg.clicked.connect(lambda : on_btnAddImg_clicked(self.send_text,self.ui.chkbox_bulk,self.ui.chkbox_individual))# Kết nối sự kiện click của nút Add Image với hàm xử lý on_btnAddImg_clicked
            self.ui.btnReadBarcode.clicked.connect(lambda : self.on_btnRead_clicked())       
        except Exception as e:
            err_msg = traceback.format_exc()# Lấy chi tiết lỗi (dòng mấy, lỗi gì)
            QMessageBox.critical(self, "Error Alarm", str(e))# Hiển thị lỗi ra một hộp thoại thông báo
            logExport(f"Occur Error : \n {err_msg}")# Ghi lỗi vào file log để sau này có thể xem lại
#region Ham Dinh Dang
    def on_btnRead_clicked(self):
            # Kiểm tra xem kho có hàng không
            if not self.image_storage:
                print("Chưa có ảnh trong kho để đọc!")
                return

            # Lặp qua kho để xử lý
            for path in self.image_storage:
                print(f"Đang đọc ảnh: {path}")
                # Thực hiện logic quét Barcode ở đây
    #--> Hàm nhận dữ liệu từ signal và lưu vào biến toàn cục
    def store_data(self, data):
            self.image_storage = data
            print(f"Hệ thống đã nhận và lưu {len(self.image_storage)} ảnh vào kho.")
    #--> Hàm Load icon cho title của mainWindow
    def load_form_icon(self):
        strAbsPath = os.path.abspath(sys.argv[0])
        print(strAbsPath) 
        strCrrPath = os.path.dirname(strAbsPath)
        print(strCrrPath)
        strImgPath = os.path.join(strCrrPath,"img") + r"\kca.ico"
        pixmap = QPixmap(strImgPath)
        return pixmap
    #--> Hàm set gui ở trung tâm màn hình
    def center_on_screen(self):
        # Lấy màn hình hiện tại
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Lấy kích thước form
        size = self.frameGeometry()

        # Tính vị trí chính giữa
        center_point = screen_geometry.center()
        size.moveCenter(center_point)

        # Đặt lại vị trí cửa sổ
        self.move(size.topLeft())
if __name__ == '__main__':
    # Bat loi toan cuc
    '''
    "Global Exception Handler" (Bộ bắt lỗi toàn cục).
    1. Ý nghĩa của sys.excepthook
        - Bình thường, nếu code của bạn xảy ra lỗi mà không nằm trong khối try...except, 
        chương trình sẽ lập tức bị "văng" (crash), cửa sổ biến mất và bạn chỉ thấy lỗi hiện 
        ra ở Terminal.
        - Khi bạn gán sys.excepthook = exception_hook, bạn đang ra lệnh cho Python: 
        "Này, nếu có bất kỳ lỗi nào xảy ra mà tôi quên chưa bắt bằng try...except, 
        đừng có tắt app ngay lập tức. Hãy đưa cái lỗi đó vào hàm exception_hook của tôi 
        để tôi xử lý trước đã.
    '''
    def exception_hook(exctype, value, tb):
        import traceback
        err_msg = "".join(traceback.format_exception(exctype, value, tb))
        logExport(f"Uncaught Exception:\n{err_msg}")
        QMessageBox.critical(None, "Lỗi không bắt được", str(value))
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)# Tạo một instance của ứng dụng. Mỗi chương trình Qt chỉ có duy nhất 1 cái này.
    win = MainWindow()# Tạo cửa sổ chính từ class mình định nghĩa ở trên.
    win.show()        # Hiển thị cửa sổ lên màn hình (mặc định khi tạo xong nó sẽ ẩn).
    sys.exit(app.exec()) # Bắt đầu vòng lặp sự kiện (đợi người dùng click chuột...). Khi đóng app, nó sẽ thoát an toàn.