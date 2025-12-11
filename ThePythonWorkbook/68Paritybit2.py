import msvcrt
import sys
import os

def limited_input_win(limit):
    """Reads input character by character up to a limit (Windows only)."""
    print(f"Enter Bits,Only 8 Bit [ ONLY 0 and 1 ] ", end='', flush=True)
    user_input = ""
    while len(user_input) < limit:
        if msvcrt.kbhit(): # Check if a key has been pressed
            char_byte = msvcrt.getch()
            # Decode the byte to a character
            char = char_byte.decode('utf-8') 

            


            if char not in ('0', '1', '\r','\n'):
                    continue
            
            if char in ('\r', '\n'): # Handle Enter key
                break     
            user_input += char
            sys.stdout.write(char) # Echo character
            sys.stdout.flush()
            if char in ('\x08'):
                user_input=user_input[0:len(user_input)-1]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(user_input.replace(user_input[:len(user_input)-1], ""))            
    print()
    return user_input
    #######################################################################################

code = limited_input_win(8)
count=0
if len(code)<=8:
    for i in code:
        if i=="1":
            count+=1


    if count % 2==0:
        print("Parity bit is 0")
    else:
        print("Parity bit is 1")



