def main():
    time = input("What time is it? ").strip()

    if time.endswith("a.m."):
        c_time = convert(time)
        if 7 <= c_time <= 8:
            print("breakfast time")

    elif time.endswith("p.m."):
        c_time = convert(time)
        if 12 <= c_time:
            print("lunch time")
        elif 6 <= c_time <= 7:
            print("dinner time")

    else:
        c_time = convert(time)
        if 7 <= c_time <= 8:
            print("breakfast time")
        elif 12 <= c_time <= 13:
            print("lunch time")
        elif 18 <= c_time <= 19:
            print("dinner time")

def convert(time):
    hours, minutes = time.replace("a.m.", "").replace("p.m.", "").split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return (hours + minutes)

if __name__ == "__main__":
    main()