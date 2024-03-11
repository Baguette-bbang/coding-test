function solution(park, routes) {
    // 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
    // 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
    let graph = park.map(str => str.split(''));
    moves = {'E' : [0,1], 'W' : [0,-1], 'S' : [1,0], 'N' : [-1,0]}
    let loc_r = 0;
    let loc_c = 0;
    for (let i = 0; i < graph.length; i++) {
        for (let j = 0; j < graph[i].length; j++) {
            if (graph[i][j] === 'S') {
                loc_r = i;
                loc_c = j;
                break;
            }
        }
    }
    
    for (route of routes) {
        const direction = route[0];
        const distance = Number(route[2]);
        
        let new_r = moves[direction][0]*distance + loc_r;
        let new_c = moves[direction][1]*distance + loc_c;
        if (0 <= new_r && new_r < park.length && 0 <= new_c && new_c < park[0].length) {
            console.log(new_r, new_c)
            // 움직이는 위치 확인 
            let flag = true;
            for(let i = 1; i <= distance; i++) { // 이동 거리에 'X'가 없는지 체크
                if (graph[loc_r + moves[direction][0]*i][loc_c + moves[direction][1]*i] === 'X'){
                    flag = false;
                    break;
                }
            }
            if (flag){
                console.log(new_r, new_c)
                loc_r = new_r;
                loc_c = new_c;
            }
        }
    }
    return [loc_r, loc_c];
}