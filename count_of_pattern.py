string_array=["one","one","one","two","one"]
pattern="one"
count = 0
for a in string_array:
    if pattern == a:
            count = count + 1

string_array.append(count)
print(string_array) 