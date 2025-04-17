# # Creating a program that reads a file from a new file
# # This codes read a all text from index file and outputed it 
with open("index.txt","r") as file:
  data=file.read()
print(data)


# # Writing a modified version
# # This lines of codes replaces (Working smart is better than working hard) with "Success is all about the mindset" in edit.txt  file
with open("edit.txt","w") as file:
  file.write("Success is all about the mindset")


#   Error handling
try:
    with open("index.txt","r")as file:
         data=file.read()
         print (data)
except FileNotFoundError:         
  print("File not found.please check the filename.")

  



