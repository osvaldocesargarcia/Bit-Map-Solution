import case
import loadFile

def extract_elements(string_line):
    digits_list = []
    for digit in string_line:
        digits_list.append(int(digit))

    return digits_list


# ////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////
uploadFile = input("Do you want to upload your data from a file? (y/n)")

if uploadFile=="y":
    casesLoaded = loadFile.LoadFile().generate_cases()

    for case in casesLoaded:
        print("Loading..Please wait")
        output_value = case.output()
        for output_temp in output_value:
            print(output_temp)


else:

    tests_length = int(input("Please enter the number of tests:   "))
    tests_count = 0
    cases_list = []

    while(tests_count<tests_length):

        n = int(input("Please set the value of N:   "))
        m = int(input("Please set the value of M:   "))
        count_n = 0
        print("Now set the values of the bit map")
        print("")
        print("EXAMPLE: when n = 3 and M = 4")
        print("0001")
        print("0011")
        print("0010")
        print("")
        input_matrix = []
        while (count_n<n):

            row_list = input("Define values of row #"+str(count_n)+":   ")
            if not len(row_list) == m:
                print("Error! - The size of the array must be equal to value M")
            else:
                row_digits = extract_elements(row_list)
                input_matrix.append(row_digits)
                count_n+=1

        cases_list.append(
            case.Case(n, m, input_matrix))
        print("_________________________________________________________________________")
        tests_count+=1

    for case in cases_list:
        output_value = case.output()
        for output_temp in output_value:
            print(output_temp)