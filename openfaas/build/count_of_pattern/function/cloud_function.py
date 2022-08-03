def cloud_function(json_input):
    string_array = json_input["string_array"]
    pattern = json_input["pattern"]
    
    
    # Processing
    count = 0
    for a in string_array:
        if  pattern == a:
                count=count+1

            

    result1=string_array#.append(count)
    result2=count
    # return the result
    res = {
        "count_array": result1,
        "count_of_pattern":result2
    }
    return res
