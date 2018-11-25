from datetime import datetime

#User-Defined Function

def even(numbers):
    #Extract dictionary from the list
    dict = numbers[0]
    #Get numbers to be checked from the dictionary data
    num = dict['sequence']
    seq = num.split(',')
    even_num = []
    for numbers in seq: #Run loop for evaluating each number
        numbers = numbers.strip()
        numbers = int(numbers)
        if numbers%2==0:
            even_num.append(numbers)
    return (even_num)
    
            
#Main Code

#Print current date and time
print ("Solution 1. Current Date and Time: "+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"\n")

#Given list of numbers
numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

#Pass on the list of numbers to the Function and receive output after calculation
even_num=even(numbers) 
print ("Solution 2. Even Numbers From The List of Given Numbers Are As Follows:\n")
for numbers in even_num:
    print (numbers)

    
