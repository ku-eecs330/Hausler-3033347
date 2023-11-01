from lab4 import Deque

def wordToDeque(input_string):
    deque = Deque()
    for char in input_string:
        deque.push(char)
    return deque

def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front_node is None or test_string[i] != temp.front_node.item:
            return False
        else:
            temp.front_node = temp.front_node.next
    if temp.front_node is not None:
        return False
    return True


test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque))  # Should return True

