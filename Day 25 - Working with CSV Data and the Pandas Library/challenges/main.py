import pathlib
import pandas

# gets current file directory
current_file = pathlib.Path(__file__)

# # gets weather-data.csv file
# weather_data = current_file.parent / "weather-data.csv"

# # loads the csv into pandas returning a pandas DataFrame
# data = pandas.read_csv(weather_data)

# # Gets the sequence (column) with the heading/key name temp
# temp = data["temp"]

# # converts sequence to list
# temp_list = temp.to_list()

# # gets mean of sequence
# mean = temp.mean()

# # gets maximum value from sequence
# maximum = temp.max()

# # retrieves a full row from the data which has the day "Friday" in the day column
# friday_row = data[data["day"] == "Friday"]

# # retrieves a full  row with maximum number in the "temp" column
# max_temp_row = data[data["temp"] == data["temp"].max()]

# # celsius to fahrenheit
# def to_fahrenheit(value):
    
#     return (value * (9/5))+32

# print(to_fahrenheit(int(max_temp_row["temp"])))

# # converts dictionary into pandas DataFrame
# data_dict = {
#     "students": ["David", "Ricardo", "Leo"], 
#     "scores": [100, 90, 0]
# }

# pd_data_dict = pandas.DataFrame(data=data_dict)

# print(pd_data_dict)

# # get location to save data
# save_location = current_file.parent / "example_data.csv"

# # Saves data into csv file
# pd_data_dict.to_csv(save_location)

# # to do: 

# write a program that reads from the csv file and determines the number of squirls with either a black, grey, or red color fur. 

squirrel_data_location = current_file.parent / "2018-Central-Park-Squirrel-Census-Squirrel-Data.csv"

data = pandas.read_csv(squirrel_data_location)

def get_count(color) -> int:
    
    result = data[data["Primary Fur Color"] == color]

    return result.shape[0]

black_count = get_count("Black")
gray_count = get_count("Gray")
cinnamon_count = get_count("Cinnamon")


new_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
new_data = pandas.DataFrame(data=new_data_dict)

output_path = current_file.parent / "squirrel_count.csv"

new_data.to_csv(output_path)



