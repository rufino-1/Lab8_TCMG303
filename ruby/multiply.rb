print "This Ruby program ask the user to input two integers. The code multiplies the two ingeters and outputs the result to the console.\n"

print "Enter the first number: "

first_num = gets.to_i

print "Enter the second number: "

second_num = gets.to_i

puts first_num.to_s + " * " + second_num.to_s + " = " +(first_num * second_num).to_s
