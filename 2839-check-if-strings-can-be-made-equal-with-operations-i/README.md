<h2><a href="https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/">2839. Check if Strings Can be Made Equal With Operations I</a></h2><h3>Easy</h3><hr><div><p>You are given two strings <code>s1</code> and <code>s2</code>, both of length <code>4</code>, consisting of <strong>lowercase</strong> English letters.</p>

<p>You can apply the following operation on any of the two strings <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two indices <code>i</code> and <code>j</code> such that <code>j - i = 2</code>, then <strong>swap</strong> the two characters at those indices in the string.</li>
</ul>

<p>Return <code>true</code><em> if you can make the strings </em><code>s1</code><em> and </em><code>s2</code><em> equal, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s1 = "abcd", s2 = "cdab"
<strong>Output:</strong> true
<strong>Explanation:</strong> We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="position: relative;"><strong>Input:</strong> s1 = "abcd", s2 = "dacb"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make the two strings equal.
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s1.length == s2.length == 4</code></li>
	<li><code>s1</code> and <code>s2</code> consist only of lowercase English letters.</li>
</ul>
</div>