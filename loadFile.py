import case

class LoadFile:

    def define_n_m_values(self,line):
        count_values = 0
        n_value = ''
        m_value = ''
        for letter in line:
            if letter.isdigit() and count_values == 0:
                n_value += letter
            elif not letter.isdigit():
                count_values = 1
            elif letter.isdigit() and count_values == 1:
                m_value += letter
        return [n_value, m_value]



    def define_row_vector(self,line):
        row_result = []
        for digit in line:
            if digit.isdigit():
                row_result.append(int(digit))
        return row_result


    def generate_cases(self):
        cases_list = []

        file = open('input.txt')
        file_lines = file.readlines()
        cases_length = int(file_lines.pop(0))


        count_cases = 0
        general_count = 0

        while (count_cases < cases_length and general_count<len(file_lines)):
            second_line_list = self.define_n_m_values(file_lines[general_count])
            n_value = int(second_line_list[0])
            m_value = int(second_line_list[1])
            matrix = []

            general_count+=1
            n_count = 0
            while (n_count<n_value and general_count<len(file_lines)):

                current_line=file_lines[general_count]
                row = self.define_row_vector(current_line)
                matrix.append(row)
                n_count +=1
                general_count+=1

            count_cases = count_cases + 1
            cases_list.append(case.Case(n_value,m_value,matrix))

        return cases_list

