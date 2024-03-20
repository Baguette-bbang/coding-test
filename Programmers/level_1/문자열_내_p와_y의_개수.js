function solution(s){
    const yCount = (s.match(/y/gi) || []).length;
    const pCount = (s.match(/p/gi) || []).length;

    return yCount === pCount;
}
