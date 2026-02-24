'''
Nhập các thành phần cần thiết từ thư viện PySide6 để 
-tạo cửa sổ chính (QMainWindow), 
-quản lý vòng đời ứng dụng (QApplication) 
-hiện thông báo lỗi (QMessageBox).
'''
from PySide6.QtWidgets import (QApplication,QMessageBox,QMainWindow)
'''
- QPixmap: Hiển thị ảnh: QPixmap được tối ưu hóa để vẽ hình ảnh lên các widget như 
   QLabel hoặc QPushButton , Hỗ trợ nhiều định dạng , tương tác với .qrc file
'''
from PySide6.QtGui import (QPixmap)
from UI.gui import Ui_MainWindow # import giao dien tu file gui.py
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
        except Exception as e:
            err_msg = traceback.format_exc()# Lấy chi tiết lỗi (dòng mấy, lỗi gì)
            QMessageBox.critical(self, "Error Alarm", str(e))
            logExport(f"Occur Error : \n {err_msg}")
#region Ham Dinh Dang
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