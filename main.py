import Calculator
import BookStore
import DLList
import ChainedHashTable
import BinaryTree
import BinarySearchTree


def menu_calculator() :
    calculator =  Calculator.Calculator()
    option=""
    while option != '0':
        print ("""
        1 Check mathematical expression 
        2 Set variable to values
        3 introduce expression
        4 print expression
        5 Evaluate expression
        0 Return to main menu
        """)
        option=input() 
        if option=="1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression) :
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "2":
            key = input("Input your variable: ")
            if key != '':
                value =input("Input your value: ")
                calculator.set_variable(key,float(value))
            else:
                value = input("Introduce your value: ")
                calculator.set_variable(key,value)
            # calculator.set_variable(key, value)
        elif option == "3":
            x = 1
            while x == 1:
                expression = input("Introduce a valid mathematical expression: ")
                if calculator.matched_expression(expression):
                    print(f"{expression} is a valid expression")
                    x = 0

                else:
                    print(f"{expression} is invalid expression")
                    x = 1


        elif option == "4":
            for i in expression:
                if calculator.dict.find(i) == None:
                    print(i, end='')
                else:
                    print(calculator.dict.find(i), end='')
        elif option == "5":
            print(calculator.evaluate(expression))


        ''' 
        Add the menu options when needed
        '''

def menu_bookstore_system() :
    bookStore = BookStore.BookStore()
    option=""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Reverse the order of the shopping cart
        7 Best selling book
        8 search by title(new function)
        9 search by prefix( binary lab)
        10 Traverse through bookstore txt
        11 SEARCH BESTSELLING(BINARY HEAP)
        12 merge sort
        13 quick sort
        14 prefix binary search
        15 bfs search
        16 dfs search
        0 Return to main menu
        """)
        option=input() 
        if option=="r":
            bookStore.setRandomShoppingCart()
        elif option=="s":
            bookStore.setShoppingCart()
        elif option=="1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name) 
            #bookStore.pathLength(0, 159811)
        elif option=="2":
            i = int(("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option=="3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option=="4":
            bookStore.removeFromShoppingCart()
        elif option=="5":
            infix = input("Introduce the query to search: ")
            bookStore.searchBookByInfix(infix)
        elif option=="6":
            bookStore.reverseshoppingCart()
        elif option=="7":
            bookStore.bestSelling()
        elif option=="8":
            title = input("Introduce the title:")
            bookStore.title_of_book(title)
        elif option == "9":
            prefix = input("Introduce prefix: ")
            bookStore.indexSortedTitle(prefix)
        elif option == "10":
            choice = ""
            while choice != "0":
                print("""
                                1 Test In Order Traversal
                                2 Test Pre Order Traversal
                                3 Test Post Order Traversal
                                4 Test Breath First Traversal
                                0 Return to Bookstore System menu
                                """)
                choice = input()
                if choice == "1":
                    in_order = bookStore.sortedTitle.in_order(bookStore.sortedTitle.r, [])
                    for book in in_order:
                        with open("books_in_order.txt", "a", encoding='UTF8') as f:
                            f.write(f"\n{book}")

                elif choice == "2":
                    pre_order = bookStore.sortedTitle.pre_order(bookStore.sortedTitle.r, [])
                    for book in pre_order:
                        with open("books_pre_order.txt", "a", encoding='UTF8') as f:
                            f.write(f"\n{book}")

                elif choice == "3":
                    post_order = bookStore.sortedTitle.post_order(bookStore.sortedTitle.r, [])
                    for book in post_order:
                        with open("books_post_order.txt", "a", encoding='UTF8') as f:
                            f.write(f"\n{book}")

                elif choice == "4":
                    breath_first_order = bookStore.sortedTitle.bf_traverse()
                    for book in breath_first_order:
                        with open("books_bftraversal.txt", "a", encoding='UTF8') as f:
                            f.write(f"\n{book}")
        elif option == "11":
            prefix = input("Introduce prefix: ")
            bookStore.SearchInfixBestSelling(prefix)
        elif option == "12":
            bookStore.mergeSort()
        elif option == "13":
            bookStore.quickSort()
        elif option == "14":
            prefix = str(input("enter prefix: "))
            bookStore.binarySearchbyTitle(prefix)
        elif option == "15":
            index = int(input("Enter the index of the starting book: "))
            index_location = int(input("Enter the distance from the starting index: "))
            x = bookStore.similarGraph.bfs2(index, index_location)
            for i in range(1, len(x)):
                print(bookStore.bookCatalog.get(x[i]))
        elif option == "16":
            pointer_1 = int(input("Enter the starting book index: "))
            pointer_2 = int(input("Enter the reaching index: "))
            result = bookStore.similarGraph.dfs2(pointer_1,pointer_2)
            print("the degree of seperation is: ", result)

        # elif option == "12":
        #     choice = ""
        #     prefix = input("enter a book title: ")
        #     if prefix == "":
        #         return None
        #     while choice != "0":
        #         print("Choose the following option to sort the books")
        #         print("""
        #                     1 Merge Sort
        #                     2 Quick Sort
        #                     0 Return to main menu
        #
        #
        #                     """)
        #         choice = input()
        #         if choice == "1" or choice == "2":
        #            bookStore.SortableBooks(prefix, choice)





        ''' 
        Add the menu options when needed
        '''
def the_DLList():
    dLList = DLList.DLList()
    option =""
    while option != '0':
        print("""
                1 Add a element
                2 Remove element
                3 Check if Palindrome
                4 Print out List
                0 Return to Main menu
                """)
        option=input()
        if option=="1":
            append_value =input("Please enter a value: ")
            dLList.append(append_value)
        elif option=="2":
            remove_value = input("Please enter a value: ")
            if remove_value in dLList:
                dLList.remove(remove_value)
            else:
                print("Value is not in the list")
        elif option=="3":
            print(dLList.isPalindrome())
        elif option=="4":
            print(dLList)
def traversal_function():
    y = BinaryTree.BinaryTree()
    x = BinarySearchTree.BinarySearchTree()
    option = ""
    while option != '0':
        print("""
                1 Add Elements
                2 Pre-Order
                3 In-Order
                4 Post-Order
                5 Breath First
                6 Height
                0 Return to Main menu
                """)
        option=input()
        l = list()
        if option=="1":
            node = input("Enter Node: ")
            value = input("Introduce Node value: ")
            x.add(node,value)
        elif option=="2":
            x.pre_order(x.r, l)
            print(', '.join(map(str, l)))
        elif option=="3":
            x.in_order(x.r, l)
            print(', '.join(map(str, l)))
        elif option=="4":
            x.post_order(x.r, l)
            print(', '.join(map(str, l)))
        elif option=="5":
            print(x.bf_traverse())
        elif option=="6":
            print(x.height())




#main: Create the main menu
def main() :
    option=""
    while option != '0':
        print ("""
        1 Calculator
        2 Bookstore System
        3 DLList
        4 traversal and Height
        0 Exit/Quit
        """)
        option=input() 
        
        if option=="1":
            menu_calculator()
        elif option=="2":
            menu_bookstore_system()
        elif option=="3":
            the_DLList()
        elif option == "4":
            traversal_function()


if __name__ == "__main__":
  main()
