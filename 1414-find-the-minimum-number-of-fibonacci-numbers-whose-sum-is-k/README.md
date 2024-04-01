<h2><a href="https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/">1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K</a></h2><h3>Medium</h3><hr><div element-id="858"><p element-id="857">Given an integer&nbsp;<code element-id="856">k</code>, <em element-id="855">return the minimum number of Fibonacci numbers whose sum is equal to </em><code element-id="854">k</code>. The same Fibonacci number can be used multiple times.</p>

<p element-id="853">The Fibonacci numbers are defined as:</p>

<ul element-id="852">
	<li element-id="851"><code element-id="850">F<sub element-id="849">1</sub> = 1</code></li>
	<li element-id="848"><code element-id="847">F<sub element-id="846">2</sub> = 1</code></li>
	<li element-id="845"><code element-id="844">F<sub element-id="843">n</sub> = F<sub element-id="842">n-1</sub> + F<sub element-id="841">n-2</sub></code> for <code element-id="840">n &gt; 2.</code></li>
</ul>
It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to <code element-id="839">k</code>.
<p element-id="838">&nbsp;</p>
<p element-id="837"><strong class="example" element-id="836">Example 1:</strong></p>

<pre element-id="835"><strong element-id="834">Input:</strong> k = 7
<strong element-id="833">Output:</strong> 2 
<strong element-id="832">Explanation:</strong> The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.</pre>

<p element-id="831"><strong class="example" element-id="830">Example 2:</strong></p>

<pre element-id="829"><strong element-id="828">Input:</strong> k = 10
<strong element-id="827">Output:</strong> 2 
<strong element-id="826">Explanation:</strong> For k = 10 we can use 2 + 8 = 10.
</pre>

<p element-id="825"><strong class="example" element-id="824">Example 3:</strong></p>

<pre element-id="823"><strong element-id="822">Input:</strong> k = 19
<strong element-id="821">Output:</strong> 3 
<strong element-id="820">Explanation:</strong> For k = 19 we can use 1 + 5 + 13 = 19.
</pre>

<p element-id="819">&nbsp;</p>
<p element-id="818"><strong element-id="817">Constraints:</strong></p>

<ul element-id="816">
	<li element-id="815"><code element-id="814">1 &lt;= k &lt;= 10<sup element-id="813">9</sup></code></li>
</ul>
</div>