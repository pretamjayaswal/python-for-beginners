# Python program to show the order
# in which methods are resolved

class God:
	pass

class A(God):
	def rk(self):
		print(" In class A")
class B(God):
	def rk(self):
		print(" In class B")
class D:
	def rk(self):
		print(" In class D")

# classes ordering
class C(A, B):
	def __init__(self):
		print("Constructor C")

r = C()

# it prints the lookup order
print(C.__mro__)
print(C.mro())
