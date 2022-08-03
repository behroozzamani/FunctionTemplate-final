def cloud_function(json_input):
    string = json_input["original_string"]
    
    # Processing
    result=string.split()
    # return the result
    res = {
        "array": result
    }
    return res
