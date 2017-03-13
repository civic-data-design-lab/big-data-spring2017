# Front End Environments
## HTML/CSS/JavaScript: An Overview

### Part 2 - JavaScript: The Core Concepts

In the website ecosystem, the next component is the behavior. How do we take these styled elements and interact with them in a manner in which we can load data, dynamically populate elements, and create animations and interactions. This is where JavaScript comes in.

![Environment](images/environment.png)

#### What is JavaScript?

JavaScript is a web programming language that manipulates and controls the behavior of web pages by interacting with the various elements on the page and loading data. It, along with HTML and CSS, forms the foundation of modern web browsers and the internet. Many web site templates, such as Bootstrap, are in JavaScript, and it is the programming language that most of the major mapping and data visualization libraries, including D3, are implemented in.

One of the major concepts in web development is that of **server-side** versus **client-side**. The server is the machine that *serves* your website to the rest of the world, the client is the computer that is accessing that website (your computer), requesting information from the server. **Python is a server side language**, but JavaScript can be both, but **is primarily a client-side language**, working on your client computer. In the manner we are using it, JavaScript is a scripting language that will operate in two fundamental ways. The first is executing scripts and tasks when the web page is loaded (i.e. set up a page, or load a dataset on page open), and the second is executing scripts and tasks after the web page visitor tells it to (i.e. clicking a button) or another task is completed (i.e. a menu is closed). When JavaScript executes, it can manipulate the content of the page, change how it is being viewed through the browser, give information to a server, or tell the browser to go back to the server and get new information. Often, however, the instructions given by the script can be followed on the client without additional communication with the server.

JavaScript, in a manner similar to CSS, interacts with HTML elements using the DOM.

