students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

if students % size == 0:
    print(f"Number of groups formed: {students / size}")

if students % size != 0:
    print(f"Number of groups formed: {students // size + 1}")