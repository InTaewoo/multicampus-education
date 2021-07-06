# 함수 선언부
# 큐가 꽉찼는가?
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE -1) & (front == -1):
        return True
    else :
        for i in range(front+1,SIZE) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 큐가 비었는가?
def isQueueEmpty():
    global  SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

# 큐 삽입
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

# 큐 추출
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return
    front +=1
    data = queue[front]
    queue[front] = None
    return data

# 전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

# 메인 코드부
# queue = ['화사','솔라','문별','휘인','선미']
# front = -1
# rear = 4


enQueue('화사'); enQueue('솔라'); enQueue('문별')
enQueue('휘인'); enQueue('선미');
print(queue)

retData = deQueue(); print(deQueue())
retData = deQueue(); print(deQueue())


print(queue)
enQueue('태우')