#51 리스트 저장
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

#52 리스트에 원소 추가
movie_rank.append("배트맨")
print(movie_rank)

#53 슈퍼맨을 닥스와 스플릿 사이에 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#54 럭키 삭제
movie_rank.remove("럭키")
print(movie_rank)
movie_rank.append("럭키")
del movie_rank[-1]
print(movie_rank)

#55 스플릿 배트맨 삭제
del movie_rank[-2:]
print(movie_rank)

#56 lang1과 lang2를 합친 녀석을 만들어라
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#57 리스트에서 최댓값 최솟값 출력
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

#58 리스트 합 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59 리스트에 저장된 데이터의 개수
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60 리스트 평균
nums = [1, 2, 3, 4, 5]
avg = sum(nums) / len(nums)
print(avg)