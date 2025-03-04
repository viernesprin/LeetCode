<h2><a href="https://leetcode.com/problems/merge-strings-alternately/">1768. Merge Strings Alternately</a></h2><h3>Easy</h3>
<hr><p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. 
  If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>Return the <em>merged</em> string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> word1 = "abc", word2 = "pqr"
<strong>Output:</strong> "apbqcr"
<strong>Explanation:</strong> The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = "ab", word2 = "pqrs"
<strong>Output:</strong> "apbqrs"
<strong>Explanation:</strong> Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word1 = "abcd", word2 = "pq"
<strong>Output:</strong> "apbqcd"
<strong>Explanation:</strong> Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= word1.length, word2.length <= 100</code></li>
	<li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>
</ul>
