var fs = require('fs')

fs.readFile('puzzle_input.txt', 'utf8', function(err, data) {
  let sum = 0;
  let arrayContent =  data.split('\n')
  arrayContent.forEach(content => {
    if (content !== '') {
      let digits = [...content.matchAll(/\d/g)];

      let first = digits[0][0]
      let last = digits[digits.length-1][0]

      let number = first + last

      sum += Number(number)
    }
  })
  console.log(sum)
});

