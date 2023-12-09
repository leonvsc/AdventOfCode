const fs = require('fs');
const path = require('path');

function readData() {
    const data = fs.readFileSync(path.join(__dirname, 'example.txt'), 'utf8');
    return data;
}

function getFirstNumber() {
    data = readData()
    var firstNumber = data.match(/\d+\.\d+|\d+\b|\d+(?=\w)/g || []).map(function (v) {return +v;}).shift();
    console.log(firstNumber)
    return firstNumber
}

function getLastNumber() {
    data = readData()
    var lastNumber = data.match(/\d+\.\d+|\d+\b|\d+(?=\w)/g || []).map(function (v) {return +v;}).pop();
    console.log(lastNumber);
    return lastNumber
}

function part1(firstNumber, lastNumber) {
    
}

getFirstNumber();
getLastNumber();