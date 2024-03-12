function solution(cards1, cards2, goal) {
    var answer = 'Yes';
    for (c of goal) {
        if (cards1[0] === c) {
            cards1.shift();
        } else if (cards2[0] === c){
            cards2.shift();
        } else {
            return 'No';
        }
    }
    return answer;
}