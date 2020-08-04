import random                                                                #All import are used to call their respective functions 
import string
import time
import pickle
L1=[]
L1.extend(list(string.ascii_lowercase))                                     #A list is created later its extended with the necessary characters needed in the Password  
L1.extend(list(string.ascii_uppercase))
L1.extend(list(string.digits))
l3=['!','@','#','$','%','^','&','*','(',')']
L1+=l3
with open('fname.pickle','rb') as tnp:
    b=pickle.load(tnp)                                                         #load - is to read from pickle file
ultimate=[]
ultimate=L1
#print(ultimate)                                                            #print is used to check if all the lists are extended correctly
Response=input('Do you want to create a unique password ?  ')
while True:
    
    if Response.lower()== 'yes'or Response.lower()== 's':                   # here .lower() makes the Response case-insensitive
         Password=random.choices(ultimate,k=12)                              # Random.choices produce multiple inputs and K is the limit
         Password =''.join(Password)                                        # converts the List into String
         final=b.get(Password)                                    #here Final becomes 1  if the password is already present in the pickle file , 0 if the password is new to the pickle file
         while final:                                             # if Final is true (1) , then password is regenarated and again compared until the while loop becomes false
             Password=random.choices(ultimate,k=12)
             Password =''.join(Password)
             final=b.get(Password)
         with open('fname.pickle','wb') as tnp:                  #When the final is 0 , then its added to the pickle file
                 b[Password]=1
                 pickle.dump(b,tnp,protocol=pickle.HIGHEST_PROTOCOL)  # dump - to  write data into pickle file
                  
         print("Your password :  ",Password)                       # Your very own unique password 
         time.sleep(3)                                             
         break
    
    elif Response.lower()=='no':       
         print("Get Out")
         time.sleep(3)
         break
    else:
        print("YES or NO question \nTry again with a valid input")
        exit()

    
        
        
