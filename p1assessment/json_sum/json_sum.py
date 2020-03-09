import json 

json_data = {
    "data": [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
}

def sum_data(data):
    data_sum=0
    for rows in data.values():
        for nums in rows:
            data_sum+=sum(nums)
    return data_sum

summed_num=sum_data(json_data)
summed_data={"sum":summed_num}

with open("mydata.json","w") as file_object:
    json.dump(summed_data,file_object,indent=2)

