function iterativeSumTo(n) {
    let sum = 0;
    // Note: can use let ; condition ; increment syntax
    for (const integer of [...Array(n).keys()]) {
        sum += (integer + 1);
    }
    return sum
}

function recursiveSumTo(n) {
    return (n === 1) ? n : n + sumTo(n - 1)
}

function formulaSumTo(n) {
    return n * (n + 1) / 2
}
