
//первый символ chatAt это 0 символ, остальные символы slice полсе 0 символа
function spinWords(string) {
  return string.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()).join(" ");
}

console.log(spinWords("Welcome")) //"emocleW"
console.log(spinWords("Hey fellow warriors")) // "Hey wollef sroirraw");
