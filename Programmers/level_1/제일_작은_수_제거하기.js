function solution(arr) {
    var answer = [];
    let min_idx = 0;
    let min_value = Infinity;
    if (arr.length === 1) return [-1];
    for(let i = 0; i < arr.length; i++) {
        if (min_value > arr[i]) {
            min_value = arr[i];
            min_idx = i;
        }
    }
    arr.splice(min_idx,1);
    return arr;
}