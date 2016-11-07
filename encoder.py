'''
Given the following decoder, write the encoder. (The encoder should be written to compress whenever possible): 

p14a8xkpq -> p14akkkkkkkkpq 

(8xk gets decoded to kkkkkkkk. The only other requirement is that encodings be unambiguous) 

Note that the String can have any possible ascii character
'''

def encoder(s):
    output = ""
    prev = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] == prev:
            count +=1
        else:
            if count >1:
                output += str(count) + 'x' + prev
            else:
                output += prev
            prev = s[i]
            count = 1
    
    if count>1:
        output += str(count) + 'x' + prev
    else:
        output += prev
        
    return output

def main():
    print(encoder("12222222'''''$$$$$$^"))

main()