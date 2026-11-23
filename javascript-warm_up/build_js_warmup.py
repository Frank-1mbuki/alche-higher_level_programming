#!/usr/bin/python3
"""
Generates all task files for the javascript-warm_up project (semistandard compliant).
"""
import os

files = {
    "0-javascript_is_amazing.js": """#!/usr/bin/node
const myVar = 'JavaScript is amazing';
console.log(myVar);
""",

    "1-multi_languages.js": """#!/usr/bin/node
console.log('C is fun');
console.log('Python is cool');
console.log('JavaScript is amazing');
""",

    "2-arguments.js": """#!/usr/bin/node
const argsCount = process.argv.length - 2;

if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
""",

    "3-value_argument.js": """#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
""",

    "4-concat.js": """#!/usr/bin/node
console.log(`${process.argv[2]} is ${process.argv[3]}`);
""",

    "5-to_integer.js": """#!/usr/bin/node
const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
""",

    "6-multi_languages_loop.js": """#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const line of languages) {
  console.log(line);
}
""",

    "7-multi_c.js": """#!/usr/bin/node
const count = parseInt(process.argv[2], 10);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
""",

    "8-square.js": """#!/usr/bin/node
const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
""",

    "9-add.js": """#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const first = parseInt(process.argv[2], 10);
const second = parseInt(process.argv[3], 10);

console.log(add(first, second));
""",

    "10-factorial.js": """#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2], 10);
console.log(factorial(num));
""",

    "11-second_biggest.js": """#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
""",

    "12-object.js": """#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
""",

    "13-add.js": """#!/usr/bin/node
exports.add = function (a, b) {
  return a + b;
};
"""
}

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    os.chmod(filename, 0o755)
    print(f"Created executable script: {filename}")

print("\nAll javascript-warm_up files generated successfully!")
