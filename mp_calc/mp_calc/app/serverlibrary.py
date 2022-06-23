## Merge Sort
def merge_items(A, start, middle, end, byfunc):
  # no. of elements
  n_left = middle - start + 1
  n_right = end - middle
  left_array = A[start:middle+1]
  right_array = A[middle+1:end+1]
  left = 0
  right = 0
  dest = start

  while (left<n_left) and (right<n_right): # check that cursor has not exceeded length of array
    if byfunc(left_array[left]) <= byfunc(right_array[right]): # left array has a smaller number
      A[dest] = left_array[left]
      left += 1 # move to next index
    else: # left array has a smaller number
      A[dest] = right_array[right]
      right += 1
    dest += 1

  while (left<n_left): # if right array is done
    A[dest] = left_array[left]
    left += 1
    dest += 1

  while (right<n_right): # if left array is done
    A[dest] = right_array[right]
    right += 1
    dest += 1

def merge(A, start, middle, end):
  # no. of elements
  n_left = middle - start + 1
  n_right = end - middle
  left_array = A[start:middle+1]
  right_array = A[middle+1:end+1]
  left = 0
  right = 0
  dest = start

  while (left<n_left) and (right<n_right): # check that cursor has not exceeded length of array
    if left_array[left] <= right_array[right]: # left array has a smaller number
      A[dest] = left_array[left]
      left += 1 # move to next index
    else: # left array has a smaller number
      A[dest] = right_array[right]
      right += 1
    dest += 1

  while (left<n_left): # if right array is done
    A[dest] = left_array[left]
    left += 1
    dest += 1

  while (right<n_right): # if left array is done
    A[dest] = right_array[right]
    right += 1
    dest += 1


def merge_sort_items(A, start, end, byfunc):
  if end<=start: # length = 0
    return
  else:
    middle = int((start + end)/2)
    merge_sort_items(A, start, middle, byfunc)
    merge_sort_items(A, middle+1, end, byfunc)
    merge_items(A, start, middle, end, byfunc)

def merge_sort(A, start, end):
    if end<=start: # length = 0
      return
    else:
      middle = int((start + end)/2)
      merge_sort(A, start, middle)
      merge_sort(A, middle+1, end)
      merge(A, start, middle, end)


def mergesort(array, byfunc=None):
  if byfunc is not None:
    merge_sort_items(array, 0, len(array)-1, byfunc)

  else:
    merge_sort(array, 0, len(array)-1)


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
      if len(self.__items) >= 1:
        last = self.__items[-1]
        self.__items.pop()
        return last

    def peek(self):
      if len(self.__items) >= 1:
        return self.__items[-1]
      else:
        return None

    @property
    def is_empty(self):
      return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


class EvaluateExpression:
  operands = "0123456789"
  operators = "+-*/()"

  def __init__(self, string=""):
    self.expr = string

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    valid_char = '0123456789+-*/() '
    self.expr = new_expr
    for char in new_expr:
      if str(char) not in valid_char:
        self.expr = ""
        break

  def insert_space(self):
    space_str = ''
    for char in self.expr:
      if str(char) in EvaluateExpression.operators:
        space_str += ' ' + char + ' '
      else:
        space_str += char
    return space_str

  def process_operator(self, operand_stack, operator_stack):
    op2 = operand_stack.pop()
    op1 = operand_stack.pop()
    op = operator_stack.pop()
    if op=="+":
      result = int(op1) + int(op2)
    elif op=="-":
      result = int(op1) - int(op2)
    elif op=='*':
      result = int(op1) * int(op2)
    elif op=='/':
      result = int(op1) // int(op2)
    operand_stack.push(result) # add result to stack

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    # phase 1
    for i in tokens:
      if i.isnumeric(): # if the extracted character is an operand, push it to operand_stack.
        operand_stack.push(int(i))

      elif i in "+-":
        while (not operator_stack.is_empty) and (operator_stack.peek() not in '()'):
          self.process_operator(operand_stack, operator_stack) # process all the operators at the top of the operator_stack
        operator_stack.push(i) # push the extracted operator to operator_stack

      elif i in "*/":
        if (not operator_stack.is_empty) and (operator_stack.peek() in "*/"):
                self.process_operator(operand_stack, operator_stack) # process till */
        operator_stack.push(i) # push the extracted operator to operator_stack

      elif i =="(":
        operator_stack.push(i)

      elif i ==")":
        while operator_stack.peek()!='(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop() # removes (

    # phase 2
    if operator_stack.is_empty:
      return
    else:
        while not operator_stack.is_empty:
          self.process_operator(operand_stack, operator_stack)

        return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]
