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


# https: // leetcode.com/problems/word-ladder/
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        len_word = len(beginWord)
        # creat a dict - hot -> *ot, h*t, ho*
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len_word):
                dic[word[:i] + "*" + word[i+1:]].append(word)

        # bfs
        queue = collections.deque([beginWord])
        visited = {beginWord: 1}
        while queue:
            word = queue.popleft()
            if word == endWord:
                return visited[word]
            for i in range(len_word):
                tmp = word[:i] + "*" + word[i + 1:]
                for word_in_dict in dic[tmp]:
                    if word_in_dict in visited:
                        continue
                    queue.append(word_in_dict)
                    visited[word_in_dict] = visited[word] + 1

        return 0
