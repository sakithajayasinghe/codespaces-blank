# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: W1987579 
# Date: 4/21/2023
def user_inputs():
    #range check and integer check operations included.
    range_list = [0, 20, 40, 60, 80, 100, 120]
    # Loop continuously until valid input is obtained
    while True:
        try:
            # Declare a, b, and c as global variables
            #https://www.w3schools.com/python/python_variables_global.asp#:~:text=The%20global%20Keyword,can%20use%20the%20global%20keyword.
            global a,b,c
            # Prompt the user to enter the pass mark,defer,fail and store it in a,b,c
            a = int(input("Please enter pass mark:"))
            if a not in range_list:
                print("out of range")
                continue
            b = int(input("Please enter defer mark:"))
            if b not in range_list:
                print("out of range")
                continue
            c = int(input("Please enter fail mark:"))
            if c not in range_list:
                print("out of range")
                continue
            # If all three marks are integers, return them
            if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
                return a, b, c
        except ValueError:
            print("integer required")

def progression_outcome(a,b,c):
    #selecting appropriate progression outcome according to the user input
    global pr_list_by_names
    pr_list_by_names = ["Progress","Progress(module trailer)","Do not Progress – module retriever","Exclude"]
    exclude_list = [[40, 0, 80], [20, 20, 80], [20, 0, 100], [0, 40, 80], [0, 20, 100], [0, 0, 120]]
    input_sequence = [a, b, c]
    if input_sequence in exclude_list:
        return pr_list_by_names[3]
    else:
        if a==120 :
            return pr_list_by_names[0]
        elif a==100:
            return pr_list_by_names[1]
        elif a in range(0,81):
            return pr_list_by_names[2]
        else:
            pass

def total_check(a,b,c):
    #checking total equals to 120.
    if a + b + c == 120:
        return True
    else:
        print("Total must be 120")
        return False
def staff_mode():
    #getting multiple outcomes loop
    while True:
        next_step = input("Please enter 'y' to CONTINUE. Please enter 'q' to QUIT: ")
        if next_step == 'q':
            return True
        elif next_step == 'y':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'q'.")
            
pr_list_by_count = [0, 0, 0, 0]
outcomes = 0
#histrogram function
def histogram(pr_list_by_count):
    if progression_outcome(a,b,c)== "Progress":
        pr_list_by_count[0]+=1
    elif progression_outcome(a,b,c)== "Progress(module trailer)":
        pr_list_by_count[1]+=1
    elif progression_outcome(a,b,c)== "Do not Progress – module retriever":
        pr_list_by_count[2]+=1    
    elif progression_outcome(a,b,c)== "Exclude":
        pr_list_by_count[3]+=1   
    else:
        pass
    return pr_list_by_count
#histrogram printing function after inputting data to histrogram function
def histrogram_printer():
    print('----------------------Histogram-------------------------------')
    print('Progress',pr_list_by_count[0],'  :',"*"*pr_list_by_count[0])
    print('Progress(module trailer)',pr_list_by_count[1],'   :',"*"*pr_list_by_count[1])
    print('Retriever',pr_list_by_count[2],' :',"*"*pr_list_by_count[2])
    print('Excluded',pr_list_by_count[3],'  :',"*"*pr_list_by_count[3])
    print(outcomes,'Outcomes In Total.')


print('**********START**********')
select_version=int(input("Select the version.\n 1.version 1(Main Version)\n 2.version 2(List (extension))\n 3.version 3(Text File (extension))\n 4.version 4(Dictionary)\nYour choice:"))
if select_version==1:
    while True:
        a,b,c = user_inputs()
        if total_check(a,b,c):
            print(progression_outcome(a,b,c))
            histogram(pr_list_by_count)
            outcomes += 1
            
            if staff_mode():
                histrogram_printer()
                break

list_for_progress=['Progress']
list_for_trailer=['Progress(module trailer)']
list_for_retriever=['Do not Progress – module retriever']
list_for_exclude=['Exclude']
def progression_list():
    progression_outcome(a,b,c)
    if progression_outcome(a,b,c)== "Progress":
     list_for_progress.extend([a,b,c])
     
    if progression_outcome(a,b,c)== "Progress(module trailer)":
     list_for_trailer.extend([a,b,c])
    
    if progression_outcome(a,b,c)== "Do not Progress – module retriever":
     list_for_retriever.extend([a,b,c])
       
    if progression_outcome(a,b,c)== "Exclude":
     list_for_exclude.extend([a,b,c])
    return list_for_progress,list_for_trailer,list_for_retriever,list_for_exclude  
     
def print_progression_list() :
    print('----------------------List Extension----------------------------')
    global lists
    lists = [list_for_progress,list_for_trailer,list_for_retriever,list_for_exclude]
    print(list_for_progress)
    print(list_for_trailer)
    print(list_for_retriever)
    print(list_for_exclude)

if select_version==2:
    while True:
        a,b,c = user_inputs()
        if total_check(a,b,c):
            print(progression_outcome(a,b,c))
            progression_list()
            pr_list_by_count = histogram(pr_list_by_count)
            outcomes += 1
            if staff_mode():
                histrogram_printer()
                print_progression_list()
                break
def write_data_on_txt_file():
    #write on text file
    progression_list()
    file = open("progression_data.txt", "w")
    file.write(str(list_for_progress) + '\n')
    file.write(str(list_for_trailer) + '\n')
    file.write(str(list_for_retriever) + '\n')
    file.write(str(list_for_exclude) + '\n')
    file.close()
def read_data_from_text():
    file = open('progression_data.txt', 'r')
    data = file.read()
    file.close()
    print(data)

if select_version == 3:
    while True:
        a, b, c = user_inputs()
        if total_check(a, b, c):
            print(progression_outcome(a, b, c))
            write_data_on_txt_file()
            if staff_mode():
                read_data_from_text()
                break

dictionary_for_progress = {}
dictionary_for_trailer = {}
dictionary_for_retriever = {}
dictionary_for_exclude = {}


def create_dictionary():
    # Prompt the user to enter their ID and store it in a variable called id
    id = input("Enter Your ID: ")
    # Call progression_outcome function with three arguments a, b, and c, and store the result in a variable called outcome
    outcome = progression_outcome(a, b, c)
    # Generate a result string by concatenating the ID, outcome, and values of a, b, and c.
    result = f"{id}: {outcome} - {a}, {b}, {c}"

    # Depending on the outcome, add the result string to one of four dictionaries
    if outcome == "Progress":
        dictionary_for_progress[id] = result
    elif outcome == "Progress(module trailer)":
        dictionary_for_trailer[id] = result
    elif outcome == "Do not Progress – module retriever":
        dictionary_for_retriever[id] = result
    elif outcome == "Exclude":
        dictionary_for_exclude[id] = result

    # Return the four dictionaries from the function    
    return dictionary_for_progress, dictionary_for_trailer, dictionary_for_retriever, dictionary_for_exclude

if select_version == 4:
    while True:        
        a, b, c = user_inputs()
        if total_check(a, b, c):
            outcome = progression_outcome(a, b, c)
            print(outcome)
            if outcome:
                create_dictionary()
                #using nested for loop to print result
            if staff_mode():
                for d in [dictionary_for_progress, dictionary_for_trailer, dictionary_for_retriever, dictionary_for_exclude]:
                    for id, result in d.items():
                        print(result)
                break

    
            
  
    


