class Solution(object):
    def restaurant_recommendations(self, friends_list, restaurants_map):
        final_map = {}
        all_recommendations = set()
        for group in friends_list:
            # clear recommendations in the start for every group
            all_recommendations.clear()
            # store all recommendations in a set for every friend group
            for friend in group :
                all_recommendations.update(set(restaurants_map.get(friend)))
            # loop though the recommendations and get the ones the current friend has not visited
            for friend in group:
                temp = set()
                for a in all_recommendations:
                    if a not in  restaurants_map.get(friend):
                        temp.add(a)
                # if friend in multiple group we will need all recommendations
                if friend in final_map:
                    existing_friend_recommendation = final_map.get(friend)
                    for e in existing_friend_recommendation:
                        if e not in temp:
                            temp.add(e)
                    # sorted was not necessary, Added it for manual comparisons
                    final_map[friend] = sorted(list(temp))
                else:
                    final_map[friend] = sorted(list(temp))
        return final_map


s = Solution()
friends_list = [[1,2]] 
restaurants_map = {1:['A','B'], 2:['B','C','D']}
print(s.restaurant_recommendations(friends_list, restaurants_map))

friends_list = [[1,2], [2,3,4]] 
restaurants_map = {1:['A','B'], 2:['B','C','D'], 3:['D','E','F'], 4:['G','Q','P']}
print(s.restaurant_recommendations(friends_list, restaurants_map))