def count_substring(string, sub_string):
    count = 0;
    for i in range(len(sub_string), len(string)+1):
        if (string[i-len(sub_string):i] == sub_string):
            count+=1
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count