start = "start"
stop = "stop"
quit = "quit"
start_status = False
while True:
    input2 = input("> ").lower()
    if input2 == start:
        if not start_status:
            print("Car stated....ready to go")
            start_status = True
        else:
            print("The car is already started....")
    elif input2 == stop:
        if start_status:
            print("Car stopped.")
            start_status = False
        else:
            print("The car is already stoped....")
    elif input2 == "help":
        print(f"""
{start} - to start car
{stop} - to stop car
{quit} - to exit car
           """)
    elif input2 == quit:
        break
    else:
        print("I don't understand...")