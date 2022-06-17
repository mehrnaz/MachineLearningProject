

def get_feature_percentage_numerical_chars(name: str):
    numbers = sum(c.isdigit() for c in name)
    return numbers / len(name)

if __name__ == "__main__":
    print(get_feature_percentage_numerical_chars('123abc.com'))