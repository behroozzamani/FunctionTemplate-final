def cloud_function(json_input):
    string_array = json_input["string_array"]
    pattern = json_input["pattern"]
    m = json_input["m"]
    count_of_pattern=json_input["count_of_pattern"]

    
    # Processing
    
    #string_array.pop()
    if count_of_pattern<m:
        return string_array

    count_of_pattern = count_of_pattern - m
    new_str = ""
    count = 0
    for w in string_array:
        if (w != pattern): # or (count >= count_of_removes):
            new_str = new_str + w + " "
        else:
            if count < m:
                count = count + 1
                new_str = new_str + w + " "

    result= new_str


    # return the result
    res = {
        "final_array": result
    }
    return res
