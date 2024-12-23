class Matplot():
    
    def barplot(x_points, y_points):
        print("\nBarplot:")
        max_height = max(y_points)
        for height in range(max_height, 0, -1):
            row = ""
            for value in y_points:
                if value >= height:
                    row += "█ "
                else:
                    row += "  "
            print(row)
        print("-" * (len(y_points) * 2))
        print(" ".join(str(x) for x in x_points))

    
    def lineplot(x_points, y_points):
        print("\nLineplot:")
        max_height = max(y_points)
        for height in range(max_height, 0, -1):
            row = ""
            for i in range(len(y_points)):
                if y_points[i] == height:
                    row += "● "
                elif i > 0 and y_points[i - 1] < height < y_points[i]:
                    row += "/ "
                elif i > 0 and y_points[i - 1] > height > y_points[i]:
                    row += "\\ "
                else:
                    row += "  "
            print(row)
        print("-" * (len(y_points) * 2))
        print(" ".join(str(x) for x in x_points))

    @staticmethod
    def scatterplot(x_points, y_points):
        print("\nScatterplot:")
        max_height = max(y_points)
        for height in range(max_height, 0, -1):
            row = ""
            for value in y_points:
                row += "● " if value == height else "  "
            print(row)
        print("-" * (len(y_points) * 2))
        print(" ".join(str(x) for x in x_points))


def main():
    print("Welcome to the Text-Based Plotting Tool!")
    print("Choose the type of plot:")
    print("1. Barplot")
    print("2. Lineplot")
    print("3. Scatterplot")
    choice = input("Enter your choice (1/2/3): ")

    # Taking user input for x-axis points
    raw_x_points = input("Enter x-axis points separated by spaces: ")
    x_points = raw_x_points.split()

    # Taking user input for y-axis points
    raw_y_points = input("Enter y-axis points separated by spaces: ")
    y_points = list(map(int, raw_y_points.split()))

    # Ensure the x and y points have the same length
    if len(x_points) != len(y_points):
        print("Error: The number of x-axis points and y-axis points must match!")
        return

    # Plot based on user choice
    if choice == "1":
        Matplot.barplot(x_points, y_points)
    elif choice == "2":
        Matplot.lineplot(x_points, y_points)
    elif choice == "3":
        Matplot.scatterplot(x_points, y_points)
    else:
        print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
