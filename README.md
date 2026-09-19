# Lab: Linked Lists and Recursion  
**Lab GitHub Repo**: [Linked Lists and Recursion](https://github.com/learn-co-curriculum/Linked-Lists-and-Recursion)

---

## Overview
In this lab, we’ll apply **linked lists** and **recursion** to build a small prototype for managing a list of data. Imagine a junior developer assigned to maintain a simple employee roster, where IDs are stored in a linked list. You’ve been asked to implement **recursive** functionalities such as summing IDs, reversing the list in-place, and searching for a particular ID.

By focusing on **linked lists** (for dynamic insertion/deletion) and **recursion** (for elegant traversal), you’ll gain hands-on experience with node-based data structures—common in many low-level or performance-sensitive applications.

---

## Task 1: Define the Problem

1. **Load or create** an initial linked list of integer IDs.  
2. **Enable recursive functionality** to:
   - **Sum** all node data in the list.  
   - **Reverse** the list in-place.  
   - **Search** for a given ID.  
3. **Present** or print the result for each operation in a user-friendly format.

**The Challenge**: Demonstrate your understanding of linked lists while using recursion to solve day-to-day tasks such as searching and reversing data.

---

## Task 2: Determine the Design

### Linked List Structure

- **App / Main**  
  Drive the creation and manipulation of the linked list.  

- **Node Class**  
  Each node stores an **integer data** and a pointer/reference to `next`.  

- **LinkedList Class**  
  - `head` references the first node.  
  - Methods to **insert**, **sum**, **reverse**, and **search**.  

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.  

#### Open and Run
1. Open the project in your preferred Python-friendly environment (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Create a feature branch** (e.g., `feature/linked-list-lab`).  
2. **Create the `Node` and `LinkedList` classes**:
   - **Node** class with `data` and `next`.  
   - **LinkedList** class to house `head` and methods.
3. **Manage Linked List Insertion**:
   - `insert_at_front(data)` → O(1).  
   - *(Optional)* `insert_at_end(data)` → O(n) to traverse to the end.
4. **Use Recursion**:
   - **Sum**: Returns `0` if node is `None`, otherwise `node.data + recurse(node.next)`.  
   - **Reverse**: Re-point each node’s `next` to the **previous** node until the list is reversed.  
   - **Search**: Returns `True` if a node’s `data` matches the target; stops if it hits `None`.
5. **Run Tests** (if provided) or manually test:
   - Insert some sample data, then call each recursive method.  
   - Print the list or results to confirm correctness.
6. **Push feature branch** and open a PR on GitHub.
7. **Merge** to `main` once reviewed.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Add Comments**: Clarify logic for recursion, highlight base vs. recursive cases.  
- **Explain Intent**: Make it clear why you’re using recursion in a particular method (e.g., elegance, clarity, demonstration).  
- **README**: Update with instructions on how to run the code, test, and interpret results.  
- **Clean Up**:
  - Remove any debugging prints or stale branches.  
  - Ensure your `.gitignore` is updated to exclude unnecessary files.

## How to Run

From the project root:

```bash
python3 main.py
```

Expected output:

```
Initial roster:
103 -> 102 -> 101 -> 104 -> None
Sum of all IDs: 410
Search for 102: True
Search for 999: False
Reversed roster:
104 -> 101 -> 102 -> 103 -> None
```

`main.py` builds a sample employee-ID roster, then prints the list, the recursive sum, two search results, and the reversed list.

## How to Test

```bash
python3 -m unittest tests.test_linked_list -v
```

All five tests should pass: insert at front, empty-list sum, populated-list sum, search, and in-place reverse.

## Interpreting Results

- **Sum** walks every node and adds `data`. An empty list returns `0`.
- **Search** returns `True` only when a node's `data` matches the target.
- **Reverse** rewires each `next` pointer in place and updates `head`.

## Submission
Once the lab is complete, all tests are passing, and you've pushed the completed code to 
your forked repo on GitHub, submit your GitHub repo through Canvas using CodeGrade.