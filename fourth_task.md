# Python

### The following Python code purpose is to run a simple test function to check if two field values are the same. The team has been a bit clumsy and created unhealthy code. Can you help us figure out the mistakes and problems caused by this code? 

- Code sample found in `resources/compareFields.txt`

### Mark the problems in the code above or list the problems below:

- Inside the `compareFields()` method, for variable `FInput`, the conditional statement attempts to access the tuple at an out of bounds index, index `3`, causing an error. It should be index `2`, the same index the variable is already referring to before the conditional statement. 
- The following `if` statement has incorrect syntax for not equals. The correct syntax would be `!=`. 
- The string inside the following `append()` statement is not closed. It requires a double quotation mark `"` at the end.
- The `join()` method call should not have brackets `[]` around the parentheses `()`. It should be `join(errors)` instead of `join[(errors)]`.
- The `test_list()` method is missing a colon `:` after its parentheses. 
- The `print()` method call is missing parentheses `()` around the statement to be printed. 

### Test this code after it fixed. Can you give any suggestions (except syntaxis) or any possible improvements? 

- Variables and methods/functions in python should be written with `snake_case`. 
- The return statement in the `compareFields()` method does not require `None`. 
- The `test_list()` method would be more useful if it received a variable and passed it to the `compareFields()` method. It would allow for different variables to be tested. As it is now, calling `test_list()` would only run if a variable called as the given `checkList` is present in the module. 
- The `test_list()` method always returns a `verification failed` message, even if no `errors` are present. Should instead have an `if` statement where the `verification failed` message prints only if `errors` are present, else print something like `Verified`. 