//Variable
var x = 1+1
x = 3
println(x*x)//6

//val은 재지정x
println({
  val x=1+1
  x+1
}) //3

//function 
(x: Int) => x+1
val addOne = (x: Int) => x+1
println(addOne(1)) //2

//val add = (x: Int, y: Int) => x+y
//println(add(1,2)) //3

val getTheAnswer = () => 42
println(getTheAnswer())

//Methods 
def add(x: Int, y:Int): Int = x+y
println(add(1, 2))

def addThenMultiply(x: Int, y:Int)(multiplier:Int):Int = (x+y)*multiplier
println(addThenMultiply(1,2)(3))

def name: String = System.getProperty("user.name")
println("Hello, "+name+"!")

def getSquareString(input: Double): String={
  val square = input*input
  square.toString
}

// Case Clasees - immutable
case class Point(x: Int, y: Int)

val point = Point(1,2)
val anotherPoint = Point(1,2)
val yetAnotherPoint = Point(2,2)
