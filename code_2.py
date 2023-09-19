
def generate_random_data():
    random_string = 'Serious reality agree future many response purpose threat.'
    random_number = 48

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Serious reality agree future many response purpose threat.")
        print(f"Random Number: 48")

if __name__ == "__main__":
    main()
