function fib(n) {
    let num1 = 1;
    let num2 = 1;
    for (let i = 3; i <= n; i += 1) {
        const nextNum1 = num2;
        num2 = num1 + num2;
        num1 = nextNum1;
    }
    return num2;
}
