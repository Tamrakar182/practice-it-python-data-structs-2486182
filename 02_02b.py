from collections import deque

def main():
    #add code here
    word = input("Gib me word: ")
    deque_moment = deque(word)
    if(deque_moment.popleft == deque_moment.pop):
        print("Its a palindrome")
    return

if __name__ == "__main__":
    main()