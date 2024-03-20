function solution(n) {
    x = Math.sqrt(n)
    if (x === parseInt(x)) {
        return (x+1)**2;
    }
    return -1;
}