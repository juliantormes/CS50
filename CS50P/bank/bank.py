def value(greeting):
    greeting = greeting.lower()
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else :
        return 100
def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")
if __name__ == "__main__":
    main()
