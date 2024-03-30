<h2><a href="https://leetcode.com/problems/subarrays-with-k-different-integers/">992. Subarrays with K Different Integers</a></h2><h3>Hard</h3><hr><div element-id="873"><p element-id="872">Given an integer array <code element-id="871">nums</code> and an integer <code element-id="870">k</code>, return <em element-id="869">the number of <strong element-id="868">good subarrays</strong> of </em><code element-id="867">nums</code>.</p>

<p element-id="866">A <strong element-id="865">good array</strong> is an array where the number of different integers in that array is exactly <code element-id="864">k</code>.</p>

<ul element-id="863">
	<li element-id="862">For example, <code element-id="861">[1,2,3,1,2]</code> has <code element-id="860">3</code> different integers: <code element-id="859">1</code>, <code element-id="858">2</code>, and <code element-id="857">3</code>.</li>
</ul>

<p element-id="856">A <strong element-id="855">subarray</strong> is a <strong element-id="854">contiguous</strong> part of an array.</p>

<p element-id="853">&nbsp;</p>
<p element-id="852"><strong class="example" element-id="851">Example 1:</strong></p>

<pre element-id="850"><strong element-id="849">Input:</strong> nums = [1,2,1,2,3], k = 2
<strong element-id="848">Output:</strong> 7
<strong element-id="847">Explanation:</strong> Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
</pre>

<p element-id="846"><strong class="example" element-id="845">Example 2:</strong></p>

<pre element-id="844"><strong element-id="843">Input:</strong> nums = [1,2,1,3,4], k = 3
<strong element-id="842">Output:</strong> 3
<strong element-id="841">Explanation:</strong> Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
</pre>

<p element-id="840">&nbsp;</p>
<p element-id="839"><strong element-id="838">Constraints:</strong></p>

<ul element-id="837">
	<li element-id="836"><code element-id="835">1 &lt;= nums.length &lt;= 2 * 10<sup element-id="834">4</sup></code></li>
	<li element-id="833"><code element-id="832">1 &lt;= nums[i], k &lt;= nums.length</code></li>
</ul>
</div>