function solution(n, m) {
    var answer = [];
    // 최대공약수를 구하는 법
    // 유클리드 호제법은 x, y 의 최대공약수는 y, r 의 최대공약수와 같다는 원리
    function gdb(x, y) {
        if (y === 0) return x;
        else {
            return gdb(y, x%y);
        }
    }
    // 최소공배수를 구하는 법
    // 최소공배수는 두 수의 곱 / 최대공약수 라는 공식을 이용하자.
    function lcm(x, y, gdb) {
        return x*y/gdb;
    }
    return [gdb(n,m), lcm(n,m,gdb(n,m))];
}