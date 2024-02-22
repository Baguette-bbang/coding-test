from collections import defaultdict
def solution(genres, plays):
    answer = []
    # 장르 별로 가장 많이 재생된 노래
    # 이를 두 개씩 모으기
    # 노래는 고유 번호로 구분
    # 장르 선택 -> 재생 수 선택-> 고유 번호 낮은 노래
    # 고유 번호는 인덱스임
    music_dict = defaultdict(list)
    music_play = defaultdict(int)
    for i in range(len(genres)):
        music_dict[genres[i]].append([i, plays[i]])
        music_play[genres[i]] += plays[i]
    #print(music_dict)
    
    # 장르 선택
    music_play = sorted(music_play.items(), key = lambda x: x[1], reverse = True)
    #print(music_play)
    for i in range(len(music_play)):
        genre = music_play[i][0]
        music_genre = sorted(music_dict[genre], key = lambda x: x[1], reverse = True)
        #print(music_genre)
        answer.append(music_genre[0][0])
        if len(music_genre) > 1:
            answer.append(music_genre[1][0])
            
    return answer