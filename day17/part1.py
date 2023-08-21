def main():
    with open("input.txt") as f:
        input = f.read().strip()
    _, limits = input.split("x=")
    x_range, y_range = limits.split(", y=")
    y_min, y_max = y_range.split("..")
    y_min = int(y_min)
    print((y_min + 1) * y_min // 2)


if __name__ == "__main__":
    main()
