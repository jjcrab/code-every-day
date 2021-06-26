'''
Description
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5
Example
Example 1:

Input:

start = "a"
end = "c"
dict =["a","b","c"]
Output:

2
Explanation:

"a"->"c"

Example 2:

Input:

start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:

5
Explanation:

"hit"->"hot"->"dot"->"dog"->"cog"
'''


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # use bfs
        # add the end word to dict
        dict.add(end)
        q = collections.deque([start])
        visited = {start: 1}

        while q:
            curt_word = q.popleft()
            if curt_word == end:
                return visited[curt_word]
            for next_word in self.get_next_words(curt_word, dict):
                if next_word not in visited:
                    q.append(next_word)
                    visited[next_word] = visited[curt_word] + 1

        return 0

    def get_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != letter:
                    new_word = left + letter + right
                    if new_word in dict:
                        next_words.append(new_word)
        return next_words
