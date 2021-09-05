class Item(object):

  def __init__(self, value):
    self.value = value
    self.prev = None
    self.nxt = None

  def addPrev(self,prev):
    self.prev = prev

  def addNext(self,nxt):
    self.nxt = nxt

  def getPrev(self):
    return self.prev

  def getNext(self):
    return self.nxt

  def getValue(self):
    return self.value

class Cache(object):

  def __init__(self, size):
    self.head = None
    self.tail = None
    self.meta = {}
    self.capacity = size
    self.size = 0

  def addToCache(self,i):

    if i in self.meta:
      self.removeFromCache(self.meta[i])
    
    if self.size >= self.capacity:
      self.deleteItem()

    temp = Item(i)
    if self.head == None:
      self.tail = Item(None)
      temp.addNext(self.tail)
      self.tail.addPrev(temp)
      self.head = temp
    else:
      temp.addNext(self.head)
      self.head.addPrev(temp)
      self.head = temp
    self.meta[i] = temp
    self.size += 1

  def deleteItem(self):
    temp = self.tail.getPrev()
    self.removeFromCache(temp)

  def removeFromCache(self,i):
    if i.getPrev() == None:
      self.head = i.getNext()
    else:
      i.getPrev().addNext(i.getNext())
    i.getNext().addPrev(i.getPrev())
    i.addPrev(None)
    i.addNext(None)
    del self.meta[i.getValue()]
    self.size -= 1

  def readFromHead(self):
    print("Reading from head")
    temp = self.head
    while temp.getValue() != None:
      print(temp.getValue())
      temp = temp.getNext()

  def readFromTail(self):
    print("Reading from tail")
    temp = self.tail
    while temp.getPrev() != None:
      print(temp.getPrev().getValue())
      temp = temp.getPrev()

if __name__ == "__main__":

  c = Cache(5)
  for i in range(7):
    c.addToCache(i)

  for i in range(3,7):
    c.addToCache(i)

  c.readFromHead()
  c.readFromTail()
