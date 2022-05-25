def merge_the_tools(string, k):
    for i in range(int((len(string)/k))):
        print("".join(dict.fromkeys((string[i*k:((i*k)+k)]))))    