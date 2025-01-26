import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

utm_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(index="utm_source", columns="is_click", values="user_id").reset_index()


clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])*100

percent_clicked = ad_clicks.groupby("experimental_group").user_id.count().reset_index()

percent_clicked["percent"] = percent_clicked["user_id"] / percent_clicked["user_id"].sum() *100


a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

day_a = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()
day_b = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()

day_a_pivot = day_a.pivot(columns="is_click", index="day", values="user_id")
day_b_pivot = day_b.pivot(columns="is_click", index="day", values="user_id")

day_a_pivot["percentage"] = day_a_pivot[True] / (day_a_pivot[False]+day_a_pivot[True])*100

day_b_pivot["percentage"] = day_b_pivot[True] / (day_b_pivot[False]+day_b_pivot[True])*100

print(day_a_pivot)
print(day_b_pivot)