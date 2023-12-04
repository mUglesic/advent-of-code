#include <iostream>
#include <algorithm>

namespace dataStructures {

    // Definitions

    template<typename T>
    class List;

    template<typename T>
    class Array;

    // Declarations

    template<typename T>
    class List {
        public:
            List() {
                first = new Node();
                last = new Node();
                size = 0;
            }
        private:
            class Node {
                public:
                    Node() {
                        next = nullptr;
                    }
                    Node (T d) {
                        data = d;
                    }
                public:
                    T data;
                    Node *next;
                public:
                    friend std::ostream& operator << (std::ostream &os, const Node *node) {

                        if (node->next) os << "[" << node->next->data << "]";
                        // else os << "List is empty!";

                        return os; 
                    }
            };
        private:
            Node *first;
            Node *last;
            int size;
        private:

            void addFirst(Node *newEl) {
                first->next = newEl;
                last->next = newEl;
            }

            void addLast(Node *newEl) {
                Node *temp = last->next;
                last->next->next = newEl;
                last = temp;
            }

            Node *getElement(int index) {
                if (index < 0 || index >= size) return nullptr;

                Node *el = first;
                int i = 0;

                while (i < index) {
                    el = el->next;
                    i++;
                }

                return el;
            }

        public:

            void add(T val) {
                Node *newEl = new Node(val);

                if (size == 0) {
                    addFirst(newEl);
                }
                else {
                    addLast(newEl);
                }

                size++;
            }

            void remove(int index) {
                if (index < 0 || index >= size) {
                    std::cout << "Index out of range: " << index << " | size: " << size << "\n";
                    return;
                }

                Node *le = getElement(index);
                Node *toDelete = le->next;

                if (size == 1) {
                    first->next = nullptr;
                    last->next = nullptr;
                }
                else if (le == last) {
                    Node *secondLast = getElement(size - 2);
                    le->next = nullptr;
                    secondLast->next = le;
                    last = secondLast;
                }
                else {
                    le->next = le->next->next;
                    if (toDelete == last) {
                        last = le;
                    }
                }

                delete toDelete;
                size--;
            }

            int getIndex(T val) {
                Node *el = first;
                int i = 0;

                while (el->next) {
                    if (el->next->data == val) return i;
                    i++;
                    el = el->next;
                }

                return -1;
            }

            int getSize() {
                return size;
            }

            Array<T> toArray() {
                Array<T> arr(size);

                Node *el = first;
                int i = 0;

                while (el->next) {
                    arr.set(i, el->next->data);
                    i++;
                    el = el->next;
                }

                return arr;
            }

            void printFirst() {
                std::cout << "First element: " << first << "\n";
            }

            void printLast() {
                std::cout << "Last element: " << last << "\n";
            }

            void printAll() {
                Node *el = first;

                if (size == 0) {
                    std::cout << "This list is empty!\n";
                }
                else {
                    std::cout << "List size: " << size << "\n";
                }

                std::cout << "[";

                while (el->next) {
                    std::cout << el << (el->next->next ? " -> " : "");
                    el = el->next;
                }

                std::cout << "]\n";
            }

            void clean(int debug = 0) {
                if (debug) std::cout << "Cleaning list...\n";

                Node *el = first;
                Node *nextEl;

                while (el->next) {
                    nextEl = el->next;
                    delete el;
                    el = nextEl;
                }

                if (debug) std::cout << "List cleaned!\n";
            }
    };

    template<typename T>
    class Array {
        public:
            Array(int n) {
                arr = new T[n];
                size = n;
            }
            Array(T *t, int n) {
                arr = new T[n];
                copy(arr, t, n);
                size = n;
            }
        private:
            T* arr;
            int size;
        public:

            T get(int index) {
                return arr[index];
            }

            void set(int index, T val) {
                arr[index] = val;
            }

            void fill(T val) {
                for (int i = 0; i < size; i++) {
                    arr[i] = val;
                }
            }

            void copy(T *dst, T *src, int n) {
                for (int i = 0; i < n; i++) {
                    dst[i] = src[i];
                }
            }

            Array<T> copyOf() {
                Array<T> newCopy(size);

                copy(newCopy.arr, arr, size);

                return newCopy;
            }

            void sort() {
                std::sort(arr, arr + size);
            }

            int length() {
                return size;
            }

            void print() {
                print(0, size);
            }

            void print(int start, int end) {
                std::cout << "[";
                for (int i = start; i < end; i++) {
                    std::cout << "[" << arr[i] << "]" << (i < end - 1 ? ", " : "");
                }
                std::cout << "]\n";
            }

            void clean(int debug = 0) {
                if (debug) std::cout << "Cleaning Array...\n";
                delete[] arr;
                if (debug) std::cout << "Cleaned Array!\n";
            }

        public:

            T& operator[] (int n) {
                return arr[n];
            }

    };

}