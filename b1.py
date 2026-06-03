inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False
    return True


def calculate_final_price(quantity, price):
    subtotal = quantity * price

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.1

    vat = (subtotal - discount) * 0.08
    final_total = subtotal - discount + vat

    return subtotal, discount, vat, final_total


def print_report():
    """Hiển thị tồn kho và doanh thu hiện tại."""
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    global inventory_stock, total_revenue

    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")

        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            try:
                amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))

                if amount <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                add_stock(amount)

            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        elif choice == "2":
            try:
                quantity = int(input("Nhập số lượng mua: "))
                price = float(input("Nhập đơn giá ($): "))

                if quantity <= 0 or price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                if not process_sale(quantity):
                    continue

                subtotal, discount, vat, final_total = calculate_final_price(quantity, price)

                inventory_stock -= quantity
                total_revenue += final_total

                print("\n-> Hóa đơn chi tiết:")
                print(f"Tạm tính: ${subtotal}")
                print(f"Giảm giá: ${discount}")
                print(f"VAT: ${vat}")
                print(f"Tổng thanh toán: ${final_total}")
                print("Đã bán thành công!")

            except ValueError:
                print("Vui lòng nhập số hợp lệ!")

        elif choice == "3":
            print_report()

        elif choice == "4":
            print("Thoát chương trình!")
            break

        else:
            print("Lựa chọn không hợp lệ!")

main()