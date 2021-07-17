## 베스트앨범
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
def solution(genres, plays):
    answer = []

    # 재생횟수 기준으로 정렬된 장르 리스트 만들기
    byGenre = dict()
    byGenreAndPlay = dict()
    musicList = list(zip(genres, plays))
    for i, item in enumerate(musicList):
        # i: 고유번호, item[0]: 장르, item[1]: 재생횟수
        # 장르 순위를 위해 생성하는 딕셔너리 byGenre
        if byGenre.get(item[0]):
            byGenre[item[0]] += item[1]
        else:
            byGenre[item[0]] = item[1]
        # 장르 별 노래 재생 횟수들을 담기 위해 생성하는 딕셔너리 byGenreAndPlay
        if byGenreAndPlay.get(item[0]):
            byGenreAndPlay[item[0]].append((i,item[1]))
        else:
            byGenreAndPlay[item[0]] = [(i,item[1])]

    # byGenreAndPlay 각 장르 별 재생 노래 순위대로 내림차순 정렬
    for key in byGenreAndPlay.keys():
        byGenreAndPlay[key].sort(key=lambda x : x[1], reverse=True)

    # byGenre를 장르 별 재생 순으로 내림차순 정렬
    byGenre = list(byGenre.items())
    byGenre.sort(key=lambda x : x[1], reverse=True)
    byGenre = dict(byGenre)

    print(byGenre)
    print(byGenreAndPlay)
    print(musicList)
    
    for genre in byGenre:
        for i, play in enumerate(byGenreAndPlay.get(genre)):
            if i <= 1:
                answer.append(play[0])
            else:
                break

    return answer

print(solution(genres, plays))