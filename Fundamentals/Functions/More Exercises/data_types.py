def data_types(data_type, data):
    if data_type == "int":
        output = int(data) * 2
    elif data_type == "real":
        output = f"{float(data) * 1.5:.2f}"
    elif data_type == "string":
        output = f"${data}$"
    return output


data_type_input = input()
data_input = input()
result = data_types(data_type_input, data_input)
print(result)
