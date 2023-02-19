def main():
    x = input("File name: ")
    x = x.strip().lower()
    x = file(x)

def file(f):
    # TODO
    if '.gif' in f:
        print('image/gif')
    elif '.jpg' in f:
        print('image/jpeg')
    elif '.jpeg' in f:
        print('image/jpeg')
    elif '.png' in f:
        print("image/png")
    elif ".pdf" in f:
        print("application/pdf")
    elif '.txt' in f:
        print("text/plain")
    elif '.zip' in f:
        print("application/zip")
    elif '.bin' in f:
        print("application/octet-stream")
    else:
        print("Try different name")
    return f

main()