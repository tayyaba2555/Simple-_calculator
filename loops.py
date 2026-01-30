# while True :
#print(""hello")

count = 1
while count <= 5:
    print("alfiya")
    count += 1
    print(count)

# 
i = 1
while i <= 1000:
   print("khantayyaba" , i)
   i += 1

i = 1
while i <= 5:
    print(i)
    i += 1

print("loops ended")

i = 5
while i >= 1:
    print(i)
    i -= 1
print("loops ended")

nums = [1, 2, 3, 4, 5]
veggies = ("potato" , "tomato" , "cabbage")
for val in nums:
    print(val)
for val in veggies:
    print(val)  

# looops in str
str = "khantayyaba"
for char in str:
    if(char == 'y'):
        print("y found")
        break
    print(char)
else:
    print("END")

seq = range( 6)
for i in seq:
    print(i)

seq = range(0, 10)
for i in seq:
    print(i)

seq = range(0, 10, 2)
for i in seq:
    print(i)
    