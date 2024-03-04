from collections import deque

egs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

boxes = 0

while egs and papers:
    eg = egs.popleft()
    paper = papers.pop()

    if eg <= 0:
        papers.append(paper)
        continue

    elif eg == 13:
        papers.append(paper)
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    elif eg + paper <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egs:
    print(f"Eggs left: {', '.join(str(x)for x in egs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x)for x in papers)}")
