from datetime import datetime

# Lấy ngày giờ hiện tại
now = datetime.now()

# Định dạng ngày giờ
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Hiển thị ngày giờ
print(f"Ngày giờ hiện tại: {formatted_date}")
