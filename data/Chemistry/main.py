# define functions
def data_parser(file_location, salt):
    f = open(file_location, "r")
    for x in f:
        result = x.split(" = ")
        salts = result[1].split(" ; ")
        for s in salts:
            if salt == s:
                return result[0]
    f = open(file_location, "r")
    for x in f:
        result = x.split(" = ")
        salts = result[1].split(" ; ")
        for s in salts:
            if s in salt or salt in s:
                return result[0]
        
    return "invalid input"


def solubility_o_s():
    file_location = "programming data\salt solubility.txt"
    salt = str(input("Input salt name : "))
    results = str(data_parser(file_location, salt))
    print ("Salt : " + salt)
    print ("Solubility : " + results)

def prep_method():
    file_location = "programming data\preparing method of salts.txt"
    salt = str(input("Input salt name : "))
    results = str(data_parser(file_location, salt))
    print ("Salt : " + salt)
    print ("Preparation method : " + results)



def pick_operations(reply):
    print(reply)
    if reply == 1:
        solubility_o_s()
        return
    if reply == 2:
        prep_method()
        return
    if reply == 3:
        return
    if reply == 4:
        return 


def main():
    print ("Welcome")
    print ("Please pick a task")
    print ("1. solubility of salts")
    print ("2. preparing method of salts")
    print ("3. effect of heat on salts and gas test")
    print ("4. anion test")

    reply = int(input("Operation : "))

    pick_operations(reply)



if __name__ == '__main__':
    main()