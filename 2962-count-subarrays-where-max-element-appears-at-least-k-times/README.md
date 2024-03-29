<h2><a href="https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/">2962. Count Subarrays Where Max Element Appears at Least K Times</a></h2><h3>Medium</h3><hr><div element-id="812"><p element-id="811">You are given an integer array <code element-id="810">nums</code> and a <strong element-id="809">positive</strong> integer <code element-id="808">k</code>.</p>

<p element-id="807">Return <em element-id="806">the number of subarrays where the <strong element-id="805">maximum</strong> element of </em><code element-id="804">nums</code><em element-id="803"> appears <strong element-id="802">at least</strong> </em><code element-id="801">k</code><em element-id="800"> times in that subarray.</em></p>

<p element-id="799">A <strong element-id="798">subarray</strong> is a contiguous sequence of elements within an array.</p>

<p element-id="797">&nbsp;</p>
<p element-id="796"><strong class="example" element-id="795">Example 1:</strong></p>

<pre element-id="794"><strong element-id="793">Input:</strong> nums = [1,3,2,3,3], k = 2
<strong element-id="792">Output:</strong> 6
<strong element-id="791">Explanation:</strong> The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
</pre>

<p element-id="790"><strong class="example" element-id="789">Example 2:</strong></p>

<pre element-id="788"><strong element-id="787">Input:</strong> nums = [1,4,2,1], k = 3
<strong element-id="786">Output:</strong> 0
<strong element-id="785">Explanation:</strong> No subarray contains the element 4 at least 3 times.
</pre>

<p element-id="784">&nbsp;</p>
<p element-id="783"><strong element-id="782">Constraints:</strong></p>

<ul element-id="781">
	<li element-id="780"><code element-id="779">1 &lt;= nums.length &lt;= 10<sup element-id="778">5</sup></code></li>
	<li element-id="777"><code element-id="776">1 &lt;= nums[i] &lt;= 10<sup element-id="775">6</sup></code></li>
	<li element-id="774"><code element-id="773">1 &lt;= k &lt;= 10<sup element-id="772">5</sup></code></li>
</ul>
</div>