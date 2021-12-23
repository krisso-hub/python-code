
# pull request on xmas tour

Responses = {}

Pull_active = True

while Pull_active:
    name = input("\nWhat's your name: ")
    message= input("Where are you traveling to this season: ") 

    Responses[name]= message
    repeat = input("\nDo you want another person to try (yes/no): ")
    
    if repeat == "no":
        Pull_active = False

print("---the xmass pull requst---")
for name, message in Responses.items():
    print(f"{name.title()} will be traveling to {message.title()} this season")
