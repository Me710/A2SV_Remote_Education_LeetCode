class Solution(object):
    def findRestaurant(self, list1, list2):
        common_strings = []
        min_index_sum = float('inf')
        index_sum = {}

        for i, word in enumerate(list1):
            index_sum[word] = i

        for j, word in enumerate(list2):
            if word in index_sum:
                current_index_sum = j + index_sum[word]
                if current_index_sum < min_index_sum:
                    common_strings = [word]
                    min_index_sum = current_index_sum
                elif current_index_sum == min_index_sum:
                    common_strings.append(word)

        return common_strings
