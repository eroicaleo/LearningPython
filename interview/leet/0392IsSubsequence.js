const isSubsequence = (s, t) => {
    let prev = new Array(1 + t.length).fill(0);
    let curr = new Array(1 + t.length).fill(0);
    for (let i = 0; i < s.length; i++) {
        for (let j = 1; j < t.length + 1; j++) {
            if (s[i] == t[j-1])
                curr[j] = prev[j - 1] + 1;
            else
                curr[j] = Math.max(prev[j], curr[j - 1]);
            if (curr[j] == s.length)
                return true;
        }
        prev = curr;
        curr = new Array(1 + t.length).fill(0);
    }
    return (s.length == 0) ? true : false;
}

console.log(isSubsequence("abc", "ahbgdc"));
console.log(isSubsequence("axc", "ahbgdc"));

let s = "rjufvjafbxnbgriwgokdgqdqewn"
let t = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"
console.log(isSubsequence(s, t));