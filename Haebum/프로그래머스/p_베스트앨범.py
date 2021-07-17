# 해시로 정렬 키:장르 벨류: 횟수, 고유번호
# 

def solution(genres, plays):
    answer = []
    songs = {} # 각 노래별 확인
    allGenres = {} #전체 장르별 횟수 확인하기 위한 해시
    for i in range(len(plays)):
        if songs.get(genres[i]): #해시 안에 키가 존재하냐 안하냐
            allGenres[genres[i]] += plays[i]
            songs[genres[i]].append([i,plays[i]])
        else: #존재안하면 만들어주기
            songs[genres[i]] = [[i,plays[i]]]
            allGenres[genres[i]] = plays[i]
    # 횟수별로 정렬
    allGenres = sorted(allGenres.items(),key=lambda x : x[1],reverse=True)

    for g in allGenres:
        # 횟수별 정렬
        sorted_g = sorted(songs[g[0]], key=lambda x: x[1], reverse=True)
        answer.append(sorted_g[0][0])
        if len(sorted_g) > 1:
            answer.append(sorted_g[1][0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 2500, 150, 800, 2500]
solution(genres, plays)