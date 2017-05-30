import queue

q1 = queue.Queue()

q1.put("d1")
q1.put("d2")
q1.put("d3")

print(q1.get())

q2 = queue.LifoQueue()

q2.put(1)
q2.put(2)
q2.put(3)

print(q2.get())
print(q2.get())
print(q2.get())


q3 = queue.PriorityQueue()

q3.put(9,"zhang")
q3.put(10,"xu")
q3.put(8,"tao")

print(q3.get())
print(q3.get())