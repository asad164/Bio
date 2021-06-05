class Mybio:
  def __init__(self, n,a):
        self.name = n
        self.age = a
  def my_info(self, i):
      self.interest = i
      print('Name:', self.name, 'Age: ', self.age, 'and Interest:', self.interest)

iam = Mybio('asad', 31)
iam.my_info('Development with Django')
  
