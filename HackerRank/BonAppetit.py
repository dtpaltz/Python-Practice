


def bonAppetit(bill, k, b):
    total = sum(bill)
    shared_total = total - bill[k]

    actual_b = (shared_total / 2)
    if actual_b == b:
        print("Bon Appetit")
    else:
        print(actual_b - b)