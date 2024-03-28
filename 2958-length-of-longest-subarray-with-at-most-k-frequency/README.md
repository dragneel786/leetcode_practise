<h2><a href="https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/">2958. Length of Longest Subarray With at Most K Frequency</a></h2><h3>Medium</h3><hr><div element-id="881"><p element-id="880">You are given an integer array <code element-id="879">nums</code> and an integer <code element-id="878">k</code>.</p>

<p element-id="877">The <strong element-id="876">frequency</strong> of an element <code element-id="875">x</code> is the number of times it occurs in an array.</p>

<p element-id="874">An array is called <strong element-id="873">good</strong> if the frequency of each element in this array is <strong element-id="872">less than or equal</strong> to <code element-id="871">k</code>.</p>

<p element-id="870">Return <em element-id="869">the length of the <strong element-id="868">longest</strong> <strong element-id="867">good</strong> subarray of</em> <code element-id="866">nums</code><em element-id="865">.</em></p>

<p element-id="864">A <strong element-id="863">subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

<p element-id="862">&nbsp;</p>
<p element-id="861"><strong class="example" element-id="860">Example 1:</strong></p>

<pre element-id="859"><strong element-id="858">Input:</strong> nums = [1,2,3,1,2,3,1,2], k = 2
<strong element-id="857">Output:</strong> 6
<strong element-id="856">Explanation:</strong> The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.
</pre>

<p element-id="855"><strong class="example" element-id="854">Example 2:</strong></p>

<pre element-id="853"><strong element-id="852">Input:</strong> nums = [1,2,1,2,1,2,1,2], k = 1
<strong element-id="851">Output:</strong> 2
<strong element-id="850">Explanation:</strong> The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.
</pre>

<p element-id="849"><strong class="example" element-id="848">Example 3:</strong></p>

<pre element-id="847"><strong element-id="846">Input:</strong> nums = [5,5,5,5,5,5,5], k = 4
<strong element-id="845">Output:</strong> 4
<strong element-id="844">Explanation:</strong> The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
It can be shown that there are no good subarrays with length more than 4.
</pre>

<p element-id="843">&nbsp;</p>
<p element-id="842"><strong element-id="841">Constraints:</strong></p>

<ul element-id="840">
	<li element-id="839"><code element-id="838">1 &lt;= nums.length &lt;= 10<sup element-id="837">5</sup></code></li>
	<li element-id="836"><code element-id="835">1 &lt;= nums[i] &lt;= 10<sup element-id="834">9</sup></code></li>
	<li element-id="833"><code element-id="832">1 &lt;= k &lt;= nums.length</code></li>
</ul>
</div>