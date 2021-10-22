import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree 
import BinaryHeap 
import AdjacencyList 
import time
import algorithms
import SortableBook

from MaxQueue import MaxQueue


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
    def __init__(self) :
        self.bookCatalog = None
        self.shoppingCart = SLLQueue.SLLQueue()
        self.indexTitle = None
        self.sortedTitle = None
        self.bookSortedCatalog = None ###############################NEW
        self.indexKeys= None
        

    def loadCatalog(self, fileName : str) :
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        self.indexTitle = ChainedHashTable.ChainedHashTable()
        self.sortedTitle = BinarySearchTree.BinarySearchTree()
        self.bookSortedCatalog = ArrayList.ArrayList() #######################################NEW
        self.indexKeys = ChainedHashTable.ChainedHashTable()

        with open(fileName,encoding="UTF8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                # book = SortableBook.SortableBook(key, title, group, rank, similar) #######################NEW
                # self.bookSortedCatalog.append(book)
                # self.indexTitle.add(title,s)
                # self.sortedTitle.add(title,s)
                self.indexKeys.add(s.key, i )
                i += 1
            # The following line is used to calculate the total time 
            # of execution
        self.similarGraph =  AdjacencyList.AdjacencyList(self.bookCatalog.size())
        with open(fileName, encoding="UTF8") as f:
            i = 0
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                l = similar.split()
                for k in range(1,len(l)):
                    j = self.indexKeys.find(l[k])
                    if j is not None:
                        self.similarGraph.add_edge(i,j)
                i += 1
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

        
    def setRandomShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        print(self.shoppingCart)
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")
    
    def setShoppingCart(self) :
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = SLLQueue.SLLQueue()

        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")


    def removeFromCatalog(self, i : int) :
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i : int) :
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

   
    def searchBookByInfix(self, infix : str) :
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        '''

        title_of_book = []
        book_txt_index = []
        start_time = time.time()
        catalog_size = self.bookCatalog.size() #declares a variable to the size of the catalog
        book_data = self.bookCatalog.dummy.next

        for i in range(catalog_size): #iterating through the self.bookCatalog.size()
            if infix in book_data.x.title:
                #sets limits of book to 50 if no entry
                if len(title_of_book) < 50:
                    book_txt_index.append(i)
                    title_of_book.append(book_data.x.title)
            book_data = book_data.next

        for i in range(len(title_of_book)):
            print(f"Title: {title_of_book[i]}\nIndex: {book_txt_index[i]}\n") # formats the way the output will be represented

        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")



    def removeFromShoppingCart(self) :
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def bestSelling(self):
        start_time = time.time()
        s = MaxQueue()
        book = self.shoppingCart.head
        for i in range(self.shoppingCart.size()):
            s.add(book.x)
            book = book.next
        print("Max:", s.max())
        elapsed_time = time.time() - start_time
        print(f"bestSelling Completed in {elapsed_time} seconds")

    def reverseshoppingCart(self):
        start_time = time.time()
        self.shoppingCart.reverse()
        elapsed_time = time.time() - start_time
        print(f"reverse Completed in {elapsed_time} seconds")

    def title_of_book(self, title: str):
        start_time = time.time()
        t = self.indexTitle.find(title)
        if t != None:
            self.shoppingCart.add(t)
        else:
            return None
        elapsed_time = time.time() - start_time
        print(f"Added to shopping cart {t} \n{elapsed_time} seconds")

    def indexSortedTitle(self, prefix: str):
        start_time = time.time()
        p = self.sortedTitle.find(prefix)
        if prefix == "":
            return None
        elif p != "":
            self.shoppingCart.add(p)
            print(f"Added to shopping cart {p}")
        else:
            return None
        elapsed_time = time.time() - start_time
        print(f"indexSortedTitle Completed in {elapsed_time} seconds")

    def SearchInfixBestSelling(self, infix: str):
        x = BinaryHeap.BinaryHeap()
        y = self.bookCatalog
        k = 0
        book_title = []
        book_rank =[]
        if infix == "":
            return None


        for i in range(len(y)):
            if infix in y[i].title:
                rank = y[i].rank * -1
                x.add(Book.Book(y[i].key,y[i].title,y[i].group, rank, y[i].similar))

        for j in range(len(x)):
            k += 1
            if k == 11:
                break
            print(x.remove())

    def binarySearchbyTitle(self,title: str): ##########################################NEW
        start_time = time.time()
        if title == "":
            return None
        bookSortedCatalog = ArrayList.ArrayList()
        booktitle = ArrayList.ArrayList()
        for x in self.bookSortedCatalog:
            bookSortedCatalog.append(x)
        for y in bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.quick_sort(bookSortedCatalog)
        algorithms.quick_sort(booktitle)
        i = not None
        while i is not None:
            i = algorithms.binary_search(booktitle, title)
            if i is not None:
                print(i,bookSortedCatalog[i])
                booktitle.set(i, "None")
        elapsed_time = time.time() - start_time
        print(f"Binary Search Completed in {elapsed_time} seconds")
    # def SortableBooks(self, prefix: str, choice: str):
    #     start_time = time.time()
    #
    #     Array = []
    #     index = -1
    #     for i in self.bookCatalog:
    #         index += 1
    #         if prefix in i.title:
    #             a = index, i.title
    #             if choice == "1" or choice == "2":
    #                 Array.append(a)
    #
    #     if choice == "1":
    #         print("Merge Sort: ", algorithms.merge_sort(Array))
    #     elif choice == "2":
    #         print("Quick Sort: ", algorithms.quick_sort(Array))
    #     elapsed_time = time.time() - start_time
    #     print(f"sorting books completed in {elapsed_time} seconds")

    def mergeSort(self):
        booktitle = ArrayList.ArrayList()
        for y in self.bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.merge_sort(booktitle)
        algorithms.merge_sort(self.bookSortedCatalog)
        # x = self.bookSortedCatalog
        # titleCatalog = ArrayList.ArrayList()
        # algorithms.merge_sort(x)
        # for i in self.bookSortedCatalog:
        #     titleCatalog.append(i.tite)
        # print(algorithms.merge_sort(titleCatalog))
    def quickSort(self):
        booktitle = ArrayList.ArrayList()
        for y in self.bookSortedCatalog:
            booktitle.append(y.title)
        algorithms.quick_sort(booktitle)
        algorithms.quick_sort(self.bookSortedCatalog)
        # x = self.bookSortedCatalog
        # titleCatalog = ArrayList.ArrayList()
        # algorithms.quick_sort(x)
        # for i in self.bookSortedCatalog:
        #     titleCatalog.append(i.tite)
        # print(algorithms.quick_sort(titleCatalog))














