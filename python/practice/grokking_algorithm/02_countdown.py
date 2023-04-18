def countdown(i):
    print(i)
    if i <= 0:  # base case
        return
    countdown(i - 1)  # recursive case


countdown(10)
