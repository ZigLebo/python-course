import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# NOTE: Python version >=3.3 is required, due to "yield from" feature.

def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]

def bubblesort(A):
    """swapped=True
    for i in range(len(A)-1):
        if not swapped:
            break
        swapped=False
        for j in range(len(A)-1-i):
            if A[j]>A[j+1]:
                swap(A,j,j+1)
                swapped=True"""
    while not all(A[i] <= A[i+1] for i in range(len(A)-1)):
        random.shuffle(A)
        yield A

def insertionsort(A):
    for i in range(1,len(A)):
        j=i
        while j>0 and A[j]<A[j-1]:
            swap(A,j,j-1)
            j-=1
            yield A


def mergesort(A, start, end):
    """Merge sort."""

    pass

def quicksort(A, start, end):
    """In-place quicksort."""
    pass

def selectionsort(A):
    for i in range(len(A)):
        min_val=A[i]
        min_ind=i
        for j in range(i+1,len(A)):
            if A[j]<min_val:
                min_val=A[j]
                min_ind=j
        A[i],A[min_ind]=A[min_ind],A[i]
        yield A

if __name__ == "__main__":
    # Get user input to determine range of integers (1 to N) and desired
    # sorting method (algorithm).
    N = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:\n(b)ubble\n(i)nsertion\ n(m)erge \
        \n(q)uick\n(s)election\n"
    method = input(method_msg)

    # Build and randomly shuffle list of integers.
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "b":
        title = "Bubble sort"
        generator = bubblesort(A)
    elif method == "i":
        title = "Insertion sort"
        generator = insertionsort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergesort(A, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = quicksort(A, 0, N - 1)
    else:
        title = "Selection sort"
        generator = selectionsort(A)

    # Initialize figure and axis.
    fig, ax = plt.subplots()
    ax.set_title(title)

    # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
    # list of rectangles (with each bar in the bar plot corresponding
    # to one rectangle), which we store in bar_rects.
    bar_rects = ax.bar(range(len(A)), A, align="edge")

    # Set axis limits. Set y axis upper limit high enough that the tops of
    # the bars won't overlap with the text label.
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    # Place a text label in the upper-left corner of the plot to display
    # number of operations performed by the sorting algorithm (each "yield"
    # is treated as 1 operation).
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
    # To track the number of operations, i.e., iterations through which the
    # animation has gone, define a variable "iteration". This variable will
    # be passed to update_fig() to update the text label, and will also be
    # incremented in update_fig(). For this increment to be reflected outside
    # the function, we make "iteration" a list of 1 element, since lists (and
    # other mutable objects) are passed by reference (but an integer would be
    # passed by value).
    # NOTE: Alternatively, iteration could be re-declared within update_fig()
    # with the "global" keyword (or "nonlocal" keyword).
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()
