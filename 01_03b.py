from collections import Counter

def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    counter = Counter(inventory)
    #sell 5 starters, 3 salads, and 3 entrees
    counter.subtract(STA001 = 5, SAL002 = 3, ENT004 = 3)
    #make 9 more starters and 1 more entree
    counter.update(STA001 = 9, SAL002 = 0, ENT004 = 1)
    print(inventory)

if __name__ == "__main__":
    main()