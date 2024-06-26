def find_indices(string, substring):
    indices = []
    leng = len(substring)
    for i in range(len(string)):
        if string[i:i+leng]==substring:
            indices.append(i)
    return indices


string = "hello python programming"
substring = "python"
print(find_indices(string,substring))