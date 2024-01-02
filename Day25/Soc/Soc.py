import pandas
data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray, count_cinnamon, count_black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Day25/squirrel_count.csv")