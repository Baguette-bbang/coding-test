function solution(name, yearning, photo) {
    var answer = [];
    let dictionary = {};
    for (let i = 0; i < name.length; i++) {
        dictionary[name[i]] = yearning[i];
    }
    
    for(let i = 0; i < photo.length; i++) {
        let score = 0;
        for (let j = 0; j < photo[i].length; j++) {
            if (dictionary[photo[i][j]] != null){
                score += dictionary[photo[i][j]];
            }
        }
        answer.push(score);
    }
    return answer;
}