class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        item_count_result = len(self.collection)
        print(item_count_result)

    def page_count(self):
        pg_count = len(self.collection) // self.items_per_page
        if len(self.collection) % self.items_per_page != 0:
            pg_count =  pg_count + 1
        print(pg_count)

    def page_item_count(self, page_index):
        if page_index < 0:
            return -1
        print(self.items_per_page)

    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        print(item_index // self.items_per_page)


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count()  # should output: 2
helper.item_count()  # should output: 6
print(helper.page_item_count(0))  # should output: 4
helper.page_item_count(1)  # last page - should output: 2
helper.page_item_count(2)  # should output: -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5)  # should output: 1 (zero-based index)
helper.page_index(2)  # should output: 0
helper.page_index(20)  # should output: -1
helper.page_index(-10) # should output: -1 because negative indexes are invalid
