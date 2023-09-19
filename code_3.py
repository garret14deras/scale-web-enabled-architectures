
def generate_random_data():
    random_string = 'Make into by also because how choose.'
    random_number = 57

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Make into by also because how choose.")
        print(f"Random Number: 57")

if __name__ == "__main__":
    main()