![DOM](http://duspviz.mit.edu/wp-content/uploads/2015/02/dom_model.jpg)

When you are working with D3 in the second half of the semester, some of your main goals will be to:

* Load and Bind Data
* Create Page Elements
* Modify and Set Element Properties
* Write Functions (blocks of code)
* Listen for User Interaction (ie clicks, hovers, rollovers)

#### Link a JavaScript Document to your Site

JavaScript can be added to your website by either typing in script between two **script** tags, or by linking a JavaScript file your site. In your file, at the bottom of the **body** section, add the following code snip. This will read all code found in the *main.js* file that is in the **js** folder.

```xml
<script src="js/main.js"></script>
```

In the body of your HTML document, above the script. Add a button using the following. When clicked, this button will run the function named **helloworld()** in our main.js JavaScript file, and change the content of the paragraph elements with *id="foo"*.

```xml
<button type="button" onclick="helloworld()">Click Me!</button>
```

So where is **helloworld()**? It is in the **main.js** document. The structure of it is as follows. It looks through the document to find an element named **foo**, then changes the HTML within that element to 'Hello JavaScript!'.

```js
function helloworld() {
    document.getElementById('foo').innerHTML = 'Hello JavaScript!';
}
```

Now, we are programming! Let's learn JavaScript!

#### JavaScript Consoles

*The In-browser JavaScript Console*

JavaScript is the language of the modern web browser. Modern web browsers have JavaScript consoles built that we can explore the basics of the language with. Open up our browser, navigate to a page, and open the browser JavaScript console and do some basic coding to show some of the principles. If you are using Chrome or Firefox, there are integrated JavaScript consoles that allow you to input and explore JavaScript. Use **CTRL+SHIFT+K** (Windows)/**CMD+OPTION+K** (Mac) for Firefox, and **CTRL+SHIFT+J** (Windows)/**CMD+OPTION+J** (Mac) for Chrome. In the following steps we will introduce some concepts, try them using the console, and look for how the concepts manifest in our web map code.

![JS Console](http://duspviz.mit.edu/wp-content/uploads/2015/02/browser-jsconsole.png)

In your JavaScript code, if you ever want to log something to the console, use:

```js
console.log([object]);

// for example
console.log("Hello world");

// or
var hello = "Hello world"
console.log(hello)
```

Try out all of the examples today using [REPL.IT](https://repl.it/languages/javascript), an online sandbox for testing out JavaScript.

#### Introducing Objects: The Foundation of JavaScript

Objects are the kings of JavaScript and almost everything you work with in JavaScript is an object. Objects are the main elements of JavaScript, and they can have properties, and values. To illustrate this, I will reference a nice example from W3schools, in real life, a car is an **object**. This car has **properties** like weight and color that are set to certain **values**, and it has **methods**, like start and stop (methods themselves are actually objects).

![JS Object](http://duspviz.mit.edu/wp-content/uploads/2015/02/js_object.png)

You will commonly be accessing objects within objects. Typical syntax might look like the following.

```js
[object1].[nested_object].[nested_nested_object]

// properties and methods
var car = {
    make:"Ford",
    model: "Mustang",
    year: 2013,
    color: "Red",
    accessories: {
        windows: "Power",
        transmission: "Automatic"
    },
    start: function(){
    	console.log("Vroom! Car started!");
    }
};

console.log(car)
console.log(car.make)
console.log(car.accessories.windows)
```

Our page elements from our HTML webpage document can be referenced through JavaScript. Using JavaScript, we can change the properties of these elements and tell them to do things, like change color, or disappear. Going back to our car example, to create a Ferrari and tell it to be red, we can create a car **div** with **id="myFerrari"**, then make it red by setting the **color** method **(myFerrari.color = "red")**.

Object and their properties can be stored stored and accessed for later use using variables. Try typing **car.start()**. You should get confirmation your car started. This is a function stored as a property. What is a function? We'll get to that soon, let's talk more about our variables. Hint, they are just like Python!

#### Variables

Variables are containers that hold data values, simple or complex, that can be referred to later in your code.

[Variables](http://www.w3schools.com/js/js_variables.asp) in JavaScript are alot like those in Python. The following are examples. Plug these into your JavaScript console one by one, hitting enter after each. **Note the semicolon!** All individual lines in JavaScript must end with a semicolon.

```js
// Simple math (note, this is a comment!)
var x = 5;
var y = 6;
var z = x + y;
```
In your JavaScript console, to see a current value of a variable, type it and hit enter, it will return the current value.


```js
z;
// will return
11
```

#### Data Types

Variables fall into two different data types, primitive and reference. Primitive data types must be of a specific type, where Reference data types can be thought of a references to other objects in your document.

Primitive Data Types

* **Boolean:** true or false
* **Number:** Any integer or floating-point value
* **String:** Text characters that are delimited by quotes
* **Null:** Variable set to have the value of null
* **Undefined:** Variable declared, but set to have no value

Examples of JavaScript data, and what can be stored as a variable and referred to later are shown below. Variables can contain many different data types, including strings, numbers, and even entire objects, arrays, and functions. To familiarize yourself with data in JavaScript, try some of the following in your browser JavaScript console.

All objects are mutable after being instantiated. Primitive values are immutable.

#### Primitive Data Types

##### Strings

Strings are text characters. They can be concatenated by using **+**.

```js
var name = "Michael";
var last_name = "Foster";
console.log(name);
console.log(last_name);
console.log(name + last_name); // string concatenation
```

##### Number

Number types can hold integers and decimals.

```js
var count = 25; // integer
var cost = 1.51; // decimal

count + cost // returns decimal
```

##### Boolean

Boolean values are either **true** or **false**. They are good for evaluation and flow control. Boolean values are the result of **comparison operators**.

```js
// you can set variables to be true or false
var found = true;
var lost = false;

// comparisons can evaluate to true or false
9 >= 10 // returns false
11 > 10 // returns true
```

Boolean values can also be applied to logical operators.

* **&&** - AND operator. True only if both values are true.
* **||** - OR operator. True if one or both values are true.
* **!** - NOT operator. True if statement is false.

##### Null and Undefined Objects

NULL objects can be created if you need an object, but you dont have anything to put in it yet you can populate it at a later point

```js
// null object
var object = null;

// undefined object
var flag = undefined;

// undefined object
var ref;
```

#### Reference Data Types

##### Array

```js
var array = []; //empty array
var array1 = [ 1, 3, 5 ]; //populated array
```

You can access array elements much like in Python lists. Just like Python, JavaScript is a **zero-index** language, meaning you access values in arrays using index values.

```js
array1[];
[1, 3, 5]
array1[0];
[1]
array1[1];
3
```

##### Object Literal

Object Literal data type is a comma separated list of name value pairs. Kind of like a **dict** in Python. Our car above was this example.

```js
var workshop = {
    name: "Big Data Class",
    year: 2017
};

console.log(workshop.name);
```
##### Function

You can place functions within variables.

```js
var myFunction = functionName(argument){
	// function code goes here
};
```

When you call the variable **myFunction**, it will run the function you have stored in that variable.

#### Functions

Introducing functions. Just like Python, functions are pieces of code that can run when called upon. To use a function, it must be defined using the *function* declaration.

##### Parameters versus Arguments

In the function definition above, we listed parameters that are taken by the function. *Parameters* are placeholders for objects that will be passed to the function when called. *Arguments* are the real values of the objects received as parameters for the function when it is invoked.

If a parameter is defined in JavaScript, it must be passed an argument when invoked. However, it is possible to provide default values if an argument is not received. [More on that here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)

When defining a function, you also define the parameters that are required for the function. These parameters are placeholders for accepting variable values created outside of the function. For example, let's look at a basic function.

```js
// function declaration with parameters
function multiply_this(a,b) {
    return a*b;
}

// call the function, providing arguments for the parameters
var x = 4;
var y = 5;

multiply_this(x,y); // run function with x and y as our arguments
20 // returned value
```

When a function reaches a *return* statement, it will stop executing. The return value is returned back to the calling object and carried forward.

##### Ways to Declare Functions

There are a couple of ways you can declare functions.

1. Function Declarations

Functions are declared using the *function* keyword, then saved for when they are called. Syntax looks as follows.

```js
// function declaration with two parameters
function multiply_this(a,b) {
    return a*b;
}

// invocation
multiply_this(x,y)
20 // return value
```

2. Function Expression

Functions can be held in variables. These functions are *anonymous functions*, and are not required to have a name.

```js
// function expression
// this is an anonymous function (an unnamed function)
// functions stored in variables do not need a name, but rather are called using the variable name
var multiply_that = function(a,b){
    return a*b;
}

mutiply_that(x,y) // run function
20 // return value
```

### Anonymous Functions

An anonymous function is a function that was declared without any named identifier to refer to it. As such, an anonymous function is usually not accessible after its initial creation.

Normal function definition:

```js
function hello() {
  alert('Hello world');
}
hello();
```

Anonymous function definition:

```js
var anon = function() {
  alert('I am anonymous');
};
anon();
```

More on [anonymous functions](https://en.wikibooks.org/wiki/JavaScript/Anonymous_functions) from wikibooks.

### Closure

Closure are local variables of a function, kept alive after the function has been returned. This can happen when you store a function within a variable, and you can refer to the function output directly. Similar to Python, you can store function returns and use them elsewhere in your code. It is a method pointer.

```js
function sayHello(name) {
    var text = 'Hello, ' + name + '!';
    var sayAlert = function() { alert(text); }
    
    return sayAlert;
}
var say = sayHello('John');

say();
alert(say.toString());    // Returns the code of the anonymous function
```

More reading on [Closures](https://en.wikibooks.org/wiki/JavaScript/Closures) from Wikibooks.

[More on Function Definition and Anonymous Functions](http://www.w3schools.com/Js/js_function_definition.asp)

##### Functions as Objects

Functions are objects, and can have both properties and methods. They can be stored as variables and referred to later. Functions can be stored within other objects as methods of that object, and then referred to later. For example:

```js
// properties and methods
var car = {
    make:"Ford",
    model: "Mustang",
    year: 2013,
    color: "Red",
    accessories: {
        windows: "Power",
        transmission: "Automatic"
    },
    start: function(){
        console.log("Vroom! Car started!");
    }
};

// view the data values
console.log(car);
console.log(car.make);

// or start the car
car.start();
```

##### Function Hoisting

If a function is declared, it can be called before the declaration. This is the default behavior of JavaScript, and it moves functions to the top of the scope. It is called *hoisting*. Function expressions are not hoisted, however.

Functions, as you see, are a pretty big topic, dig in more at the following link. [More on Functions from Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)

#### Variable Scope

Scope refers to the set of objects you have access to at any point in your script.

How long do variables last when you declare them? There are two main types of variables, global variables and local variables. Variables declared within a function are **Local** to that function. Values held within a local variable will not be usable after the function ends. Variables declared outside a function are **Global**, and can be used anywhere on the webpage.

##### Global Variable

```js
var carName = " Volvo";
// code here can use carName
function functionName() {
    // code here can use carName
}
```

##### Local Variable

```js
// code that sits here can not use carName
function functionName() {
    var carName = "Volvo";
    // code here can use carName
}
```

Assigning a value to a variable that is not declared automatically makes that variable global. In general, you want to limit the number of global variables to be only those that are required.

#### More on Methods

Methods are the options and actions that can be performed on objects. Using the car as an object analogy, the methods might be start, drive, brake, and stop. These are actions the car can perform. In other words, write a function that defines how to start the car. In JavaScript, to start the car, access the start method by using **car.start()**. Likewise, write one for brake. Access the brake method by using **car.brake()**.

#### Properties and Values

Properties are the values associated with a JavaScript object. Let's use the car example again, for the object car, say it has the properties of make, model, weight, and color. Each of these can be set to a value.

```js
// properties and methods
var car = {
    make:"Ford",
    model: "Mustang",
    year: 2013,
    color: "Red",
    accessories: {
        windows: "Power",
        transmission: "Automatic"
    },
    start: function(){
        console.log("Vroom! Car started!");
    }
};
```

This creates an object called car, then sets the properties of car to be a Red 2013 Ford Mustang. To access this property, we would type the object name and property **(objectName.property)**, for example, **car.make = "Ford"**.

If we wanted to change the color, we would access it through this method. For example, overwrite the color property currently set to "Red" by changing it to "Blue" by using the following.

```js
> car.color;
"Red"
> car.color = "Blue";
>
> car.color;
"Blue"
```

[Read more about objects and properties](http://www.w3schools.com/js/js_properties.asp)

#### Flow Control

Statements in your document will run top to bottom when your script is run, but you can control this using conditionals and loops.

* **Conditionals** are *if...else* statements.
* **Loops** are *while* or *for* statements.

##### Conditionals

Run pieces of code if an expression produces a boolean value. Your code can 'diverge' and run different paths.

Conditionals will run one block of code if true, another block if false.

```js
> var number = 100;
> 
> if(number == 100){
	console.log("True")
	} else {
	console.log("False")
	};
True
> 
> if(number == 99){
	console.log("True")
	} else {
	console.log("False")
	};
False
```

If statements can be used to check if elements on in your page, or if properties are set to certain values. For example, you can toggle layers on and off in a web map by using an if statement to see if the layers is visible. If visible is true, hide the layer, and vice versa. 

Conditionals are powerful! You can use multiple else statements to explore multiple options.

```js
var number = 100;

if(number == 100){
	console.log("Number is 100");
} else if(number < 100){
	console.log("Number is less than 100.");
} else if(number > 100){
	console.log("Number is greater than 100.");
};
```

##### Loops

Loops go through a piece of code a set number of times.

**For Loop**

A basic for loop will use the following syntax. Note the first argument is an index for the the start value, the second is a conditional for the index stating where the loop will stop when the value is false, and the last is the increment of the loop. Note the syntax, **i++** will increase i by 1 every single time the loop circles. The code in the middle is what will run.

```js
for(var i=0; i<1000, i++){
	// code here will run 1000 times, then move on to the next
}
```

You can also use for loops to loop through arrays and datasets. We'll do this in a little bit. Looks very similar to Python, we just have to declare the index variable.

```js
// iterate through a dataset, logging values to the console
for(var i in data){
    // run this on each value in data
}
```

**While Loop**

Similar to the for loop, the while loop

```js
var counter = 0;
while(counter < 1000){
	// code here will run
	counter++ // adds 1 to counter each time, will stop at 1000
}
```

Loops will run until the conditional that it is operating on evaluates to false. Loops that don't end are called infinite loops, and they will crash your program!

#### JSON: JavaScript Object Notation

Data can be stored in something called JSON, which is a JavaScript element. A JSON is structured as follows:

```js
// set employee directory dataset
var directory = {"employees":[
    {"firstName":"John", "lastName":"Doe"}, 
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]}

console.log(directory.employees)
console.log(directory.employees[1]);
console.log(directory.employees[1].firstName);
```

A GeoJSON is a Geographic JSON element, and contains geometry!

```js
var dataset = {
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [-71.093027,42.359225]
  },
  "properties": {
    "name": "MIT Main Campus"
  }
}

console.log(dataset);
console.log(dataset.type);
console.log(dataset.geometry.coordinates);
console.log(dataset.geometry.coordinates[0]);
console.log(dataset.properties);
```

#### Iterate a JSON - Putting this Together

Given that you can access data elements in arrays, you can see then how parsing and accessing various elements of your JSON is easy. Can you iterate through the directory array?

Try the following block of code in your console:

```js
// employee directory dataset
var directory = {"employees":[
    {"firstName":"John", "lastName":"Doe"}, 
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]}

// create array of employee names
var data = directory.employees;
console.log(data);

// iterate through the array, logging values to the console
for(var i in data){
    fName = data[i].firstName;
    // do something with each value of the array
    console.log(fName);
}
```
Note the differences with Python. Now wrap it in a function!

```js
function get_first_names(data){
    for(var i in data){
        fName = data[i].firstName;
        // do something with each value of the array
        console.log(fName);
    }    
}
```

#### Accessing Elements of your Page

Accessing elements of your page in JavaScript is easy because JavaScript can read the DOM, then adjust properties such as style, content, images, links, and alot more. One method you can use to get into the document is call the document object. Type this into your console and see that you can view the entire page.

```js
document;
```

Try **document.body** to see elements within the document body.

##### Access elements by ID, class, or  and make changes to properties

You can access elements by DOM selectors. Use the [W3 HTML DOM Elements](http://www.w3schools.com/js/js_htmldom_elements.asp) reference to learn more about searching through the page. 

```js
// Access element by element ID
document.getElementById("foo");

// Access element by class name
document.getElementByClassName("my_paragraphs")';
```

#### Event Listeners

Often, when working with JavaScript, you are interacting with a page. Using JavaScript, you can make element perform functions when something happens to them. This is called an event. Event listeners can be added to elements and will run functions when an event, such as a click, hover, or other user interaction occurs on that element. Example syntax, enabling a change on an element named **foo** by creating an event listener in JavaScript is as follows.

```js
// listen for a click on 'foo'
// when click occurs, run function called displayDate
document.getElementById("foo").addEventListener("click", displayDate);

// displayDate function
function displayDate() {
    document.getElementById("foo").innerHTML = Date();
}
```

The [Date](https://www.w3schools.com/jsref/jsref_obj_date.asp) object is built in and lets you work with dates and times.

#### Working with Libraries

Unless you want to become a hardcore JavaScript master, most often, you will be working with a library that is already written... Just like Python! A library is a collection of pre-written JavaScript with allows for easier development of JavaScript based applications. Libraries are packages of code that when loaded into your document allow access to the objects of that code. In this class, we are primarily going to be using two JavaScript libraries: **jQuery** and **D3**.

What are these used for?

**jQuery** is great for adding user interaction and making calls to other websites, for example, you can easily use it to load data. [Visit the jQuery homepage](http://jquery.com/).

Adding jQuery to your webpage is done by including the following line of code at the bottom of your body section.

```xml
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
```

**D3** stands for Data Driven Documents, and is a library designed for visualizing data and making beautiful interactive graphics. D3 uses JavaScript to **bind** data values to page elements and changes properties of those elements accordingly. Very powerful.

```xml
<script src="https://d3js.org/d3.v4.min.js"></script>
```

 Please put these in your page.

#### Get Started with a Simple D3 Graphic

D3 is a largely open source and freely available library. Next week, we will get into the guts of D3, but one of the best ways to get started is to read and implement some of the code available online. Mike Bostock, the creator of D3, has implemented a website called [Bl.ocks](https://bl.ocks.org/-/about) that is designed to display code and showcase examples of D3 code saved on Github. Users can create a [Github Gist](https://gist.github.com/), and then point people to Bl.ocks to view the example. For example, a really simple network block, created by user Jose Christian, can be found on [his Bl.ock page](http://bl.ocks.org/jose187/4733747).

To stand up a simple D3 visualization from blocks, copy the respective files into empty files on your server, name them appropriately, and then load your page. Can you stand up the [Force Directed Graph](http://bl.ocks.org/mbostock/4062045) at this link?

#### In Class Example

Display how to set up [D3 map of US Counties](http://bl.ocks.org/mbostock/3306362). Your homework will be based on this Bl.ock example.

#### Server-side JavaScript

JavaScript is usually a client-side language, meaning all of the code goes to the client. This can present efficiency problems and introduce security problems though, for obvious reasons. It is possible to use JavaScript on the server-side. Probably the most popular server-side JavaScript implementation is [NodeJS](https://nodejs.org/en/). NodeJS is a runtime that runs on the server to provide fast and dynamic applications, and pushes select output to the client. It can be used for both production and development, and allows you to install Leaflet, D3 and other libraries on your server. We have plenty else to focus on today, however, so this can come later.

For an intro to NodeJS, visit the [DUSPviz NodeJS mapping tutorial](http://duspviz.mit.edu/web-map-workshop/leaflet_nodejs_postgis/).

### Website Frameworks

Often, to do all of this, you don't need to reinvent the wheel. Frameworks have been created that help website developers with layout, CSS, elements, and JavaScript interactions.

For a crash course in Bootstrap, a highly used and robust framework, please visit the following tutorial.

[Bootstrap Templates](http://duspviz.mit.edu/web-map-workshop/bootstrap-templates/)

USE TEMPLATES! They will make your life so much easier!

====
### Publish your Site! Push to Github

Finally, when done with your edits. Commit your site to your Github.