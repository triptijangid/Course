try:
    # Opening data.txt file in read mode and result.txt file in append mode because i have to store the result in the result.txt file.
    with open("data.txt","r") as f, open("result.txt", "a") as out:
        # Reading file line by line.
        for line in f:
            line = line.strip()

            try: 
                num = int(line)

                if num<0:
                    # Raise an value error if the value is not integer.
                    raise ValueError("Only integetrs are allowed")
                
                result = 1/num
                out.write(str(result)+ "\n")
            except ValueError:
                # Catch the value error
                print("Invalid value: ", line)

            except ZeroDivisionError:
                # Catch the zero divison error
                print("Cannot devided by zero")
except FileNotFoundError:
    # File not found error
    print("File is not present")

