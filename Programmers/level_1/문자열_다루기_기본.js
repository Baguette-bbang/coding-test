function solution(s) {
    if (s.length == 4 || s.length == 6){
        for (c of s.split('')) {
            if (isNaN(+c)) {
                return false;
            }
        }
    } else {return false;}
    return true;
}
