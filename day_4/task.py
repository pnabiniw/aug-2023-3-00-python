# Given a list a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)],
# sort the list based on the last item of each tuple inside the list.
# Output : [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]


def get_last_item(element):
    return element[-1]


data = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]
data.sort(key=get_last_item)
print(data)  # [(6, 1), (4, 12, 5), (6, 7, 8), (11, 12)]

