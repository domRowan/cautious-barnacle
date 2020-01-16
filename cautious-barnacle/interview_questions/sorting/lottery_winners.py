import random
import heapq


class Customer:
    def __init__(self, id, price):
        self.id = id
        self.price = price


def get_top_n_customers_with_weight(customers, n):
    sorted_customers = []
    result = []
    customer_entries = set()

    for customer in customers:
        if not customer.id in customer_entries:
            customer_entries.add(customer.id)
            if len(sorted_customers) < n:
                heapq.heappush(sorted_customers,
                               (calculate_weight(customer.price), customer.id))
            else:
                # Remove an item from the heap and add in another if required
                heapq.heappushpop(sorted_customers,
                                  (calculate_weight(customer.price), customer.id))

        else:
            print "discarded duplicate entry: ", customer.id

    for i in range(0, len(sorted_customers)):
        result.append(sorted_customers.pop())

    return result


def calculate_weight(price):
    return price * random.randint(0, 1000)


x = Customer("x", 10000)
x = Customer("x", 1000)
y = Customer("y", 70)
z = Customer("z", 50)
a = Customer("a", 20)
b = Customer("b", 70)
c = Customer("c", 50)

customers = [x, y, z, a, b, c]
n = 1

print get_top_n_customers_with_weight(customers, n)
