from email import message


def machine() : 
   ##created the string that contains character 
   keys ='abcdefghijklmmopqrstuvwxyz !'  
   values='@#$%^&*():"?><}{[]\"|~_-+=,/'


   encryptdict= dict(zip(keys,values))
   decryptdict = dict(zip(values,keys)) 

   mess=input("Enter your message ")
   mode =input("Please enter the mode : Encode(E) or Decode(D)")


   if mode=='E' :
      message=''.join([encryptdict[letter] 
                       for letter in mess.lower()])
   elif mode=='D' :
      message=''.join([decryptdict[letter]
                        for letter in mess.lower()]) 
   else:
      print("please Enter the correct choice ")

   return message.capitalize() 



print(machine())
