import queue

names = ['Spock', 'Kirk', 'Gamorra', 'Star Lord', 'Rocket', 'Khabib']

def hotPotato(names, count):
    circleQ = queue.Queue()
    for name in names:
        circleQ.enqueue(name)
    while circleQ.size() > 1:
        for i in range(count):
            circleQ.enqueue(circleQ.dequeue())
        print(circleQ.dequeue())
    return circleQ.dequeue()

print(hotPotato(names, 12))