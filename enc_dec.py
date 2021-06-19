def main():
    status = input("Encrypt or Decrypt Press E or D:  ")

    if status == "E":
        key1 = input("Enter Key 1: ")
        key2 = input("Enter Key 2: ")
        passc = input("Enter Passcode: ")


        key1 = key1.encode("utf-8").hex()
        key2 = key2.encode("utf-8").hex()
        passc = passc.encode("utf-8").hex()


        key1 = int(key1, 16)
        key2 = int(key2, 16)
        passc = int(passc, 16)

        key1_e = key1 ^ passc
        key2_e = key2 ^ passc
    
        key1_len = len(str(key1_e))
        
        if key1_len < 10:
            key3 = str(key1_e) + str(key2_e) + "0" + key1_len
            
        else:
            key3 = str(key1_e) + str(key2_e) + str(key1_len)
        
        

        print("Key 3: ", key3)
    
    elif status == "D":

        key3 = input("Enter key3: ")
        passc = input("Enter passcode: ")

        passc = passc.encode("utf-8").hex()
        passc = int(passc, 16)
    
        cut = int(key3[-2:])
        
        key1_rev = int(key3[:cut])
        key2_rev = int(key3[cut:-2])

        key1_rev = hex(key1_rev ^ passc)
        key2_rev = hex(key2_rev ^ passc)

        key1_rev = key1_rev[2:]
        key2_rev = key2_rev[2:]

        print("Key 1: ", bytes.fromhex(key1_rev).decode('utf-8'))
        print("Key 2: ", bytes.fromhex(key2_rev).decode('utf-8'))
    else:
        print("Wrong choice!")
        main()
        
main()
    