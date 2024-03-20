function solution(a, b) {
    let date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    let week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];
    let days = 0;
    for (let i = 0; i < a-1; i++) {
        days += date[i];
    }
    days += b-1;
    return week[days%7];
}