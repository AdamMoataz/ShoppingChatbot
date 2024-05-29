print("hi im Adam")

Name = input("what is your name ? ")
age = input("what is your age ? ")
hobby = input("what is your hobby ? ")

print("your details are as follow ")
print("Name: ", Name)
print("age: ", age)
print("hobby: ", hobby)

print("Welcome to our store")
print("Chose the department you want too shop in")
departments = ["frozen", "precoked","preheated","snacks","fruits and vegetables"]
for i in range(5):
    print(i+1,departments[i])
choice = input()
print("Thank you") 
print("You well be redirected to the desired depatment")