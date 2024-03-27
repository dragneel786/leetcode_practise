<h2><a href="https://leetcode.com/problems/subarray-product-less-than-k/">713. Subarray Product Less Than K</a></h2><h3>Medium</h3><hr><div element-id="931"><p element-id="930">Given an array of integers <code element-id="929">nums</code> and an integer <code element-id="928">k</code>, return <em element-id="927">the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than </em><code element-id="926">k</code>.</p>

<p element-id="925">&nbsp;</p>
<p element-id="924"><strong class="example" element-id="923">Example 1:</strong></p>

<pre element-id="922"><strong element-id="921">Input:</strong> nums = [10,5,2,6], k = 100
<strong element-id="920">Output:</strong> 8
<strong element-id="919">Explanation:</strong> The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>

<p element-id="918"><strong class="example" element-id="917">Example 2:</strong></p>

<pre element-id="916"><strong element-id="915">Input:</strong> nums = [1,2,3], k = 0
<strong element-id="914">Output:</strong> 0
</pre>

<p element-id="913">&nbsp;</p>
<p element-id="912"><strong element-id="911">Constraints:</strong></p>

<ul element-id="910">
	<li element-id="909"><code element-id="908">1 &lt;= nums.length &lt;= 3 * 10<sup element-id="907">4</sup></code></li>
	<li element-id="906"><code element-id="905">1 &lt;= nums[i] &lt;= 1000</code></li>
	<li element-id="904"><code element-id="903">0 &lt;= k &lt;= 10<sup element-id="902">6</sup></code></li>
</ul>
</div>