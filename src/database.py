import pymysql

class Database:
    """
    Class quản lý kết nối và thao tác với cơ sở dữ liệu MySQL.

    Class này cung cấp các phương thức để thực hiện truy vấn (query) và cập nhật (execute) dữ liệu trên cơ sở dữ liệu MySQL.

    Attributes:
        connection (pymysql.Connection): Đối tượng kết nối đến cơ sở dữ liệu.
    """
    def __init__(self):
        """
        Khởi tạo đối tượng Database và thiết lập kết nối đến cơ sở dữ liệu MySQL.
        """
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='waterfeel',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def query(self, sql, params=None):
        """
        Thực hiện truy vấn SQL và trả về kết quả.

        Args:
            sql (str): Câu lệnh SQL cần thực hiện.
            params (tuple, list, or dict, optional): Các tham số truyền vào câu lệnh SQL (nếu có).
                Mặc định là None.

        Returns:
            list of dict: Danh sách các bản ghi kết quả, mỗi bản ghi là một từ điển.

        Raises:
            pymysql.Error: Nếu có lỗi xảy ra trong quá trình thực hiện truy vấn.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()
        return result

    def execute(self, sql, params=None):
        """
        Thực hiện câu lệnh SQL (INSERT, UPDATE, DELETE) và commit thay đổi.

        Args:
            sql (str): Câu lệnh SQL cần thực hiện.
            params (tuple, list, or dict, optional): Các tham số truyền vào câu lệnh SQL (nếu có).
                Mặc định là None.

        Raises:
            pymysql.Error: Nếu có lỗi xảy ra trong quá trình thực hiện câu lệnh.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()