
def generate_random_data():
    random_string = 'Third city tonight adult model.'
    random_number = 79

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Third city tonight adult model.")
        print(f"Random Number: 79")

if __name__ == "__main__":
    main()
