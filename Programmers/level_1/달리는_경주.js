function solution(players, callings) {
    var answer = [];
    let dictionary = {};
    for(let i = 0; i < players.length; i++) {
        dictionary[players[i]] = i;
    }
    
    for (call of callings) {
        dictionary[call] -= 1;
        dictionary[players[dictionary[call]]] += 1;
        const temp = players[dictionary[call]];
        // 기존 순서에 해당하는 플레이어
        players[dictionary[call]] = call;
        players[dictionary[call] + 1] = temp;
    }
    return players;
}