def day(n):
    if (n < 24):
        return 1
    return 1 + day(n - 24)

def hour(n):
    if (n < 24):
        return n
    return hour(n - 24)

def main():
    #n = 445, therefore we should be on
    #day 19, hour 13
    d = day (445)
    h = hour(445)
    print(d, h)

main()

<<<<<<< Updated upstream
#input_file_list[element_count].append(element);
=======
#temp_list[element_count].append(element);
>>>>>>> Stashed changes
