#task from codewars
#sum wo numbers without using operators +, -, add, etc...

#first try:

#the code is in cpp

int Add (int x, int y){
  int xx = pow(2, x);
  int yy = pow(2, y);
  return log2(xx * yy);
  }
# this code may not work because it exceeds the memory limit of an int and rounds it to the wrong digit
# i tried to replace int by int64_t. The first sub_cases worked this time.
# second try :

int Add (int x, int y){
  return log2(pow(2, x) * pow(2,y));
  }
# this code works because it doesn't round since it uses 64 bit for a float, therefore it is more accurate.However this is not an optimal solution because it may exceed the memory limit 64 bits in cases with very large numbers

# optimal solution :

int Add (int x, int y){
  while (y != 0) {
  int carry = x & y;
# the operator & returns a 1 in each bit position for which the corresponding bits of both operands are 1.
  x = x ^ y;
# the operator ^ is comparing the 2 numbers on base 2 and if only one one is present at one position
# (for example the first digit of both) it returns one, otherwise zero.
# Then it returns the created number (0101 & 0011 => 0110)
  y = carry << 1;
# the operator << shifts the bits number by one to the left leaving the firs digit equal to zero
  }
  return x;

}
# now i have no idea how it works but i understood the operators

