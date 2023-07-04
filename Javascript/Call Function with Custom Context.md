### [Call Function with Custom Context](https://leetcode.com/problems/call-function-with-custom-context/description/)

## Brief Description:
### Symbol () 
A symbol is a unique and immutable data type in JavaScript that can be used as a property key for objects. Symbols are created using the `Symbol()` function, which returns a new symbol value each time it is called.
Here is an example of how symbols can be used as property keys for objects:

```javascript
const mySymbol = Symbol();
const myObject = {
  [mySymbol]: "Hello, world!"
};

console.log(myObject[mySymbol]); // logs "Hello, world!"
```

In this example, we create a new symbol using the `Symbol()` function and store it in the `mySymbol` variable. We then use this symbol as a property key for an object, assigning the value `"Hello, world!"` to that property. When we access the property using the symbol key, we get the value that we assigned to it.
One of the main benefits of using symbols as property keys is that they are guaranteed to be unique. This means that if you use a symbol as a property key for an object, you can be sure that it will not conflict with any other properties on the object, even if those properties have the same name.
I hope this explanation helps you understand what symbols are and how they can be used in JavaScript. 

### this context
Imagine you are playing a game with your friends where you pretend to be different characters. Each character has their own special abilities and things they can do. When it's your turn to play, you get to choose which character you want to be, and then you can use their abilities and do the things that they can do.
In JavaScript, the `this` context is like choosing which character you want to be when it's your turn to play. When you call a function, you can choose what the `this` context should be, and then the function can use the properties and methods of that object, just like how you can use the abilities of the character you choose to be.
For example, let's say we have two objects, `cat` and `dog`, and each object has a `speak` method that makes them say "meow" or "woof". When we call the `speak` method on the `cat` object, the `this` context is set to the `cat` object, so the method will make the cat say "meow". When we call the `speak` method on the `dog` object, the `this` context is set to the `dog` object, so the method will make the dog say "woof".
Just like how you can choose which character you want to be when it's your turn to play, in JavaScript you can choose what the `this` context should be when you call a function. This lets you control what the function can do and what properties and methods it can access.
I hope this explanation helps you understand what the `this` context is in JavaScript.


## Explanation:
This code defines a `callPolyfill` method on the `Function.prototype` object, which allows you to call a function with a specified `this` context and arguments. The method takes in an `obj` as its first parameter, which becomes the `this` context for the function, and any number of additional arguments, which are passed to the function.

Here is a detailed explanation of the main logic of the code:
1. The method creates a unique symbol using the `Symbol()` function. This symbol is used as a property key to temporarily store the function on the `obj`.
2. The method sets the `this` context of the function to the provided `obj` by assigning the function to a property on the `obj` with the unique symbol key.
3. The method calls the function with the provided arguments by accessing it on the `obj` using the unique symbol key. This ensures that the `this` context inside the function is set to the `obj`.
4. The method deletes the temporary property from the `obj` by deleting the property with the unique symbol key.
5. The method returns the result of calling the function.

I hope this explanation helps you understand how this code works.

## Time and Space Complexity:
### `Time Complexity`:
The time complexity of this code is O(1), because it performs a constant number of operations regardless of the size of the input.

### `Space Complexity`:
The space complexity is also O(1), because it uses a constant amount of additional memory to store the unique symbol and temporary property on the `obj`.

## Code:
```javascript
/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */

Function.prototype.callPolyfill = function(obj, ...args) {
  // Create a unique symbol to use as the property key
  const key = Symbol();
  // Set the this context of the function to the provided obj
  obj[key] = this;
  // Call the function with the provided arguments
  const result = obj[key](...args);
  // Delete the temporary property from the obj
  delete obj[key];
  // Return the result of calling the function
  return result;
}

```
