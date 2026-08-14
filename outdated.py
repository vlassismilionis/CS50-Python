def main():
    months = {
        "January" : "01",
        "February" : "02",
        "March" : "03",
        "April" : "04",
        "May" : "05",
        "June" : "06",
        "July" : "07",
        "August" : "08",
        "September" : "09",
        "October" : "10",
        "November" : "11",
        "December" : "12"
    }

    while True:
        # Getting input from user in format: MM/DD/YYYY & Month DD, YYYY
        try:
            date = input("Date: ").strip()
            i = list(date)
            # If the first char is a digit then the format is MM/DD/YYYY
            if i[0].isdigit():
                m, d, y = date.split(sep="/")
                m = int(m)
                d = int(d)
                y = int(y)
                if m <= 0 or m >= 13 or d >= 32 or d <= 0 or y <= 0 :
                    continue
                if m < 10 and d < 10:
                    print(f"{y}-0{m}-0{d}")
                    break
                elif m >= 10 and d < 10:
                    print(f"{y}-{m}-0{d}")
                    break
                elif m < 10 and d >= 10:
                    print(f"{y}-0{m}-{d}")
                    break
                else:
                    print(f"{y}-{m}-{d}")
                    break
            # If the first char is a letter then the format is Month DD, YYYY
            elif i[0].isalpha:
                m, d, y = date.split(sep=" ")
                # Checking if there is not a ,(comma) after d(DD):
                d1 = list(d)
                if not "," in d1:
                    continue
                d = int(d.replace(",", ""))
                y = int(y)
                if d >= 32 or d <= 0 or y <= 0 :
                    continue 
                if d >= 10:
                    print(f"{y}-{months[m]}-{d}")
                    break
                else:
                    print(f"{y}-{months[m]}-0{d}")
                    break
            else:
                continue
        except ValueError:
            pass


main()