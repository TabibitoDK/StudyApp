class saltf:
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