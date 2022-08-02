from datetime import date, timedelta
import corona_data

now = date.today() # 20200701
now_str = now.strftime("%Y%m%d")
print(now_str)

# 오늘날짜로 요청해
data = corona_data.get_corona_data('20200702','20200702')
print(data)
# 없으면 어제 날짜로 요청해라
if not data :
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    print(yesterday_str)

    data = corona_data.get_corona_data(yesterday_str,yesterday_str)
    print(data)